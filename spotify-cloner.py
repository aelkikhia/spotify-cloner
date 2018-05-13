import time
import json
import requests
# from urllib import request, parse

READ_AUTH_TOKEN = "BQB9sSwZ5EjWXD-8cfbfskJwq240r3xJmccyqxsot6PRG1vQLinh5LO5bDsQOjxFQhzGBPYXExL4UveM1yq0C6SREMeJ_wsxTdkiNzgUQmTTzdyuj9ZHSPTVVMBF6zsoBbJmG2mbLRCsWGIj1UbhQJpHL-QpGZ4ow2RV6ebPovWe3r5PTdnTNI_sNZraBIb32JY8cA4i-1MsYddTAE7am23A8aOHpQbNRVAtWfcTYE0UJcuhe8gNI5WEft7Fy_P4GSIuVQPndMg"
MODIFY_AUTH_TOKEN = "BQA1uf4lLIeLglfru012_XZ5k8kkwBh505tYfC8014Ryu6j-mGJckSAN6Y4gwfWghLdV9XBsrFPDSdbF3mUT80ELPEjaZsxE4kRDDc505fNB5xE1qDiTEfYdgb0xeaUrM6FrTyErLqlnLQcpI1PN22zdp9tpEnlHMhRVTAY0BhJz7WDsypUmSblMJ3sGq3_tLLHgynp8lNwP6Fwb83nKBOAFtUUaXLSeKvi174eWD4V3n6stOF5nqteHFuVpdTqj31NYsA"

SPOTIFY_URI = "https://api.spotify.com/v1/me/"

GET_HEADERS = {"Authorization": "Bearer %s" % READ_AUTH_TOKEN,
               "Content-Type": "application/json"}

PUT_HEADERS = {"Authorization": "Bearer %s" % MODIFY_AUTH_TOKEN,
               "Content-Type": "application/json"}


def run_transfer():
    pass


def get_albums(limit=50):

    initial_call = True
    total = 9999999
    offset = 0
    albums = []
    resp = ""

    while offset < total:
        try:
            response = requests.get(SPOTIFY_URI + "albums",
                                    headers=GET_HEADERS,
                                    params={"limit": limit, "offset": offset})
            resp = response.json()

            if "error" in resp:
                break

            albums.extend(resp["items"])

            if initial_call:
                total = resp["total"]
                initial_call = False

            print("Retrieving albums %d - %d of %d" % (offset,
                                                       offset+limit,
                                                       total))
            offset += limit

        except Exception as e:
            print("oh crap, get request failed, don't ask why")

    if "error" not in resp:
        album_ids = [item["album"]["id"] for item in albums]
        return album_ids
    else:
        print(resp)


def get_tracks(limit=50):
    initial_call = True
    total = 9999999
    offset = 0
    tracks = []
    resp = ""

    while offset < total:
        try:
            response = requests.get(SPOTIFY_URI + "tracks",
                                    headers=GET_HEADERS,
                                    params={"limit": limit, "offset": offset})
            resp = response.json()

            if "error" in resp:
                break

            tracks.extend(resp["items"])

            if initial_call:
                total = resp["total"]
                initial_call = False

            print("Retrieving tracks %d - %d of %d" % (offset,
                                                       offset+limit,
                                                       total))
            offset += limit

        except Exception as e:
            print("oh crap, get request failed, don't ask why")

    if "error" not in resp:
        track_ids = [item["track"]["id"] for item in tracks]
        return track_ids
    else:
        print(resp)


def put_tracks(track_ids, limit=20):

    length = len(track_ids)
    resp = ""

    for i in range(0, length, limit):
        body = json.dumps(track_ids[i:i + limit])
        print("saving tracks: " + body)

        try:
            resp = requests.put(SPOTIFY_URI + "tracks",
                                headers=PUT_HEADERS,
                                data=body)

            print(resp)

        except Exception as e:
            print("oh crap, get request failed, don't ask why ", resp)

        time.sleep(5)


def get_playlists():
    pass


def put_playlists():
    pass


def get_artists():
    pass


def put_artists():
    pass


def post_albums(album_ids, limit=20):

    length = len(album_ids)
    resp = ""

    for i in range(0, length, limit):
        body = json.dumps(album_ids[i:i + limit])
        print("saving albums: " + body)

        try:
            resp = requests.put(SPOTIFY_URI + "albums",
                                headers=PUT_HEADERS,
                                data=body)

            print(resp)

        except Exception as e:
            print("oh crap, get request failed, don't ask why ", resp)

        time.sleep(5)


def delete_albums(album_ids, limit=20):
    length = len(album_ids)
    resp = ""

    for i in range(0, length, limit):
        try:
            # body = json.dumps(album_ids[i:i + limit])
            # print(body)
            response = requests.delete(
                SPOTIFY_URI + "albums",
                headers=PUT_HEADERS,
                data=json.dumps(album_ids[i:i + limit])
            )

            print(response.text)

        except Exception as e:
            print("oh crap, get request failed, don't ask why ", resp)

        time.sleep(3)


if __name__ == "__main__":
    # album_list = get_albums()
    track_list = get_tracks()
    print(track_list)
    if track_list:
        put_tracks(track_list)
    # artist_list = get_artists()
    # playlists = get_playlists()

    # if album_list:
    #     post_albums(album_list)

