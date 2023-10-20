# -*- coding: utf-8 -*-

"""
Created on Sat Sep 30 02:17:21 2023

@author: R Haynes

filename: inputs.py
"""

# variables

# paths to the json files to be processed

json_files = [
    
    'SampleElectric2AccountDetails.json',
    
    'SampleElectricAccountDetails.json',
    
    'SampleGasAccountDetails.json',
    
    'SampleWaterAccountDetails.json'
    
]

# path to the spreadsheet to be written to

xl_spreadsheet_file = "EntryTemplate_General.xlsx"

# these are the names of the dataframe columns that are needed

dataframe_columns = [
    
    '_embedded.accounts.accountNumber',
    
    '_embedded.accounts.statementDate',
    
    '_embedded.accounts.dueDate',
    
    '_embedded.accounts.totalCharges',
    
    '_embedded.accounts.meterData.meterNumber',
    
    '_embedded.accounts.meterData.meterReadDate',
    
    '_embedded.accounts.meterData.usages.meterReadingRaw',
    
    '_embedded.accounts.newCharges'
    
]

# argument for json_normalize() function

record_path_info = ['_embedded','accounts','meterData','usages']

# argument for json_normalize() function

meta_info = [
                ['_embedded','accounts','meterData','meterNumber'],
                
                ['_embedded','accounts','meterData','meterReadDate'],
                
                ['_embedded','accounts','accountNumber'],
                
                ['_embedded','accounts','dueDate'],
                
                ['_embedded','accounts','totalCharges'],
                
                ['_embedded','accounts','newCharges'],
                
                ['_embedded','accounts','statementDate']
                
            ]

# argument for json_normalize() function

record_prefix_info = '_embedded.accounts.meterData.usages.'

# argument for json_normalize() function

errors_info = 'ignore'

# this var lists the dropped columns before setting the record_prefix='_embedded.accounts.meterData.usages.'

# not used but I'm keeping it here in case the 'record_prefix' is not used or changed.

dropped_columns_no_record_prefix = [
    
    'calorificValue',
    
    'citedUsage',
    
    'contributionStatus',
    
    'createdDate',
    
    'hoursOfUse',
    
    'loadFactor',
    
    'loadType',
    
    'measuredUsage',
    
    'measurementType',
    
    'meterConstantMultiplier',
    
    'meterConversionMultiplier',
    
    'meterReadDate',
    
    'meterReadType',
    
    'meterReadingDelta',
    
    'meterReadingDeltaPrevious',
    
    'meterReadingDeltaUsageUnit',
    
    'meterReadingRawPrevious',
    
    'numberOfDaysInPeriod',
    
    'outageBlock',
    
    'periodStart',
    
    'periodEnd',
    
    'powerFactor',
    
    'pressureMultiplier',
    
    'prevReadDate',
    
    'previousMeterReadType',
    
    'previousReadTypeAsPrinted',
    
    'previousUsage',
    
    'rateOrTariffActualName',
    
    'readTypeAsPrinted',
    
    'readingSchedule',
    
    'tariffRateComponents',
    
    'usageActualName',
    
    'usageUnit',
    
    'prorationStatus'
]

# this var lists the dropped columns using the record_prefix='_embedded.accounts.meterData.usages.'

dropped_columns_with_record_prefix = [
    
    '_embedded.accounts.meterData.usages.calorificValue',
    
    '_embedded.accounts.meterData.usages.citedUsage',
    
    '_embedded.accounts.meterData.usages.contributionStatus',
    
    '_embedded.accounts.meterData.usages.createdDate',
    
    '_embedded.accounts.meterData.usages.hoursOfUse',
    
    '_embedded.accounts.meterData.usages.loadFactor',
    
    '_embedded.accounts.meterData.usages.loadType',
    
    '_embedded.accounts.meterData.usages.measuredUsage',
    
    '_embedded.accounts.meterData.usages.measurementType',
    
    '_embedded.accounts.meterData.usages.meterConstantMultiplier',
    
    '_embedded.accounts.meterData.usages.meterConversionMultiplier',
    
    '_embedded.accounts.meterData.usages.meterReadDate',

    '_embedded.accounts.meterData.usages.meterReadType',
    
    '_embedded.accounts.meterData.usages.meterReadingDelta',
    
    '_embedded.accounts.meterData.usages.meterReadingDeltaPrevious',
    
    '_embedded.accounts.meterData.usages.meterReadingDeltaUsageUnit',
    
    '_embedded.accounts.meterData.usages.meterReadingRawPrevious',
    
    '_embedded.accounts.meterData.usages.numberOfDaysInPeriod',
    
    '_embedded.accounts.meterData.usages.outageBlock',
    
    '_embedded.accounts.meterData.usages.periodStart',
    
    '_embedded.accounts.meterData.usages.periodEnd',
    
    '_embedded.accounts.meterData.usages.powerFactor',
    
    '_embedded.accounts.meterData.usages.pressureMultiplier',
    
    '_embedded.accounts.meterData.usages.prevReadDate',
    
    '_embedded.accounts.meterData.usages.previousMeterReadType',
    
    '_embedded.accounts.meterData.usages.previousReadTypeAsPrinted',
    
    '_embedded.accounts.meterData.usages.previousUsage',
    
    '_embedded.accounts.meterData.usages.rateOrTariffActualName',
    
    '_embedded.accounts.meterData.usages.readTypeAsPrinted',
    
    '_embedded.accounts.meterData.usages.readingSchedule',
    
    '_embedded.accounts.meterData.usages.tariffRateComponents',
    
    '_embedded.accounts.meterData.usages.usageActualName',
    
    '_embedded.accounts.meterData.usages.usageUnit',
    
    '_embedded.accounts.meterData.usages.prorationStatus'
    
]










# EOF