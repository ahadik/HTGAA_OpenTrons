from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Pipette Printer',
    'author': 'Ido Calman <calman@mit.edu>',
    'description': 'A simple protocol template for the pipette printing lab.',
    'apiLevel': '2.11'
}


# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    # NOTE: Do not change anything in this section â€” we will assume the OpenTrons
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

    COLS = 12
    ROWS = "ABCDEFGH"
    MAX_VOL = 280

    red_pal = palette[color['red']]
    green_pal = palette[color['green']]
    blue_pal = palette[color['blue']]
    pals = [red_pal, green_pal, blue_pal]

    def hex_to_rgb(h):
        values = h[1:]
        return tuple(int(values[i:i+2], 16) for i in (0, 2, 4))

    def normalized_rgb(rgb):
        relative_rgb = [x / 255 for x in rgb]
        return tuple(int(x * MAX_VOL) for x in relative_rgb)

    def paint_rows(start_row, end_row, color_vals):
        start_row = int(start_row)
        end_row = int(end_row)

        for j, val in enumerate(color_vals):
            if val > 0:
                # efficient tips, pickup every change of color
                pal = pals[j]
                left_pipette.pick_up_tip()
                for i in range(start_row, end_row):
                    row = ROWS[i]
                    for col in range(COLS):
                        cell = canvas[row + str(col + 1)]
                        left_pipette.aspirate(val, pal)
                        left_pipette.dispense(val, cell)
                left_pipette.drop_tip()

        # mix all tubes
        left_pipette.pick_up_tip()
        for i in range(start_row, end_row):
            row = ROWS[i]
            for col in range(COLS):
                left_pipette.mix(3, MAX_VOL, canvas[row + str(col + 1)])
        left_pipette.drop_tip()

    # paint first half of the flag
    ukraine_blue = "#3366ff"
    blue_vals = normalized_rgb(hex_to_rgb(ukraine_blue))
    paint_rows(0, len(ROWS) / 2, blue_vals)

    # paint second half of the flag
    ukraine_yellow = "#fecb00"
    yellow_vals = normalized_rgb(hex_to_rgb(ukraine_yellow))
    paint_rows(len(ROWS) / 2, len(ROWS), yellow_vals)
