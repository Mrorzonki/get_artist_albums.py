from wsgiref import headers
import pandas as pd
import json

def write_to_jason(json_data, pathname):
    file = open(file=pathname,mode='w')
    file.write(json.dumps(obj=json_data,indent=2))
    file.close()

def write_to_csv(json_data, pathname):
    df = pd.DataFrame(json_data)
    df.to_csv(path_or_buf=pathname,index=False,header=False,mode='w')

def write_to_excel(json_data, pathname): #write to file with xlsx excel format
    df = pd.DataFrame(json_data)
    df.to_excel(excel_writer=pathname,index=False,header=False)

def write_to_raw(json_data): #RAW / print to consloe
    for item in json_data:
        print('"'+item+'"')