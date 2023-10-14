import requests
import datetime


def get_access_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()['access_token']


def fetch_song_from_playlist(access_token, playlist_link):

    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(playlist_link, headers=headers)
    response.raise_for_status()
    data = response.json()

    return song_of_the_week(data)


def song_of_the_week(data):
    start_week = 37  # for september 16
    current_week = datetime.datetime.today().isocalendar()[1]
    return data['tracks']['items'][current_week - start_week]['track']


if __name__ == "__main__":
    CLIENT_ID = "5972487482b145d183008a0ff7af682e"
    CLIENT_SECRET = "7411610ad87f42b9958d7472531dee9c"
    PLAYLIST_ID = "7gmLrKkw6OMl70O5Y2CEtM"
    PLAYLIST_LINK = f'https://api.spotify.com/v1/playlists/{PLAYLIST_ID}?market=US'

    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
    song = fetch_song_from_playlist(access_token, PLAYLIST_LINK)

    song_name = song['name']
    artist_name = song['artists'][0]['name']
    song_link = song['external_urls']['spotify']

    print(f"Song Name: {song_name}")
    print(f"Artist Name: {artist_name}")
    print(f"Song Link: {song_link}")


