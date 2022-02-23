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
    # make sure you are pipetting FROM the palette TO the canvas
    # use the color mpa for easy well reference:
    # palette[color['green']] == palette['A1']
    