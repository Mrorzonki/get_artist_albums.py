#module imports
import credentials as cred
import spotipy_module as spm

#other imports
import sys
import json

def main(artist_name='Casting Crowns', export_type='raw', export_pathname='C:/Users/X/Desktop/out'):
    auth_sp = spm.get_authentication(cred.client_id, cred.client_secret) 
    
    artist = spm.get_artist_by_name(auth_sp, artist_name)
    albums = spm.get_albums_by_artist(auth_sp, artist['id'])

    if(export_type=='csv'): print('Export mode = csv')
    elif(export_type=='excel'): print('Export mode = excel')
    elif(export_type=='json'): print('Export mode = json')
    else: print('Export mode = raw')

if __name__ == '__main__':
    argv = sys.argv

    #TODO: parmeters validation
    if(len(argv) < 2 or 3 < len(argv)):  sys.exit("ERROR: invalid parameters count") #script requires 2 to 3 parameters
       
    artist_name=argv[1]
    export_type=argv[2].lower()

    if(export_type not in ['csv','excel','json','raw']): sys.exit("ERROR: invalid export type selected") #avaliable eksport types
    
    #export_pathname=argv[3] #TODO: provide devault export pathname 
    main(export_type=export_type) #TODO