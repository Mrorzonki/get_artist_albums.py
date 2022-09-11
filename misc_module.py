#imports
import re
import json

with open('setup.json','r') as setup_file: #load setup file
    setup = json.load(setup_file)

#setup functions
def get_credentials(): #return spotipy api credetianls 
    return setup['credentials']

def set_credentials(client_id, client_secret): #save credentials to setup.json
    setup['credentials']['client_id'] = client_id
    setup['credentials']['client_secret'] = client_secret
    with open('setup.json','w') as setup_file:
        setup_file.write(json.dumps(obj=setup, indent=2))

#helper functions
def get_snake_case(str):
    str = str.lower()
    str = re.sub('\s', '_', str)
    return str

def rmv_file_extension(pathname):
    return re.sub('[.]\w*$', '', pathname)