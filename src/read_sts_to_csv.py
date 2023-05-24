# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:50:00 2022

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

main_df = pd.DataFrame()

for k, sts_file in enumerate([sts_file_list[0]]):
    print('Reading file no: {}'.format(k))
    
    with open(sts_file, 'r') as f:
        lines = f.readlines()
        start_line = 0
        for i, line in enumerate(lines):
            if 'Name                             	Connection Level' in line:
                start_line = i
        
        data = lines[start_line:-1]
        columns = data[0].replace(' ', '').split('\t')[:-1]
    
    df = pd.DataFrame(columns=columns)

    for line in tqdm(data[1:]):
            row = line.replace(' ', '').split('\t')[:-1]
            
            # if row[1] != '1':
            #     continue
            
            row[0] = row[0].split('::')[-1]
            
            df.loc[len(df)] = row
    
    df['realization'] = k + 1
    
    main_df = pd.concat([main_df,df], axis = 0)
    
main_df.to_csv(r'wall_scale_all_blocks.csv')
            
        
        
        
        