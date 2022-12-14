#module imports
import spotipy_module as spm
import export_module as exm
import misc_module as mm

#other imports
import sys

#messages
setup_error_credentials_missing = ("SETUP ERROR: client id or secret is not set."
+ "\n Set credentials with: get_artist_albums.py -c 'client_id' 'client_secret'")

error_artist_name_mismatch = "ERROR: artist not found, did you mean: \""

error_pathname_missing = "SCRIPT ERROR: export_pathname missing."
error_type_missing = "SCRIPT ERROR: export_type missing."

error_invalid_paramiters = ("Error: invalid paramiters provided"
+ "\nTry: get_artist_albums.py 'artist name' 'export type' 'file pathname'"
+ "\n  'artist name' - name of the aritst in spotify"
+ "\n  'export type' - avalible output formats: 'csv','excel','json' (each crates a file) or 'raw' (wites to console)"
+ "\n  'file pathname' - optional pathname for output file (without file extension), when skipped artist_name is used")

#variables
cred = mm.get_credentials()

def main(artist_name, export_type, export_pathname=None):
    export_type = export_type.lower()
    
    auth_sp = spm.get_authentication(cred['client_id'], cred['client_secret']) 
    
    artist = spm.get_artist_by_name(auth_sp, artist_name)
    if(artist_name != artist['name']): sys.exit(error_artist_name_mismatch + artist['name'] + '"?') #check if exact match found, if not exit with error message

    albums = spm.get_albums_by_artist(auth_sp, artist['id'])

    if(export_type=='raw'): exm.write_to_raw(json_data=albums)
    else:
        if(export_pathname == None): sys.exit(error_pathname_missing) #backup check if pathname provided, if no script failed and requires fix 

        #if file allready exists, below will exit with error message, set overwrite to True to disable
        if(export_type=='csv'): exm.write_to_csv(json_data=albums,pathname=export_pathname+'.csv')
        elif(export_type=='excel'): exm.write_to_excel(json_data=albums,pathname=export_pathname+'.xlsx')
        elif(export_type=='json'): exm.write_to_jason(json_data=albums,pathname=export_pathname+'.json')
        else: sys.exit(error_type_missing) #if execution reached this line script failed and requires fix
    
if __name__ == '__main__':
    argv = sys.argv

    if(len(argv) == 4 and argv[1] in ['-c']): mm.set_credentials(client_id=argv[2],client_secret=argv[3]) #changing credentials operation, check if selected

    elif( (cred['client_id'] in [None,'']) 
    or (cred['client_secret'] in [None,''])): sys.exit(setup_error_credentials_missing)  #check if credentials missing

    elif(3 <= len(argv) <= 4 and argv[2].lower() in ['csv','excel','json','raw']): #get albums of artsit operation, check if contains 3 arguments and if provided correct export type, if not exit with error message
        artist_name = argv[1]
        export_type = argv[2]
        
        if(export_type == 'raw'): #check if export type is 'raw', if yes skip pathname paramiter
            main(artist_name=artist_name, export_type=export_type)
        else:
            if(len(argv) == 4): export_pathname = mm.rmv_file_extension(argv[3]) #check if provided output file pathname, if yes clear its file extension... 
            else: export_pathname = mm.get_snake_case(artist_name) #... if not create pathname of artist_name
            main(artist_name=artist_name, export_type=export_type, export_pathname=export_pathname)
        
    else: sys.exit(error_invalid_paramiters)