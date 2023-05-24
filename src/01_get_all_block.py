# -*- coding: utf-8 -*-
"""
Created on Mon May 15 10:17:22 2023

@author: gld_yfogel
"""

import os
import pandas as pd
import glob
from tqdm import tqdm

def get_sn(real):
    '''
    get realization number from str in the from of 'Stats_rea-xx.sts'
    '''
    return int(real.split('.')[0].split('-')[-1])


sts_files_directory = r'V:\RTKC\Bingham Canyon\CX21495304_NPB_FS\FS2300_Model_Build\08_WallScale\Run3_KUC_QS\Post-Processing\04_Stats'
dir_list = os.listdir(sts_files_directory)
sts_file_list = []

for dirc in dir_list:
    if '.sts' not in dirc:
        continue
    
    sts_file_list.append(os.path.join(sts_files_directory,dirc))

# sort sts list by realization number
sts_file_list.sort(key=get_sn)

main_df = pd.DataFrame(columns = ['real', 'total_blocks'])

for k, sts_file in enumerate(tqdm(sts_file_list)):
    
    with open(sts_file, 'r') as f:
        lines = f.readlines()
        # get the total number of blocks in the realizations
        # 1. strip whitespaces from string
        # 2. split at ('\t')
        # 3. get last element and convert to integer
        total_nm_blocks = int(lines[2].strip().split('\t')[-1])
        
        row = ['realization_{}'.format(k+1), total_nm_blocks]
         
        main_df.loc[len(main_df)] = row

main_df.to_csv('wall_scale_all_blocks.csv')
    
   