#imports
import spotipy as sp

#variables
result_size = 10 #TODO: set to desired ammount; #number of items returned from search in one batch, 50 itmes per batch is max

def get_authentication(cilent_id, client_secret):
    auth_manager = sp.SpotifyClientCredentials(client_id = cilent_id, client_secret = client_secret)
    auth_sp = sp.Spotify(auth_manager = auth_manager)
    return auth_sp

def get_artist_by_name(auth_sp, artist_name): #returns best match to artist_name
    results = auth_sp.search(q = artist_name, limit = 1, type = 'artist')
    return results['artists']['items'][0] #returns first atrist from list

def get_albums_by_artist(auth_sp, artist_id): #returns array of artist albums names
    results = auth_sp.artist_albums(artist_id = artist_id, album_type=['album'], limit = result_size, offset = 0) #album_type=['albums'] limits search to accual albums, replace [] with None to turn off, check soptipy docs for more opitons
    
    albums = []
    while(results['next'] != None): #while next bach of results avaliable
        for item in results['items']:
            albums.append(item['name']) #get just albums names
        results = auth_sp.next(results) #load next batch of results

    return albums