#imports
import re

#helper functions

def get_snake_case(str):
    str = str.lower()
    str = re.sub('\s', '_', str)
    return str

def rmv_file_extension(pathname):
    return re.sub('[.]\w*$', '', pathname)