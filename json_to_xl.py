# -*- coding: utf-8 -*-

"""
Created on Sat Sep 30 02:36:44 2023

@author: R Haynes

filename: json_to_xl.py
"""

# NOTE: Please be advised that this script only extracts and prints to the 
		
# spreadsheet the 8 minimum columns needed to make an entry on the system.

# If more data columns are desired, additional modifications to this script

# will be needed.

# imports

import inputs as ip

import functions as fn

#import pandas as pd

import openpyxl as xl

###

# not strictly needed. just setting some options for printing out dataframe on command line.

#pd.set_option('display.max_columns', None)

#pd.set_option('display.max_rows', None)

#pd.set_option('display.max_colwidth', None)

#pd.set_option('display.width', 10000)

###

# open XL spreadsheet file

workbook = xl.load_workbook(ip.xl_spreadsheet_file)

# grab the active worksheet

sheet = workbook.active

###

######

for item in ip.json_files:

    # open the next needed json file
    
    data = fn.open_json_file(item)

    # convert data into a dataframe
    
    df = fn.convert_data_to_dataframe(
        
        data,
        
        ip.record_path_info,
        
        ip.meta_info,
        
        ip.record_prefix_info,
        
        ip.errors_info,
        
        ip.dropped_columns_with_record_prefix,
        
        ip.dataframe_columns
        
        )
    
    # append data to spreadsheet
    
    fn.append_to_spreadsheet(df, sheet)

######

# save spreadsheet and close

workbook.save(filename=ip.xl_spreadsheet_file)

workbook.close()

###

#print(df)

































# EOF