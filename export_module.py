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