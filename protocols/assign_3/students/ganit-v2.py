from opentrons import protocol_api

# metadata
metadata = {
		'protocolName': 'Pipette Printer',
    'author': 'Alex Hadik <ahadik@mit.edu>',
    'description': 'A simple protocol template for the pipette printing lab.',
    'apiLevel': '2.11'
}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    # labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    palette = protocol.load_labware('usascientific_12_reservoir_22ml', '2')
    canvas = protocol.load_labware('nest_96_wellplate_200ul_flat', '5')

    # pipettes
    left_pipette = protocol.load_instrument(
         'p300_single', 'left', tip_racks=[tiprack])
         
    yellow = palette['A4']
    red = palette['A3']
    blue = palette['A2']
    green = palette['A1']

    # commands
 
    colors = [yellow, red, blue, green]
    wells = ['A1', 'B3', 'C5', 'D5']
    
    # pattern = [['A1', blue], ['B2', yellow]]
        
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    rows = [i for i in range(1,13)]
    last_color = 'yellow'
    
    color_map = {
        'yellow': yellow,
        'red': red,
        'blue': blue,
        'green': green
    }

    instructions = {
        'yellow': [],
        'red': [],
        'blue': [],
        'green': []
    }
    for column in columns:
        for row in rows:
            #left_pipette.pick_up_tip()
            #left_pipette.aspirate(100, last_color) 
            #left_pipette.dispense(100, canvas[column + str(row)])
            #left_pipette.drop_tip()

            instructions[last_color].append(column + str(row))
            
            if last_color == 'yellow':
                last_color = 'blue'
            elif last_color == 'blue':
                last_color = 'red'
            else:
                last_color = 'yellow'

    for color in instructions.keys():
        if (len(instructions[color])):
            left_pipette.distribute(100, color_map[color], [canvas.wells_by_name()[well_name] for well_name in instructions[color]])
        #left_pipette.pick_up_tip()
        #for well in instructions[color]:
            #left_pipette.aspirate(100, color_map[color])
            #left_pipette.dispense(100, canvas[well])
        #left_pipette.drop_tip()

    
    # for well, color in pattern:
        # left_pipette.pick_up_tip()
        # left_pipette.aspirate(100, color) 
        # left_pipette.dispense(100, canvas[well])
        # left_pipette.drop_tip()
    
            

    # left_pipette.pick_up_tip()
    # left_pipette.aspirate(100, palette['A2'])
    # left_pipette.dispense(100, canvas['A2'])
    # left_pipette.drop_tip()