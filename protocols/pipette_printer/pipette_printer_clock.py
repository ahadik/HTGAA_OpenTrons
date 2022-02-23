from opentrons import protocol_api
from datetime import datetime

# metadata
metadata = {
    'protocolName': 'Pipette Printer',
    'author': 'Alex Hadik <ahadik@mit.edu>',
    'description': 'A simple protocol template for the pipette printing lab.',
    'apiLevel': '2.11'
}

print('hello')

#
def get_rows(column, start_row_index, end_row_index):
    wells = []
    for i in range(start_row_index, end_row_index + 1):
        ascii_num = i + 64
        wells.append(chr(ascii_num)+str(column))
    return wells

def get_wells_for_digit(digit, column_offset):
    wells = []
    if digit == 0:
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 1, 8, 8)
        wells.append(get_rows(column_offset + 2, 1, 8))
        return wells
    elif digit == 1:
        wells += get_rows(column_offset + 1, 1, 8)
        wells += get_rows(column_offset, 2, 2)
        wells += get_rows(column_offset, 8, 8)
        wells += get_rows(column_offset + 2, 1, 1)
        return wells
    elif digit == 2:
        wells += get_rows(column_offset, 1, 1)
        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 2, 1, 5)

        wells += get_rows(column_offset + 1, 5, 5)
        wells += get_rows(column_offset, 5, 8)

        wells += get_rows(column_offset + 1, 8, 8)
        wells += get_rows(column_offset + 2, 8, 8)
        return wells
    elif digit == 3:
        wells += get_rows(column_offset + 2, 1, 8)

        wells += get_rows(column_offset, 1, 1)
        wells += get_rows(column_offset + 1, 1, 1)

        wells += get_rows(column_offset, 5, 5)
        wells += get_rows(column_offset + 1, 5, 5)

        wells += get_rows(column_offset, 8, 8)
        wells += get_rows(column_offset + 1, 8, 8)
        return wells
    elif digit == 4:
        wells += get_rows(column_offset + 2, 1, 8)
        wells += get_rows(column_offset, 1, 4)
        wells += get_rows(column_offset + 1, 4, 4)

        return wells
    elif digit == 5:
        wells += get_rows(column_offset, 1, 4)
        wells += get_rows(column_offset + 2, 4, 8)

        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 2, 1, 1)

        wells += get_rows(column_offset + 1, 4, 4)

        wells += get_rows(column_offset, 8, 8)
        wells += get_rows(column_offset, 8, 8)
        return wells
    elif digit == 6:
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 2, 5, 8)

        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 2, 1, 1)
        wells += get_rows(column_offset + 1, 5, 5)
        wells += get_rows(column_offset + 1, 8, 8)

        return wells
    elif digit == 7:
        wells += get_rows(column_offset + 2, 1, 8)

        wells += get_rows(column_offset, 1, 1)
        wells += get_rows(column_offset + 1, 1, 1)

        return wells
    elif digit == 8:
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 2, 1, 8)

        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 1, 4, 4)
        wells += get_rows(column_offset + 1, 8, 8)
        return wells
    else:
        wells += get_rows(column_offset + 2, 1, 8)
        wells += get_rows(column_offset, 1, 4)

        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 1, 4, 4)
        return wells

def paint_digit(digit, column_offset, color_well, pipette, canvas):
    wells = get_wells_for_digit(digit, column_offset)

    pipette.pick_up_tip()
    
    for well in wells:
        pipette.aspirate(100, color_well)
        pipette.dispense(100, canvas[well])

    pipette.drop_tip()


# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    # labware
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    palette = protocol.load_labware('usascientific_12_reservoir_22ml', '2')
    canvas = protocol.load_labware('nest_96_wellplate_200ul_flat', '5')

    palette_map = {
        'green': 'A1',
        'blue': 'A2',
        'red': 'A3',
        'yellow': 'A4'
    }

    # pipettes
    left_pipette = protocol.load_instrument(
         'p300_single', 'left', tip_racks=[tiprack])

    #get time
    now = datetime.now()
    current_time = now.strftime("%H%M")

    # commands
    i = 0
    for digit in current_time:
        color_well = palette[list(palette_map.values())[i]]
        paint_digit(digit, (i * 3) + 1, color_well, left_pipette, canvas)
        i += 1

    
    