import cv2
import numpy as np

from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Pipette Printer',
    'author': 'Camron Blackburn <camronb@mit.edu>',
    'description': 'Lab automation assignment with pipette printer',
    'apiLevel': '2.11'
}

LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def convert_img(img_path, output_path=None):
    ''' Takes an input BGR image of any size and returns a 8x12
            (96 total) pixel version with BGR values averaged accross subsets

        optional: add output path to save 96 pixel image to the given file
    '''
    input_im = cv2.imread(img_path)

    # init plate array
    plate = np.zeros([8, 12, 3])

    # well height and width in img pixels
    well_h = int(input_im.shape[0] / plate.shape[0])
    well_w = int(input_im.shape[1] / plate.shape[1])

    for i in range(plate.shape[0]):
        for j in range(plate.shape[1]):
            h = i*well_h
            w = j*well_w
            im_subset = input_im[h:h+well_h, w:w+well_w]

            # average along height
            avg_h = np.mean(im_subset, axis=0, dtype=int)
            # then average along width
            avg_bgr = np.mean(avg_h, axis=0, dtype=int)
            plate[i,j] = avg_bgr

    if output_path:
        cv2.imwrite(output_path, plate)

    return plate

def px_to_uL(px):
    ''' Convert BGR pixel values to real volumes that can be manipulated
          by opentrons. result expands values to (h,w,4) array for four-channel
          CMYK values
              - BGR values must be converted to CMYK values
              - scale percentage values from CMYK to fit in 500 uL wells
              - drop volumes below 10uL, since picking up anything this size in
                  the p300 pipette has the highest error
                    https://opentrons.com/pipettes/
    '''
    # convert BGR values to CMYK
    px = px/255
    K = 1-np.amax(px, axis=2)
    C = (1-px[:,:,2] - K)/(1-K)
    M = (1-px[:,:,1] - K)/(1-K)
    Y = (1-px[:,:,0] - K)/(1-K)
    CMYK = np.stack([C, M, Y, K], axis=2)

    # CMYK gives values in percentages with each
    #   color channel having 100% possible
    # convert this to 100 uL for 100%
    uL = np.around(CMYK*100)

    # then drop small volumes
    uL = (uL > 10) * uL
    return uL

def color_run(canvas, pipette, color, vols, w_log):
    '''
        pass in:
        pipette
        color: the location of color in palette
        vols: a [8x12] array of volumes
        w_log: water log to keep track of water volume
            to be passed at the end

        returns water log to pass it on for final water round
    '''
    pipette.pick_up_tip()

    # get color and fill to max
    max_fill = 300
    pipette.aspirate(max_fill, color)

    remaining = max_fill
    for i in range(8):
        for j in range(12):
            vol = vols[i,j]

            # skip if the color channel is 0
            if vol == 0:
                continue

            # check that there is enough dye in the pipette to
            #    complete the next well, if not refill
            if vol > remaining:
                pipette.dispense(remaining, color)
                pipette.aspirate(max_fill, color)
                remaining = max_fill

            # find volume location on plate then
            #    dispense and update the remaining volume value
            plate_loc = LETTERS[i] + str(j+1)
            pipette.dispense(vol, canvas[plate_loc])
            remaining -= vol

            # keep track of water added to well at the end
            water = 100 - vol
            w_log[i,j] += water

    pipette.drop_tip()
    return w_log



# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    # NOTE: Do not change anything in this section, we will assume the OpenTrons
    # is set up according to this configuration
    # ---------------------------------------------------------------------------
    # labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    palette = protocol.load_labware('usascientific_12_reservoir_22ml', '2')
    canvas = protocol.load_labware('nest_96_wellplate_200ul_flat', '5')

    ## add black color ?
    ## could be done just by mixing all the dyes
    color = {
        'green': 'A1',
        'blue': 'A2',
        'red': 'A3',
        'yellow': 'A4',
        'black': 'A5',
        'clear': 'A6'  # water well
    }

    # pipettes
    left_pipette = protocol.load_instrument(
         'p300_single', 'left', tip_racks=[tiprack])

    # NOTE: Describe your commands below this line
    # ---------------------------------------------------------------------------
    # make sure you are pipetting FROM the palette TO the canvas
    # use the color map for easy well reference:
    # palette[color['green']] == palette['A1']


    #I liked starry night best so load that one ...
    input_path = "./input_im/starry_night.jpg"
    bgr_px = convert_img(input_path)

    plate_CMYK = px_to_uL(bgr_px)
    print(plate_CMYK)

    water_log = np.zeros([8, 12])

    # do all blue/cyan dye
    water_log = color_run(canvas, left_pipette, palette[color['blue']], plate_CMYK[:,:,0], water_log)

    # then all red/magenta
    water_log = color_run(canvas, left_pipette, palette[color['red']], plate_CMYK[:,:,1], water_log)

    # wow this is so ugly passing water_log in and out
    # then yellow
    water_log = color_run(canvas, left_pipette, palette[color['yellow']], plate_CMYK[:,:,2], water_log)

    # final color black
    water_log = color_run(canvas, left_pipette, palette[color['black']], plate_CMYK[:,:,3], water_log)

    # then the pass of water for dilution
    #  throw away water log output bc we don't need it and fake one to reuse the func
    _ = color_run(canvas, left_pipette, palette[color['clear']], water_log, np.zeros([8,12]))

    return
