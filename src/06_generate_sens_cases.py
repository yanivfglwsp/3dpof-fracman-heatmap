# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:54:03 2023

@author: gld_yfogel
"""

import os
import pandas as pd

from tqdm import tqdm

input_directory = r'V:\RTKC\Bingham Canyon\CX21495304_NPB_FS\FS2400_Method_Calibrations\Wall_Scale\RUN_4\02_Output_Files\08_Updated_data\024-WallScale-Run_4_failure' 
file_name = '024-WallScale-Run_4_failure_Updated_Composite_Results.csv'
csv_file = os.path.join(input_directory,file_name)

output_directory = r'V:\RTKC\Bingham Canyon\CX21495304_NPB_FS\FS2400_Method_Calibrations\Wall_Scale\RUN_4\02_Output_Files\12_Recompiled_Results'
output_csv = os.path.join(output_directory,'01_CSV')

sector_num = 48

# '''
# Load main results file
# '''
# df = pd.read_csv(csv_file)

# '''
# split result file into sector .csv files
# '''
# sector_num_list = tqdm(list(range(1,48+1)))
# for sector in sector_num_list:
#     temp_df = df[df['Section'] == 'sector_{}'.format(sector)]
#     temp_df = temp_df.reset_index()
#     temp_df.index += 1
    
#     csv_file_name = file_name.split('-')[-1].replace('.csv','-Sector_{}.csv'.format(sector))
#     temp_df.to_csv(os.path.join(output_csv,csv_file_name),
#                    index = False)

'''
load BaseCase scenario .csv file
'''
baseCase_file = r'V:\RTKC\Bingham Canyon\CX21495304_NPB_FS\FS2400_Method_Calibrations\Wall_Scale\RUN_4\02_Output_Files\12_Recompiled_Results\Run_4_failure_Sensitivitiy_Scenarios_all_sectors.csv'

baseCase_df = pd.read_csv(baseCase_file)

print('Loading Base Case scenario and generating updated sector .csv files...')

for sector in tqdm(list(range(1,sector_num+1))):
    scenario_id_list = baseCase_df['sector_{}'.format(sector)]
    bc_scenario_id_list = baseCase_df['scenario']
    
    sector_file_name = 'Run_4_failure_Updated_Composite_Results-Sector_{}.csv'.format(sector)
    sector_file_path = os.path.join(output_csv, sector_file_name)
    
    sector_df = pd.read_csv(sector_file_path, index_col = 0)
    
    bc_sector_df = pd.DataFrame()
    
    for scenario_id, bc_scenario_id in zip(scenario_id_list, bc_scenario_id_list):
        df1 = sector_df[sector_df['Scenario Id'] == scenario_id].copy()
        df1['Sensitivity Scenario Id'] =  bc_scenario_id
        
        bc_sector_df = pd.concat([bc_sector_df,df1])
        
    bc_sector_df = bc_sector_df.reset_index()
    bc_sector_df.index += 1
    
    update_sector_file_path = os.path.join(output_directory,'02_Update_CSV', 'Run_4_Sensitivity')
    update_sector_file_name = 'Sector_{}_UPDATE.csv'
    bc_sector_df.to_csv(os.path.join(update_sector_file_path, update_sector_file_name.format(sector)),
                        index = False)
    
print('Done')
    
'''
Complie all base case .csv file to one big file
'''

update_all_sector_csv_path = os.path.join(output_directory,'03_Final_CSV','Run_4_Sensitivity')
update_all_sector_csv_name = 'Run_4_Sensitivity_3DPOF_Results.csv'

final_df = pd.DataFrame()

print('Generating final .csv result file...')
for sector in tqdm(list(range(1,sector_num+1))):
    temp_df = pd.read_csv(os.path.join(update_sector_file_path, update_sector_file_name.format(sector)),
                          index_col = 0)
    
    final_df = pd.concat([final_df,temp_df])
final_df.rename(columns = {'index': 'og_index', 'Scenario Id': 'og_scenario_id'})
final_df = final_df.reset_index()
final_df.index += 1

final_df.to_csv(os.path.join(update_all_sector_csv_path,update_all_sector_csv_name))
print('Done.')