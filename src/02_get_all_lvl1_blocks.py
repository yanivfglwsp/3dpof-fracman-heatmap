# -*- coding: utf-8 -*-
"""
Created on Mon May 15 10:40:39 2023

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
    return int(real.split('_')[-1])

output_path = r'V:\RTKC\Bingham Canyon\CX21495304_NPB_FS\FS2400_Method_Calibrations\Wall_Scale\FM_HeatMap/08_Python/OUTPUT'
if not os.path.exists(output_path):
    os.makedirs(output_path)

real_file_path = r'V:\RTKC\Bingham Canyon\CX21495304_NPB_FS\FS2300_Model_Build\08_WallScale\Run3_KUC_QS\Post-Processing\05_Blocks'
dir_list = os.listdir(real_file_path)

#get rid of first elemnet which is .hub
dir_list = dir_list[1:]

dir_list.sort(key=get_sn)

all_block_df = pd.read_csv(r'V:\RTKC\Bingham Canyon\CX21495304_NPB_FS\FS2400_Method_Calibrations\Wall_Scale\FM_HeatMap\08_Python/wall_scale_all_blocks.csv',  index_col=0)

for real in tqdm(dir_list):
    
    j = get_sn(real)
    real_results_path = os.path.join(output_path, 'Realization_{}'.format(j))
    if not os.path.exists(real_results_path):
        os.makedirs(real_results_path)
    
    block_list = glob.glob(os.path.join(real_file_path, real) + '\*.ts')
    
    strip_block_list = [block.split('\\')[-1].replace('.ts','') for block in block_list]
    
    df1 = pd.DataFrame()
    df1['lvl1_blocks'] = strip_block_list
    df1_csv_path = os.path.join(real_results_path,'real_{}_lvl1_blocks.csv'.format(j))
    df1.to_csv(df1_csv_path,index = False)
    
    total_number_of_blocks = int(all_block_df['total_blocks'][all_block_df['real'] == 'realization_{}'.format(j)])
    all_blocks_list = ['Block__{}'.format(bid) for bid in range(1,total_number_of_blocks + 1)]
    
    df2 = pd.DataFrame()
    df2['all_blocks'] = all_blocks_list
    df2_csv_path = os.path.join(real_results_path,'real_{}_all_blocks.csv'.format(j))
    df2.to_csv(df2_csv_path,index = False)
    
    blocks_to_delete = [x for x in all_blocks_list if x not in strip_block_list]
    df3 = pd.DataFrame()
    df3['blocks_to_delete'] = blocks_to_delete
    df3_csv_path = os.path.join(real_results_path,'real_{}_blocks_to_delete.csv'.format(j))
    df3.to_csv(df3_csv_path,index = False)