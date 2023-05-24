# -*- coding: utf-8 -*-
"""
Created on Tue May 16 17:59:47 2023

@author: gld_yfogel
"""

import os
import pandas as pd

from tqdm import tqdm

def int_func(x):
    if x > 0:
        return 1
    else:
        return 0

real_num = 100

# '''
# Merge results for Run_4_Sensitivity case
# '''

# grid_dir_loc = r'V:\RTKC\Bingham Canyon\CX21495304_NPB_FS\FS2400_Method_Calibrations\Wall_Scale\FM_HeatMap\07_Heat_Map'
# run_dir = 'Run_4_Sens'
# case_dir = 'Results_Grid_25ft'
# grid_csv_name = 'Grid_Real_{}.csv'
# empty_grid_file = 'Empty_Grid_file_25ft.csv'

# intersection_dir = 'Results_Grid_25ft_intersections'

# main_grid_df = pd.read_csv(os.path.join(grid_dir_loc,run_dir,empty_grid_file))

# for real in tqdm(list(range(1,real_num + 1))):
#     df = pd.read_csv(os.path.join(grid_dir_loc,
#                                   run_dir,
#                                   case_dir,
#                                   grid_csv_name.format(real)))
    
#     df['01_all_blocks'] = df['01_all_blocks'].apply(lambda x: int_func(x))
#     df['02_Dry'] = df['02_Dry'].apply(lambda x: int_func(x))
#     df['03_Ru_0.1'] = df['03_Ru_0.1'].apply(lambda x: int_func(x))
#     df['04_Ru_0.2'] = df['04_Ru_0.2'].apply(lambda x: int_func(x))
#     df['05_Ru_0.3'] = df['05_Ru_0.3'].apply(lambda x: int_func(x))
#     df['06_Ru_0.4'] = df['06_Ru_0.4'].apply(lambda x: int_func(x))

#     intersection_grid_name = grid_csv_name.format(real).replace('.csv','_intersection.csv')
    
#     df.to_csv(os.path.join(grid_dir_loc,run_dir,intersection_dir,intersection_grid_name))
    
#     main_grid_df['01_all_blocks'] += df['01_all_blocks']
#     main_grid_df['02_Dry'] += df['02_Dry']
#     main_grid_df['03_Ru_0.1'] += df['03_Ru_0.1']
#     main_grid_df['04_Ru_0.2'] += df['04_Ru_0.2']
#     main_grid_df['05_Ru_0.3'] += df['05_Ru_0.3']
#     main_grid_df['06_Ru_0.4'] += df['06_Ru_0.4']
    
# merged_grid_name = 'Run_4_Sens_grid_25ft_{}_realizations_intersections.csv'.format(real_num)
# main_grid_df.to_csv(os.path.join(grid_dir_loc,run_dir,merged_grid_name))


'''
Merge results for Run_4_BaseCase case
'''

grid_dir_loc = r'V:\RTKC\Bingham Canyon\CX21495304_NPB_FS\FS2400_Method_Calibrations\Wall_Scale\FM_HeatMap\07_Heat_Map'
run_dir = 'Run_4_BaseCase'
case_dir = 'Results_Grid_25ft'
grid_csv_name = 'Grid_Real_{}.csv'
empty_grid_file = 'Empty_Grid_file_25ft.csv'

intersection_dir = 'Results_Grid_25ft_intersections'

main_grid_df = pd.read_csv(os.path.join(grid_dir_loc,run_dir,empty_grid_file))

for real in tqdm(list(range(1,real_num + 1))):
    df = pd.read_csv(os.path.join(grid_dir_loc,
                                  run_dir,
                                  case_dir,
                                  grid_csv_name.format(real)))
    
    df['01_all_blocks'] = df['01_all_blocks'].apply(lambda x: int_func(x))
    df['02_rep_ru'] = df['02_rep_ru'].apply(lambda x: int_func(x))
    
    intersection_grid_name = grid_csv_name.format(real).replace('.csv','_intersection.csv')
    
    df.to_csv(os.path.join(grid_dir_loc,run_dir,intersection_dir,intersection_grid_name))
    
    main_grid_df['01_all_blocks'] += df['01_all_blocks']
    main_grid_df['02_rep_ru'] += df['02_rep_ru']
    
merged_grid_name = 'Run_4_BaseCase_grid_25ft_{}_realizations_intersections.csv'.format(real_num)
main_grid_df.to_csv(os.path.join(grid_dir_loc,run_dir,merged_grid_name))
