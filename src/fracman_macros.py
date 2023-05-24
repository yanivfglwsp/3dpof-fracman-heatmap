# -*- coding: utf-8 -*-
"""
Created on Mon May 15 08:29:41 2023

@author: gld_yfogel
"""

import os
import pandas

def add_blocks_to_file (block_list):
    
    '''
    The following function creates a FracMan macro that is set to delete the
    block listed in it.
    Example:
    
    
BEGIN BlockSetStoreInternal
	Object = "NW_WedgeAnalysis:Blocks_1_subset_1"
	StoreInternal = 0
END

BEGIN DeleteObjects
 	Name = "Block__1"
 	Name = "Block__24"
 	Name = "Block__47"
 	Name = "Block__70"
END
    
    '''
    
    macro_str = '''

BEGIN BlockSetStoreInternal
	Object = "NW_WedgeAnalysis:Blocks_1_subset_1"
	StoreInternal = 0
END

BEGIN DeleteObjects
'''
    for block in block_list:
        block_id = block.split('__')[-1]
        macro_str += '''	Name = "Block__{bid}"
'''.format(bid = block_id)

    macro_str += '''END

'''
    return macro_str

if __name__ == "__main__":
    
    test_block_list = ['B__1', 'B__34', 'B__401', 'B__5000']
    
    output_path = r'C:/Projects/DRAFT_OUTPUT'
    macro_file_name  = 'test_macro.fmf'
    
    macro_file_path = os.path.join(output_path, macro_file_name)
    
    with open(macro_file_path, 'w') as ofh:
        ofh.write(add_blocks_to_file(test_block_list))
        
    

