import time
import json
import requests
# from urllib import request, parse

READ_AUTH_TOKEN = "BQA7NaDximJ0RWHIpbmjD5k3ZM_9Bf_YGOJUj0GQIcuCuejH4DsoW7cw6_3tJ0YVA6d5mD0E58kxCk7TnWMWkM1CYtx1ikVtjwoEvWP5_eijYgh1CbdFOzQz7av5WsG_2NRVypJj4DWuTXzJ_gENMxUwM0E0CbMzdwdBVu_OTtOv4kZ-ecufo_Ga5bfSFXaK1QKW6Vb0Ykt0o7lBE-6DSZ3zL6YVVCDf6a9hFVUXMREbVUQdoTtCKUficmVgTElZ3ceONp64vBc"
MODIFY_AUTH_TOKEN = "BQCwi6qoSgrzq2ug14Qj9a2mCQPgiqFy3fQ7zvE2eFScL7Qwg1wzQpWOMdOyN-6boQl0oSp3J4qpJ0NeWzgiE46guhfVsnyeHH0L8P8n8ZGJiZ3mPT83dsZFNRH9BHnx6iIvzblQkjwdwq8NoeyVpBgeu0zUPI4IIG0_V6f9aCmy-Oi4TDzLrlQBx5W8L7WJbeMzFucQ0iNTElviQyiZNbvaHczVpvrsEBWSNYctK69gQUzEtebRuXs1EORC8IV_EJGa-Q"

ALBUM_URI = "https://api.spotify.com/v1/me/albums"
GET_HEADERS = {'Authorization': "Bearer %s" % READ_AUTH_TOKEN,
               "Content-Type": "application/json"}
PUT_HEADERS = {'Authorization': "Bearer %s" % MODIFY_AUTH_TOKEN,
               "Content-Type": "application/json"}


def run_transfer():
    pass


def get_albums(limit=50, output='my_spotify_albums.json'):

    initial_call = True
    total = 9999999
    offset = 0
    albums = []
    resp = ""

    while offset < total:
        try:
            response = requests.get(ALBUM_URI,
                                    headers=GET_HEADERS,
                                    params={'limit': limit, 'offset': offset})
            resp = response.json()

            if "error" in resp:
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
        album_ids = [item['album']['id'] for item in albums]
        return album_ids
    else:
        print(resp)


def get_artists():
    pass


def show_albums():
    pass


def show_artists():
    pass


def put_artists():
    pass


def post_albums(album_ids):

    length = len(album_ids)
    limit = 49
    resp = ""

    for i in range(0, length, limit):
        # print(json.dumps(album_ids[i:i + limit]))
        try:
            response = requests.put(
                ALBUM_URI,
                headers=PUT_HEADERS,
                # params={"ids": json.dumps(album_ids[i:i + limit])}

                data=json.dumps(album_ids[i:i + limit])
            )

            print(response.text)

        except requests.RequestException:
            print("oh crap, get request failed, don't ask why ", resp)

        time.sleep(1)


if __name__ == "__main__":
    album_list = get_albums()

    if album_list:
        post_albums(album_list)

    # post_albums([])
