#imports
import pandas as pd
import json
from sys import exit
from os.path import exists

#messages
error_file_exists = 'ERROR: file with same pathname allready exists.'

#export functions

def write_to_jason(json_data, pathname, overwrite = False):
    if(overwrite is False and exists(pathname)): exit(error_file_exists) #if file allready exists, exit with error message

    file = open(file=pathname,mode='w')
    file.write(json.dumps(obj=json_data,indent=2))
    file.close()

def write_to_csv(json_data, pathname, overwrite = False):
    if(overwrite is False and exists(pathname)): exit(error_file_exists) #if file allready exists, exit with error message

    df = pd.DataFrame(json_data)
    df.to_csv(path_or_buf=pathname,index=False,header=False,mode='w')

def write_to_excel(json_data, pathname, overwrite = False): #write to excel file with .xlsx format
    if(overwrite is False and exists(pathname)): exit(error_file_exists) #if file allready exists, exit with error message

    df = pd.DataFrame(json_data)
    df.to_excel(excel_writer=pathname,index=False,header=False)

def write_to_raw(json_data): #RAW / print to consloe
    for item in json_data:
        print('"'+item+'"')