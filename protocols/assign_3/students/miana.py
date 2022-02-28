from opentrons import protocol_api, simulate
import numpy as np

# metadata
metadata = {
    'protocolName': 'Pipette Printer',
    'author': 'miana',
    'description': 'Conway glider ish thing.',
    'apiLevel': '2.11'
}

def wellToindex(well):
    x = ord(well[0])-65
    y = int(well[1]) - 1
    return x,y

def indexTowell(ind):
    well = chr(ind[0]+65)
    well+=(str(ind[1]+1))
    return well

def run(protocol: protocol_api.ProtocolContext):

    # NOTE: Do not change anything in this section we will assume the OpenTrons
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
    # make sure you are pipetting FROM the palette TO the canvas
    # use the color mpa for easy well reference:
    # palette[color['green']] == palette['A1']

    plate = np.zeros((8,12))
    #print(plate)

    #initial configuration
    #set up two gliders
    left_pipette.pick_up_tip()
    left_pipette.aspirate(300, palette['A1'])
    left_pipette.dispense(100, canvas['A1'])
    plate[wellToindex('A1')] = 1
    #print(plate)
    #print(wellToindex('B2'))
    left_pipette.dispense(100, canvas['B2'])
    plate[wellToindex('B2')] = 1
    left_pipette.dispense(100, canvas['B3'])
    plate[wellToindex('B3')] = 1

    left_pipette.aspirate(200, palette['A1'])
    left_pipette.dispense(100, canvas['C1'])
    plate[wellToindex('C1')] = 1
    left_pipette.dispense(100, canvas['C2'])
    plate[wellToindex('C2')] = 1
    left_pipette.drop_tip()

    left_pipette.pick_up_tip()
    left_pipette.aspirate(300, palette['A2'])
    left_pipette.dispense(100, canvas['B8'])
    plate[wellToindex('B8')] = 1
    left_pipette.dispense(100, canvas['C6'])
    plate[wellToindex('C6')] = 1
    left_pipette.dispense(100, canvas['C8'])
    plate[wellToindex('C8')] = 1

    left_pipette.aspirate(200, palette['A2'])
    left_pipette.dispense(100, canvas['D7'])
    plate[wellToindex('D7')] = 1
    left_pipette.dispense(100, canvas['D8'])
    plate[wellToindex('D8')] = 1
    left_pipette.drop_tip()
    #print(plate)
    
    #following time steps, we'll do 16. 
    n=0
    N = plate.shape[0]
    M = plate.shape[1]
    #plateCopy=np.copy(plate)
    while n<16:
        plateCopy=np.copy(plate)
        #print(plateCopy)
        #Select color
        if n%4==0:
            col = 'A2'
        elif n%4==1:
            col = 'A3'
        elif n%4==2:
            col = 'A4'
        else:
            col = 'A1'
        #Play game
        for i in range(plate.shape[0]):
            for j in range(plate.shape[1]):
                #print(plate[(i-1)%N,(j-1)%M])
                total = (plate[(i-1)%N,(j-1)%M] + \
                plate[(i-1)%N,j] + \
                plate[(i-1)%N,(j+1)%M] + \
                plate[i,(j-1)%M] + \
                plate[i,(j+1)%M] + \
                plate[(i+1)%N,(j-1)%M] + \
                plate[(i+1)%N,j] + \
                plate[(i+1)%N,(j+1)%M])
                #print((i,j))
                #print((plate[(i-1)%N,(j-1)%M],plate[(i-1)%N,j],plate[(i-1)%N,(j+1)%M],(i, (j-1)%M),plate[i%N,(j+1)%M],plate[(i+1)%N,(j-1)%M],plate[(i+1)%N,j],plate[(i+1)%N,(j+1)%M]))
                if plate[i,j] == 1:
                    if (total < 2) or (total > 3):
                        plateCopy[i,j]=0
                else:
                    if total == 3:
                        plateCopy[i,j]=1
                        left_pipette.pick_up_tip()
                        left_pipette.aspirate(100, palette[col])
                        left_pipette.dispense(100, canvas[indexTowell([i,j])])
                        #print(indexTowell([i,j]))
                        left_pipette.drop_tip()
        plate = plateCopy
        n+=1