# -*- coding: utf-8 -*-
"""
Created on Mon May 15 11:43:43 2023

@author: gld_yfogel
"""

import os
import pandas as pd
import sys
from tqdm import tqdm

from fracman_macros import add_blocks_to_file


number_of_realizations = 100
result_path = r'V:\RTKC\Bingham Canyon\CX21495304_NPB_FS\FS2400_Method_Calibrations\Wall_Scale\RUN_4\02_Output_Files\12_Recompiled_Results\03_Final_CSV\Run_4_BaseCase'
result_file = 'Run_4_BaseCase_3DPOF_Results.csv'

fracman_csv_file = r'V:\RTKC\Bingham Canyon\CX21495304_NPB_FS\FS2400_Method_Calibrations\Wall_Scale\FM_HeatMap\02_Filtered_Stats\realization_{}.csv'

case_dir = 'Run_4_BaseCase'

output_path = r'V:\RTKC\Bingham Canyon\CX21495304_NPB_FS\FS2400_Method_Calibrations\Wall_Scale\FM_HeatMap\05_Macros\{}\Initial_Blocks_Delete'.format(case_dir)



print('Reading 3DPOF data...')
df = pd.read_csv(os.path.join(result_path,result_file))
print('Done.')

case_num = 0
df_data = df[df['Sensitivity Scenario Id'] == case_num]
 
print('Generating Macros...')
print('   Initial Blocks')
for real in tqdm(list(range(1,number_of_realizations + 1))):
    
    # get all blocks from 3DPOF
    block_data = df_data[(df_data['Realization'] == 'realization_{}'.format(real))]
    initial_blocks = list(block_data['Block Id'])
    
    # get FracMan blocks
    fracman_blocks = pd.read_csv(fracman_csv_file.format(real))
    
    # get rid of rows where the "Name   " element is Non
    fracman_blocks = fracman_blocks[fracman_blocks['Name                            '].notna()]
    
    fracman_blocks_list = list(fracman_blocks['Name                            '].apply(lambda x: x.split('::')[-1]))
    
    # check if framan block list is shorter than 3dpof list
    if len(fracman_blocks_list) < len(initial_blocks):
        print('Error. The number of FracMan blocks is smaller than 3DPOF count')
        print('Error occourd in Realization: {}'.format(real))
        sys.exit(1)
    
    # take out blocks from fracman list that were filtered in the 3DPOF
    blocks_to_delete = [x for x in fracman_blocks_list if x not in initial_blocks] 
    
    # create macro
    macro_file_name  = 'real_{}_delete_initial_blocks.fmf'.format(real)
    macro_file_path = os.path.join(output_path, macro_file_name)
    
    with open(macro_file_path, 'w') as ofh:
        ofh.write(add_blocks_to_file(blocks_to_delete))




print('   Only Stable Blocks')
for real in tqdm(list(range(1,number_of_realizations + 1))):
    
    case_num = 0 # Base Case only = 0
    df_data = df[df['Sensitivity Scenario Id'] == case_num]
    
    # get all stable blocks from 3DPOF
    block_data = df_data[(df_data['Realization'] == 'realization_{}'.format(real))]
    stable_blocks = list(block_data[block_data['FOS'] >= 1]['Block Id'])
    
    output_path = r'V:\RTKC\Bingham Canyon\CX21495304_NPB_FS\FS2400_Method_Calibrations\Wall_Scale\FM_HeatMap\05_Macros\{}\BaseCase_Blocks'.format(case_dir)
    macro_file_name  = 'real_{}_delete_blocks.fmf'.format(real)
    macro_file_path = os.path.join(output_path, macro_file_name)
    
    with open(macro_file_path, 'w') as ofh:
        ofh.write(add_blocks_to_file(stable_blocks))
        
print('Done.')