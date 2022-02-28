from opentrons import protocol_api
import numpy as np

# metadata
metadata = {
    'protocolName': 'Pipette Printer',
    'author': 'Ilan Mitnikov <ilanm@mit.edu>',
    'description': 'Draw a molecule',
    'apiLevel': '2.11'
}


# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):
    # NOTE: Do not change anything in this section — we will assume the OpenTrons
    # is set up according to this configuration
    # ---------------------------------------------------------------------------
    # labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    palette = protocol.load_labware('usascientific_12_reservoir_22ml', '2')
    canvas = protocol.load_labware('nest_96_wellplate_200ul_flat', '5')

    color = {
        'green': 'A1',
        'blue': 'A2',
        'red': 'A3',
        'yellow': 'A4'
    }

    # pipettes
    left_pipette = protocol.load_instrument(
        'p300_single', 'left', tip_racks=[tiprack])

    # NOTE: Describe your commands below this line
    # ---------------------------------------------------------------------------

    # set dispense height such that doesn't touch the liquid in the well
    left_pipette.well_bottom_clearance.dispense = canvas.well(0).depth

    red_drops, green_drops, blue_drops, yellow_drops, wells = image_to_drops(IMAGE, canvas)

    left_pipette.distribute(red_drops, palette[color['red']], wells)
    left_pipette.distribute(green_drops, palette[color['green']], wells)
    left_pipette.distribute(blue_drops, palette[color['blue']], wells)
    left_pipette.distribute(yellow_drops, palette[color['yellow']], wells)


def image_to_drops(img, canvas):
    blue_drops = []
    red_drops = []  # list of volumes and locations
    yellow_drops = []
    green_drops = []
    wells = []
    for y in range(8):
        for x in range(12):
            if sum(img[y, x]) == 0:
                continue
            a = img[y, x]
            a = a / sum(a) * 100  # normalize
            # let CMYK be BRYG
            wells.append(xy_to_well(x, y, canvas))
            blue_drops.append(int(a[0]))
            red_drops.append(int(a[1]))
            yellow_drops.append(int(a[2]))
            green_drops.append(int(a[3]))
    return red_drops, green_drops, blue_drops, yellow_drops, wells


def xy_to_well(x, y, canvas):
    y_dict = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
    y = y_dict[y]
    x += 1

    return canvas.well(f"{y}{x}")


# (8, 12, 4) shape
IMAGE = np.array([[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 6, 13, 0], [11, 25, 44, 0], [37, 44, 58, 0],
                   [7, 31, 61, 0], [1, 6, 13, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                  [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 20, 43, 0], [43, 40, 32, 0], [140, 94, 17, 0],
                   [24, 25, 23, 0], [1, 2, 4, 0], [10, 6, 33, 0], [11, 7, 43, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                  [[0, 0, 0, 0], [0, 0, 0, 0], [7, 20, 20, 0], [4, 20, 21, 0], [4, 4, 2, 0], [47, 106, 100, 0],
                   [24, 91, 93, 0], [88, 53, 4, 0], [73, 41, 37, 0], [9, 6, 43, 0], [0, 3, 7, 0], [0, 3, 8, 0]],
                  [[0, 5, 11, 0], [6, 5, 4, 0], [46, 103, 99, 0], [26, 98, 101, 0], [80, 48, 5, 0], [64, 60, 35, 0],
                   [9, 29, 30, 0], [70, 63, 26, 0], [56, 77, 55, 0], [30, 20, 5, 0], [40, 38, 38, 0], [3, 22, 46, 0]],
                  [[2, 31, 66, 0], [72, 51, 18, 0], [127, 85, 19, 0], [16, 25, 22, 0], [99, 64, 6, 0], [91, 52, 5, 0],
                   [40, 22, 1, 0], [54, 69, 53, 0], [30, 114, 120, 0], [83, 69, 29, 0], [102, 74, 31, 0],
                   [5, 30, 62, 0]],
                  [[0, 3, 7, 0], [17, 20, 20, 0], [55, 80, 62, 0], [33, 126, 132, 0], [69, 55, 16, 0], [116, 72, 7, 0],
                   [105, 68, 8, 0], [93, 57, 37, 0], [4, 5, 12, 0], [4, 24, 48, 0], [4, 14, 25, 0], [0, 5, 11, 0]],
                  [[0, 7, 14, 0], [44, 50, 53, 0], [131, 88, 21, 0], [25, 45, 47, 0], [2, 6, 8, 0], [4, 3, 1, 0],
                   [4, 3, 6, 0], [22, 14, 82, 0], [4, 3, 23, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                  [[0, 7, 15, 0], [21, 42, 65, 0], [55, 39, 10, 0], [8, 31, 58, 0], [1, 9, 20, 0], [0, 0, 0, 0],
                   [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]])
