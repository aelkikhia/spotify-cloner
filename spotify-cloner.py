import time
import json
import requests
# from urllib import request, parse

READ_AUTH_TOKEN = ""
MODIFY_AUTH_TOKEN = ""

SPOTIFY_API_URI = "https://api.spotify.com/v1/"
GET_HEADERS = {'Authorization': "Bearer %s" % READ_AUTH_TOKEN,
               "Accept": "application/json"}
POST_HEADERS = {}


def run_transfer():
    pass


def fetch_album_list(limit=1, output='my_spotify_albums.json'):

    albums_url = SPOTIFY_API_URI + "me/albums"
    initial_call = True
    total = 999
    offset = 0
    albums = []
    resp = ""

    while offset < total:
        try:
            response = requests.get(albums_url,
                                    headers=GET_HEADERS,
                                    params={'limit': limit, 'offset': offset})
            resp = response.json()

            if "error" in resp:
                print(resp)
                break

            albums.extend(resp['items'])

            if initial_call:
                total = resp['total']
                initial_call = False

            print("Retrieving albums %d - %d of %d" % (offset,
                                                       offset+limit,
                                                       total))
            offset += limit

        except requests.RequestException:
            print("oh crap, get request failed, don't ask why")

    if "error" not in resp:
        out = {'items': albums}
        fp = open(output, 'w')
        json.dump(out, fp)
        fp.close()
        # return out


def fetch_artist_list():
    pass


def show_albums():
    pass


def show_artists():
    pass


def put_artist_list():
    pass


def put_album_list():
    pass


if __name__ == "__main__":
    fetch_album_list()
