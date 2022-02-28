from opentrons import protocol_api, types

#input AG23
#print('Enter your two-letter initials (in caps) and two-digit graduation year:')
input_data = 'AG23'
#print(input_data)


#appended to template provided by adding 3x8 rows/ column alphabet mapping
# metadata
metadata = {
    'protocolName': 'Pipette Printer',
    'author': 'Alex Hadik <ahadik@mit.edu>',
    'description': 'A simple protocol template for the pipette printing lab.',
    'apiLevel': '2.11'
}

#library of digits and letters
def get_rows(column, start_row_index, end_row_index):
    wells = []
    for i in range(start_row_index, end_row_index + 1):
        ascii_num = i + 64
        wells.append(chr(ascii_num)+str(column))
    return wells

def get_wells_for_digit(digit, column_offset):
    wells = []
    if digit == "0":
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 1, 8, 8)
        wells += get_rows(column_offset + 2, 1, 8)
        return wells

    elif digit == "1":
        wells += get_rows(column_offset + 1, 1, 8)
        wells += get_rows(column_offset, 2, 2)
        wells += get_rows(column_offset, 8, 8)
        wells += get_rows(column_offset + 2, 8, 8)
        return wells

    elif digit == "2":
        wells += get_rows(column_offset, 1, 1)
        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 2, 1, 5)

        wells += get_rows(column_offset + 1, 5, 5)
        wells += get_rows(column_offset, 5, 8)

        wells += get_rows(column_offset + 1, 8, 8)
        wells += get_rows(column_offset + 2, 8, 8)
        return wells

    elif digit == "3":
        wells += get_rows(column_offset + 2, 1, 8)

        wells += get_rows(column_offset, 1, 1)
        wells += get_rows(column_offset + 1, 1, 1)

        wells += get_rows(column_offset, 5, 5)
        wells += get_rows(column_offset + 1, 5, 5)

        wells += get_rows(column_offset, 8, 8)
        wells += get_rows(column_offset + 1, 8, 8)
        return wells

    elif digit == "4":
        wells += get_rows(column_offset + 2, 1, 8)
        wells += get_rows(column_offset, 1, 4)
        wells += get_rows(column_offset + 1, 4, 4)

        return wells

    elif digit == "5":
        wells += get_rows(column_offset, 1, 4)
        wells += get_rows(column_offset + 2, 4, 8)

        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 2, 1, 1)

        wells += get_rows(column_offset + 1, 4, 4)

        wells += get_rows(column_offset, 8, 8)
        wells += get_rows(column_offset+1, 8, 8)
        return wells

    elif digit == "6":
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 2, 5, 8)

        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 2, 1, 1)
        wells += get_rows(column_offset + 1, 5, 5)
        wells += get_rows(column_offset + 1, 8, 8)

        return wells

    elif digit == "7":
        wells += get_rows(column_offset + 2, 1, 8)

        wells += get_rows(column_offset, 1, 1)
        wells += get_rows(column_offset + 1, 1, 1)

        return wells
    elif digit == "8":
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 2, 1, 8)

        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 1, 4, 4)
        wells += get_rows(column_offset + 1, 8, 8)
        return wells
    
    elif digit == "9":
        wells += get_rows(column_offset + 2, 1, 8)
        wells += get_rows(column_offset, 1, 4)

        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 1, 4, 4)
        return wells
    
    elif digit == "A":
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 2, 1, 8)
        wells += get_rows(column_offset + 1, 4, 4)
        return wells
    
    elif digit == "B":
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 1, 4, 5)
        wells += get_rows(column_offset + 1, 8, 8)
        wells += get_rows(column_offset + 2, 2, 3)
        wells += get_rows(column_offset + 2, 6, 7)
        return wells
    
    elif digit == "C":
        wells += get_rows(column_offset, 2, 7)
        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 1, 8, 8)
        wells += get_rows(column_offset + 2, 1, 1)
        wells += get_rows(column_offset + 2, 8, 8)
        return wells
    
    elif digit == "D":
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 1, 8, 8)
        wells += get_rows(column_offset + 2, 2, 7)
        return wells
    
    elif digit == "E":
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 1, 4, 4)
        wells += get_rows(column_offset + 1, 8, 8)
        wells += get_rows(column_offset + 2, 1, 1)
        wells += get_rows(column_offset + 2, 4, 4)
        wells += get_rows(column_offset + 2, 8,8)
        return wells
    
    elif digit == "F":
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 1, 4, 4)
        wells += get_rows(column_offset + 2, 1, 1)
        wells += get_rows(column_offset + 2, 4, 4)
        return wells

    elif digit == "G":
        wells += get_rows(column_offset, 2, 4)
        wells += get_rows(column_offset, 7, 8)
        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 1, 5, 5)
        wells += get_rows(column_offset + 1, 8, 8)
        wells += get_rows(column_offset + 2, 1, 8)
        return wells
    
    elif digit == "H":
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 1, 4, 4)
        wells += get_rows(column_offset + 2, 1, 8)
        return wells

    elif digit == "I":
        wells += get_rows(column_offset, 1, 1)
        wells += get_rows(column_offset, 8, 8)
        wells += get_rows(column_offset + 1, 1, 8)
        wells += get_rows(column_offset + 2, 1, 1)
        wells += get_rows(column_offset + 2, 8, 8)
        return wells
    
    elif digit == "J":
        wells += get_rows(column_offset, 1, 1)
        wells += get_rows(column_offset, 6, 7)
        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 1, 1, 8)
        wells += get_rows(column_offset + 2, 1, 7)
        return wells
    
    elif digit == "K":
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 1, 4, 5)
        wells += get_rows(column_offset + 2, 1, 3)
        wells += get_rows(column_offset + 2, 6, 8)
        return wells
    
    elif digit == "L":
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 1, 8, 8)
        wells += get_rows(column_offset + 2, 8, 8)
        return wells
    
    elif digit == "M":
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 1, 3, 4)
        wells += get_rows(column_offset + 2, 1, 8)
        return wells
    
    elif digit == "N":
        wells += get_rows(column_offset, 2, 8)
        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 2, 2, 8)
        return wells

    elif digit == "O":
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 1, 8, 8)
        wells += get_rows(column_offset + 2, 1, 8)
        return wells
    
    elif digit == "P":
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 1, 4, 4)
        wells += get_rows(column_offset + 2, 2, 3)
        return wells
    
    elif digit == "Q":
        wells += get_rows(column_offset, 1, 6)
        wells += get_rows(column_offset + 1, 5, 7)
        wells += get_rows(column_offset + 2, 1, 6)
        wells += get_rows(column_offset + 2, 8, 8)
        return wells
    
    elif digit == "R":
        wells += get_rows(column_offset, 2, 8)
        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 1, 4, 5)
        wells += get_rows(column_offset + 2, 2, 3)
        wells += get_rows(column_offset + 2, 6, 8)
        return wells
    
    elif digit == "S":
        wells += get_rows(column_offset, 2, 4)
        wells += get_rows(column_offset, 7, 7)
        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 1, 5, 5)
        wells += get_rows(column_offset + 1, 8, 8)
        wells += get_rows(column_offset + 2, 2, 3)
        wells += get_rows(column_offset + 2, 6, 8)
        return wells
    
    elif digit == "T":
        wells += get_rows(column_offset, 1, 1)
        wells += get_rows(column_offset + 1, 1, 8)
        wells += get_rows(column_offset + 2, 2, 8)
        return wells
    
    elif digit == "U":
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 1, 8, 8)
        wells += get_rows(column_offset + 2, 1, 8)
        return wells

    elif digit == "V":
        wells += get_rows(column_offset, 1, 7)
        wells += get_rows(column_offset + 1, 8, 8)
        wells += get_rows(column_offset + 2, 1, 7)
        return wells
    
    elif digit == "W":
        wells += get_rows(column_offset, 1, 8)
        wells += get_rows(column_offset + 1, 6, 8)
        wells += get_rows(column_offset + 2, 1, 8)
        return wells
    
    elif digit == "X":
        wells += get_rows(column_offset, 1, 3)
        wells += get_rows(column_offset, 6, 8)
        wells += get_rows(column_offset + 1, 4, 5)
        wells += get_rows(column_offset + 2, 1, 3)
        wells += get_rows(column_offset + 2, 6, 8)
        return wells
    
    elif digit == "Y":
        wells += get_rows(column_offset, 1, 4)
        wells += get_rows(column_offset, 6, 8)
        wells += get_rows(column_offset + 1, 4, 4)
        wells += get_rows(column_offset + 1, 8, 4)
        wells += get_rows(column_offset + 2, 1, 8)
        return wells
    
    elif digit == "Z":
        wells += get_rows(column_offset, 1, 1)
        wells += get_rows(column_offset, 6, 8)
        wells += get_rows(column_offset + 1, 1, 1)
        wells += get_rows(column_offset + 1, 5, 5)
        wells += get_rows(column_offset + 1, 8, 8)
        wells += get_rows(column_offset + 2, 1, 4)
        wells += get_rows(column_offset + 2, 8, 8)
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

    protocol.comment('Message is: ' + input_data)

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


    # commands
    i = 0
    j=[1, 3, 0, 2] 
    for digit in str(input_data):
        color_well = palette[list(palette_map.values())[j[i]]]
        paint_digit(digit, (i * 3) + 1, color_well, left_pipette, canvas)
        i += 1
     