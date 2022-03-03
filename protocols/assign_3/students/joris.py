from opentrons import protocol_api

# metadata
metadata = {
		'protocolName': 'Fireball',
    'author': 'Joris Komen <komen@mit.edu>',
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
        'yellow': 'A4',
        'dilutant': 'A6'
        
    }

    # pipettes
    left_pipette = protocol.load_instrument(
         'p300_single', 'left', tip_racks=[tiprack])

    # NOTE: Describe your commands below this line
    # ---------------------------------------------------------------------------
    # make sure you are pipetting FROM the palette TO the canvas
    # use the color mpa for easy well reference:
    # palette[color['green']] == palette['A1']

       # commands
   # commands
    #yellow
    left_pipette.pick_up_tip()
    left_pipette.aspirate(300, palette['A4'])
    left_pipette.dispense(100, canvas['C12'])
    left_pipette.dispense(100, canvas['D12'])
    left_pipette.dispense(100, canvas['E12'])
    left_pipette.aspirate(300, palette['A4'])
    left_pipette.dispense(100, canvas['F12'])
    left_pipette.dispense(100, canvas['G8'])
    left_pipette.dispense(100, canvas['G9'])
    left_pipette.aspirate(300, palette['A4'])
    left_pipette.dispense(100, canvas['B8'])
    left_pipette.dispense(100, canvas['B9'])
    #orangestep1
    left_pipette.dispense(50, canvas['D9'])
    left_pipette.dispense(50, canvas['E9'])
    left_pipette.aspirate(100, palette['A4'])
    left_pipette.dispense(50, canvas['E10'])
    left_pipette.dispense(50, canvas['D10'])
    left_pipette.drop_tip()

    #red
    left_pipette.pick_up_tip()
    left_pipette.aspirate(300, palette['A3'])
    left_pipette.dispense(100, canvas['C8'])
    left_pipette.dispense(100, canvas['C9'])
    left_pipette.dispense(100, canvas['C10'])
    left_pipette.aspirate(300, palette['A3'])
    left_pipette.dispense(100, canvas['C11'])
    left_pipette.dispense(100, canvas['D11'])
    left_pipette.dispense(100, canvas['E11'])
    left_pipette.aspirate(200, palette['A3'])
    left_pipette.dispense(100, canvas['F11'])
    left_pipette.dispense(100, canvas['F10'])
    left_pipette.dispense(100, canvas['F9'])
    left_pipette.aspirate(200, palette['A3'])
    left_pipette.dispense(100, canvas['F8'])
    left_pipette.dispense(100, canvas['E8'])
    left_pipette.dispense(100, canvas['D8'])
    #orangestep2
    left_pipette.aspirate(200, palette['A3'])
    left_pipette.dispense(50, canvas['E9'])
    left_pipette.dispense(50, canvas['D9'])
    left_pipette.dispense(50, canvas['D10'])
    left_pipette.dispense(50, canvas['E10'])
    left_pipette.mix(4, 98, canvas['E9'])
    left_pipette.mix(4, 98, canvas['D9'])
    left_pipette.mix(4, 98, canvas['D10'])
    left_pipette.mix(4, 98, canvas['E10'])
    left_pipette.drop_tip()

    #green
    left_pipette.pick_up_tip()
    left_pipette.aspirate(300, palette['A1'])
    left_pipette.dispense(100, canvas['A1'])
    left_pipette.dispense(100, canvas['A12'])
    left_pipette.dispense(100, canvas['H6'])
    left_pipette.aspirate(100, palette['A1'])
    left_pipette.dispense(100, canvas['H7'])
    left_pipette.drop_tip()

    #blue
    left_pipette.pick_up_tip()
    left_pipette.aspirate(300, palette['A2'])
    left_pipette.dispense(100, canvas['A6'])
    left_pipette.dispense(100, canvas['A7'])
    left_pipette.dispense(100, canvas['H1'])
    left_pipette.aspirate(100, palette['A2'])
    left_pipette.dispense(100, canvas['H12'])
    left_pipette.drop_tip()

    #blend_aquamarine

    left_pipette.transfer(
        [50, 25, 12],
        canvas['A1'],
        [canvas.wells_by_name()[well_name] for well_name in ['A2', 'A3', 'A4']])
    left_pipette.transfer(
        [50, 25, 12],
        canvas['A12'],
        [canvas.wells_by_name()[well_name] for well_name in ['A11', 'A10', 'A9']])
    left_pipette.transfer(
        [50, 25, 12],
        canvas['H6'],
        [canvas.wells_by_name()[well_name] for well_name in ['H5', 'H4', 'H3']])
    left_pipette.transfer(
        [50, 25, 12],
        canvas['H7'],
        [canvas.wells_by_name()[well_name] for well_name in ['H8', 'H9', 'H10']])

    left_pipette.transfer(
        [50, 25, 12],
        canvas['H1'],
        [canvas.wells_by_name()[well_name] for well_name in ['H2', 'H3', 'H4']])
    left_pipette.transfer(
        [50, 25, 12],
        canvas['H12'],
        [canvas.wells_by_name()[well_name] for well_name in ['H11', 'H10', 'H9']])
    left_pipette.transfer(
        [50, 25, 12],
        canvas['A6'],
        [canvas.wells_by_name()[well_name] for well_name in ['A5', 'A4', 'A3']])
    left_pipette.transfer(
        [50, 25, 12],
        canvas['A7'],
        [canvas.wells_by_name()[well_name] for well_name in ['A8', 'A9', 'A10']])
    
    left_pipette.pick_up_tip()
    left_pipette.mix(4, 98, canvas['A2'])
    left_pipette.mix(4, 98, canvas['A3'])
    left_pipette.mix(4, 98, canvas['A4'])
    left_pipette.mix(4, 98, canvas['A5'])
    left_pipette.mix(4, 98, canvas['A8'])
    left_pipette.mix(4, 98, canvas['A9'])
    left_pipette.mix(4, 98, canvas['A10'])
    left_pipette.mix(4, 98, canvas['A11'])
    left_pipette.mix(4, 98, canvas['H2'])
    left_pipette.mix(4, 98, canvas['H3'])
    left_pipette.mix(4, 98, canvas['H4'])
    left_pipette.mix(4, 98, canvas['H5'])
    left_pipette.mix(4, 98, canvas['H8'])
    left_pipette.mix(4, 98, canvas['H9'])
    left_pipette.mix(4, 98, canvas['H10'])
    left_pipette.mix(4, 98, canvas['H11'])
    left_pipette.drop_tip()

    #greentopup
    left_pipette.pick_up_tip()
    left_pipette.aspirate(261, palette['A1'])
    left_pipette.dispense(87, canvas['A1'])
    left_pipette.dispense(87, canvas['A12'])
    left_pipette.dispense(87, canvas['H6'])
    left_pipette.aspirate(87, palette['A1'])
    left_pipette.dispense(87, canvas['H7'])
    left_pipette.drop_tip()

    #bluetopup
    left_pipette.pick_up_tip()
    left_pipette.aspirate(261, palette['A2'])
    left_pipette.dispense(87, canvas['A6'])
    left_pipette.dispense(87, canvas['A7'])
    left_pipette.dispense(87, canvas['H1'])
    left_pipette.aspirate(87, palette['A2'])
    left_pipette.dispense(87, canvas['H12'])
    left_pipette.drop_tip()

    #BlendFireball
    #water/dilutant

    water_volumes = [
            0, 60, 45, 30, 30, 45, 60, 0,
            0, 50, 33, 25, 13, 33, 50, 0,
            0, 40, 30, 20, 20, 30, 40, 0,
            0, 30, 22, 15, 15, 22, 30, 0,
            0, 20, 15, 10, 10, 15, 20, 0,
            0, 15, 11, 7, 7, 11, 15, 0,
            0, 10, 8, 5, 5, 8, 10, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
          ]

    left_pipette.distribute(water_volumes, palette['A12'], canvas.wells())

    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['C8', 'C9', 'C10', 'C11']],
        canvas['C7'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['C8', 'C9', 'C10', 'C11']],
        canvas['C6'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['C8', 'C9', 'C10', 'C11']],
        canvas['C5'])
    left_pipette.mix(4, 40)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['C8', 'C9', 'C10', 'C11']],
        canvas['C4'])
    left_pipette.mix(4, 50)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['C8', 'C9', 'C10', 'C11']],
        canvas['C3'])
    left_pipette.mix(4, 60)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['C8', 'C9', 'C10', 'C11']],
        canvas['C2'])
    left_pipette.mix(4, 70)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['C8', 'C9', 'C10', 'C11']],
        canvas['C1'])
    left_pipette.mix(4, 80)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['F8', 'F9', 'F10', 'F11']],
        canvas['F7'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['F8', 'F9', 'F10', 'F11']],
        canvas['F6'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['F8', 'F9', 'F10', 'F11']],
        canvas['F5'])
    left_pipette.mix(4, 40)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['F8', 'F9', 'F10', 'F11']],
        canvas['F4'])
    left_pipette.mix(4, 50)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['F8', 'F9', 'F10', 'F11']],
        canvas['F3'])
    left_pipette.mix(4, 60)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['F8', 'F9', 'F10', 'F11']],
        canvas['F2'])
    left_pipette.mix(4, 70)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['F8', 'F9', 'F10', 'F11']],
        canvas['F1'])
    left_pipette.mix(4, 80)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['D8', 'D9', 'D10', 'D11']],
        canvas['D7'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['D8', 'D9', 'D10', 'D11']],
        canvas['D6'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['D8', 'D9', 'D10', 'D11']],
        canvas['D5'])
    left_pipette.mix(4, 40)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['D8', 'D9', 'D10', 'D11']],
        canvas['D4'])
    left_pipette.mix(4, 50)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['D8', 'D9', 'D10', 'D11']],
        canvas['D3'])
    left_pipette.mix(4, 60)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['D8', 'D9', 'D10', 'D11']],
        canvas['D2'])
    left_pipette.mix(4, 70)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['D8', 'D9', 'D10', 'D11']],
        canvas['D1'])
    left_pipette.mix(4, 80) 
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['E8', 'E9', 'E10', 'E11']],
        canvas['E7'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['E8', 'E9', 'E10', 'E11']],
        canvas['E6'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['E8', 'E9', 'E10', 'E11']],
        canvas['E5'])
    left_pipette.mix(4, 40)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['E8', 'E9', 'E10', 'E11']],
        canvas['E4'])
    left_pipette.mix(4, 50)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['E8', 'E9', 'E10', 'E11']],
        canvas['E3'])
    left_pipette.mix(4, 60)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['E8', 'E9', 'E10', 'E11']],
        canvas['E2'])
    left_pipette.mix(4, 70)
    left_pipette.consolidate(
        [10, 10, 10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['E8', 'E9', 'E10', 'E11']],
        canvas['E1'])
    left_pipette.mix(4, 80)

    left_pipette.consolidate(
        [10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['G8', 'G9']],
        canvas['G7'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['G8', 'G9']],
        canvas['G6'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['G8', 'G9']],
        canvas['G5'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['G8', 'G9']],
        canvas['G4'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['G8', 'G9']],
        canvas['G3'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['G8', 'G9']],
        canvas['G2'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['G8', 'G9']],
        canvas['G1'])
    left_pipette.mix(4, 30)

    left_pipette.consolidate(
        [10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['B8', 'B9']],
        canvas['B7'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['B8', 'B9']],
        canvas['B6'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['B8', 'B9']],
        canvas['B5'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['B8', 'B9']],
        canvas['B4'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['B8', 'B9']],
        canvas['B3'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['B8', 'B9']],
        canvas['B2'])
    left_pipette.mix(4, 30)
    left_pipette.consolidate(
        [10, 10],
        [canvas.wells_by_name()[well_name] for well_name in ['B8', 'B9']],
        canvas['B1'])
    left_pipette.mix(4, 30)

    #yellow_topup
    left_pipette.pick_up_tip()
    left_pipette.aspirate(280, palette['A4'])
    left_pipette.dispense(70, canvas['B9'])
    left_pipette.dispense(70, canvas['B8'])
    left_pipette.dispense(35, canvas['D9'])
    left_pipette.dispense(35, canvas['E9'])
    left_pipette.dispense(35, canvas['E10'])
    left_pipette.dispense(35, canvas['D10'])
    left_pipette.aspirate(140, palette['A4'])
    left_pipette.dispense(70, canvas['G9'])
    left_pipette.dispense(70, canvas['G8'])
    left_pipette.drop_tip()

    #orangestep1_topup
    left_pipette.pick_up_tip()
    left_pipette.aspirate(280, palette['A3'])
    left_pipette.dispense(70, canvas['C8'])
    left_pipette.dispense(70, canvas['C9'])
    left_pipette.dispense(70, canvas['C10'])
    left_pipette.dispense(70, canvas['C11'])
    left_pipette.aspirate(280, palette['A3'])
    left_pipette.dispense(70, canvas['F11'])
    left_pipette.dispense(70, canvas['F10'])
    left_pipette.dispense(70, canvas['F9'])
    left_pipette.dispense(70, canvas['F8'])
    left_pipette.aspirate(280, palette['A3'])
    left_pipette.dispense(70, canvas['D11'])
    left_pipette.dispense(70, canvas['E11'])
    left_pipette.dispense(70, canvas['E8'])
    left_pipette.dispense(70, canvas['D8'])

    left_pipette.aspirate(140, palette['A3'])
    left_pipette.dispense(35, canvas['D10'])
    left_pipette.dispense(35, canvas['E10'])
    left_pipette.dispense(35, canvas['E9'])
    left_pipette.dispense(35, canvas['D9'])

    left_pipette.mix(4, 90, canvas['E9'])
    left_pipette.mix(4, 90, canvas['D9'])
    left_pipette.mix(4, 90, canvas['D10'])
    left_pipette.mix(4, 90, canvas['E10'])
    left_pipette.drop_tip()

    #end


# In[ ]:




