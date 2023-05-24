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
    return int(real.split('\\')[-1].split('.')[0].split('-')[-1])


sts_files_directory = r'V:\RTKC\Bingham Canyon\31405526.002 - EW Extension\02_Output_Files\05_Block_Files\016d-ewextension-double\TREND-180_IRA-45'
dir_list = os.listdir(sts_files_directory)
sts_file_list = []

print('Get .sts file list...')
for dirc in tqdm(dir_list):
    if os.path.isdir(os.path.join(sts_files_directory,dirc)):
        sts_file = glob.glob(os.path.join(sts_files_directory,dirc) + '\*.sts')
    # if '.sts' not in dirc:
    #     continue
    
        sts_file_list.append(sts_file[-1])

print('Found {} .sts files'.format(len(sts_file_list)))

# sort sts list by realization number
sts_file_list.sort(key=get_sn)
print('Done \n')

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

output_path = r'C:/Projects/DRAFT_OUTPUT/Fortuna'
if not os.path.exists(output_path):
    os.makedirs(output_path)

main_df.to_csv(os.path.join(output_path,'fortuna_all_blocks.csv'))
    
   