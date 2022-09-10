#module imports
import credentials as cred
import spotipy_module as spm
import export_module as exm

#other imports
import sys

def main(artist_name, export_type, export_pathname):
    export_type = export_type.lower()

    auth_sp = spm.get_authentication(cred.client_id, cred.client_secret) 
    
    artist = spm.get_artist_by_name(auth_sp, artist_name)
    albums = spm.get_albums_by_artist(auth_sp, artist['id'])

    if(export_type=='csv'): exm.write_to_csv(json_data=albums,pathname=export_pathname+'.csv')
    elif(export_type=='excel'): exm.write_to_excel(json_data=albums,pathname=export_pathname+'.xlsx')
    elif(export_type=='json'): exm.write_to_jason(json_data=albums,pathname=export_pathname+'.json')
    else: exm.write_to_raw(json_data=albums)

if __name__ == '__main__':
    argv = sys.argv

    if(3 <= len(argv) <= 4 and argv[2].lower() in ['csv','excel','json','raw']): #check if contains 3 arguments and if provided correct export type
        artist_name = argv[1]
        export_type = argv[2]
        
        if(len(argv) == 4): export_pathname = exm.rmv_file_extension(argv[3]) #check if provided output file pathname, if yes clear its file extension... 
        else: export_pathname = exm.get_snake_case(artist_name) #... if not create pathname of artist_name

        main(artist_name=artist_name, export_type=export_type, export_pathname=export_pathname)
    else:
        error = "Error: invalid paramiters provided"
        error += "\nTry: get_artist_albums.py 'artist name' 'export type' 'file pathname'"
        error += "\n  'artist name' - name of the aritst in spotify"
        error += "\n  'export type' - avalible output formats: 'csv','excel','json' (each crates a file) or 'raw' (wites to console)"
        error += "\n  'file pathname' - optional pathname for output file (without file extension), when skipped artist_name is used"
        sys.exit(error)