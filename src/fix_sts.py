# -*- coding: utf-8 -*-
"""
Created on Tue May 16 07:43:02 2023

@author: gld_yfogel
"""

import os
import glob
import numpy as np

from tqdm import tqdm

csv_path = r'V:\RTKC\Bingham Canyon\CX21495304_NPB_FS\FS2400_Method_Calibrations\Wall_Scale\FM_HeatMap\02_Filtered_Stats'

csv_file_list = glob.glob(csv_path + '\*.csv')

for csv_file in tqdm(csv_file_list):
    with open(csv_file, 'r') as csvf:
        lines = csvf.readlines()
        
        all_lengths = []
        for line in lines:
            all_lengths.append(len(line.split(',')))
        
        all_lengths = np.asarray(all_lengths)
        if np.all(all_lengths == all_lengths[0]):
            continue
        
        loc_list = []
        for i, line in enumerate(lines):
            split_line = line.split(',')
            short_line = split_line[:5]
            short_line.append('\n')
            line = ','.join(short_line)
            
            lines[i] = line
        
    with open(csv_file, "w") as ncsvf:
        for line in lines:
            ncsvf.write(line)
    
print('Done')