# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:12:47 2022

@author: stefa
"""
import os
from pyhamilton import (HamiltonInterface,  LayoutManager, 
 Plate96, Tip96, initialize, tip_pick_up, tip_eject, 
 aspirate, dispense,  oemerr, resource_list_with_prefix, normal_logging,
 ph_controller_initialize, ph_controller_parameters, ph_controller_calibrate,
 ph_controller_pickup, ph_controller_park, ph_controller_measure_cycle,
 ph_controller_wash, ph_controller_dry, layout_item, ph_controller_loadconfig,
 ph_controller_saveconfig)


lmgr = LayoutManager('deck.lay')

measurement_plate = layout_item(lmgr, Plate96, 'Cos_96_Rd_0001')
measurement_pos = [(measurement_plate, 0)]

if __name__ == '__main__': 
    with HamiltonInterface(simulate=True) as ham_int:
        normal_logging(ham_int, os.getcwd())
        initialize(ham_int)
        
        module_id = ph_controller_initialize(ham_int, 1)
        
        ph_controller_parameters(ham_int, module_id, 'seqCOREGripTool', 'seqWash_Module',
                                 'seqDryer_Module', 8, 1, 1, 1)
        
        ph_controller_calibrate(ham_int, module_id, seq_module = 'seqpH_Module_0001', seq_solution_1 = 'seqCalibration_1',
                                 seq_solution_2 = 'seqCalibration_2', seq_reference = 'seqVerify',
                                 measure_time = 3, calibration_time = 3, measure_height = 2.0, pH_solution_1 = 7.0, 
                                 pH_solution_2 = 8.0, pH_reference = 7.5, temp_solution_1 = 35.0, temp_solution_2 = 35.0, 
                                 temp_solution_ref = 36.0, calibrate_dynamically = False)
        
        ph_controller_pickup(ham_int, module_id, seq_module = 'seqpH_Module_0001')
        
        pH_values = ph_controller_measure_cycle(ham_int, module_id, measurement_pos, 1.0, '1111', 3, 37.0)
        print(pH_values)
        
        ph_controller_wash(ham_int, module_id)
        
        ph_controller_dry(ham_int, module_id)
        
        ph_controller_park(ham_int, module_id, seq_module = 'seqpH_Module_0001')
        
        ph_controller_saveconfig(ham_int, bluetooth_port = 1, num_wash_cycles = 1, num_dry_cycles = 1, dry_time = 1)
        
        res = ph_controller_loadconfig(ham_int)
