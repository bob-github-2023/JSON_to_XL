# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 00:34:58 2023

@author: R Haynes

filename: functions.py
"""

import json

import pandas as pd

# open the needed json files:
def open_json_file(json_file):
    '''JSON file opening function.
    
    This function opens the JSON file to be processed and returns the data
    in python form.
    '''
    with open(json_file) as file:
        data = json.load(file)
        
    return data

###

# normalize json
def convert_data_to_dataframe(
    data, record_path_arg, meta_arg, record_prefix_arg, errors_arg, dropped_columns, dataframe_columns
):
    '''JSON file convert to normalized pandas dataframe function.
    
    This function opens the data and converts it to a normalized JSON dataframe. Note that I am only using the minimum eight 
    essential data columns to eventually write to the XL spreadsheet. If we need more data columns written to the spreadsheet, 
    further discussion may be needed.
    '''
    # normalize json
    dataframe = pd.json_normalize(data, record_path=record_path_arg, 
                           meta=meta_arg,
                           record_prefix=record_prefix_arg,
                           errors=errors_arg
                          )

    # drop unneeded columns from dataframe
    dataframe = dataframe.drop(dropped_columns, axis=1)

    # sort the columns into a more desirable order
    dataframe = dataframe.reindex(columns=dataframe_columns)
    
    return dataframe

###

# append data to spreadsheet
def append_to_spreadsheet(dataframe, spreadsheet):
    '''Append data to current spreadsheet row function.
    
    This function gets data from the dataframe and appends it to the current spreadsheet row.
    '''
    # print a blank spreadsheet row before printing data rows
    current_spreadsheet_row = ['','','','']
    spreadsheet.append(current_spreadsheet_row)

    # iterate through dataframe rows, build current spreadsheet row and append to spreadsheet
    # yes, iterrows() is, I think, the slowest way to do this, but that's what I started with and need to get it finished.
    # next time, I'll try something faster...
    for index, rows in dataframe.iterrows():

        # clear the list
        current_spreadsheet_row = []

        # build the list for the current spreadsheet row
        current_spreadsheet_row = [
            '', # column A (blank)
            rows['_embedded.accounts.accountNumber'], # column B
            rows['_embedded.accounts.statementDate'], # column C
            rows['_embedded.accounts.dueDate'], # column D
            rows['_embedded.accounts.totalCharges'], # column E
            '', # column F (blank)
            '', # column G (blank)
            '', # column H (blank)
            '', # column I (blank)
            rows['_embedded.accounts.meterData.meterNumber'], # column J
            '', # column K (blank)
            rows['_embedded.accounts.meterData.meterReadDate'], # column L
            '', # column M (blank)
            rows['_embedded.accounts.meterData.usages.meterReadingRaw'], # column N
            '', # column O (blank)
            '', # column P (blank)
            '', # column Q (blank)
            rows['_embedded.accounts.newCharges'] # column R
        ]

        # append current row to spreadsheet
        spreadsheet.append(current_spreadsheet_row)



















































# EOF