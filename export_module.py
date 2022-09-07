import pandas as pd
import json

def export_to_jason(json_data, pathname):
    file = open(file=pathname,mode='w')
    file.write(json.dumps(obj=json_data,indent=2))
    file.close()