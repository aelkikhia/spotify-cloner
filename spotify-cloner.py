import time
import json
import requests

READ_AUTH_TOKEN = "BQA3KIZEdu7y7ojwRwh3eN1d2Ms_1DKodWeXhlhzhU0XYFnHli73VfkOYA6gpnOTaEi1T8GE8NK2n3Lz_9Cyop2OXpNR1AB5_74h1Rnu4tlZOhyxwRPgqQgmkDreSx2vN3CErFDuEljC_rvNzaKc5Tkjw8PqrmA-MAnHk92vmGnld71Pq26RRiijbvasV85A4UcB3BKqkOOsdFWb5AXqsZSFZDCwPfVWIVKlcts2Vc98YSLJ9aVPYd2FL9XvebnOdAFK9pbGilE"
MODIFY_AUTH_TOKEN = "BQA1DnB_J6jHyPzM1o9FivCX4sF9xmIfJfLMt36psHbXDSddwe49sbVToy5SVNa1jqeTIT-I6MsjbdoIH-4tglC-OVNBp9DMieGKsITsin5navunYfOurULqDC6dbRGliuV20LtEI03NxPD92cqMBzI1c5_gR70-jyp5mrtyleHe3I0568Gm6371cv2hRR1AEVa2G5ZvQ6vtj6EPVFsBTj4XG5zGr3e63p3DUZTRTum58W9q9O7M0LohyCj_WFjp6Rkv7g"

SPOTIFY_URI = "https://api.spotify.com/v1/me/"

GET_HEADERS = {"Authorization": "Bearer %s" % READ_AUTH_TOKEN,
               "Accept": "application/json",
               "Content-Type": "application/json"}

PUT_HEADERS = {"Authorization": "Bearer %s" % MODIFY_AUTH_TOKEN,
               "Accept": "application/json",
               "Content-Type": "application/json"}


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

        try:
            resp = requests.put(SPOTIFY_URI + "tracks",
                                headers=PUT_HEADERS,
                                data=json.dumps(track_ids[i:i + limit]))

            print(resp)

        except Exception as e:
            print("oh crap, get request failed, don't ask why ", resp)

        time.sleep(5)


def get_playlists():
    pass


def put_playlists():
    pass


def get_artists(limit=50):
    initial_call = True
    total = 9999999
    offset = 0
    artists = []
    resp = ""

    while offset < total:
        try:
            response = requests.get(SPOTIFY_URI + "following",
                                    headers=GET_HEADERS,
                                    params={"limit": limit,
                                            "offset": offset,
                                            "type": "artist"})
            resp = response.json()

            if "error" in resp:
                break

            artists.extend(resp["artists"]["items"])

            if initial_call:
                total = resp["artists"]["total"]
                initial_call = False

            print("Retrieving artists %d - %d of %d" % (offset,
                                                        offset+limit,
                                                        total))
            offset += limit

        except Exception as e:
            print("oh crap, get request failed, don't ask why")
            print(resp)

    if "error" not in resp:
        artist_ids = [item["id"] for item in artists]
        return artist_ids
    else:
        print(resp)


def put_artists(artist_ids, limit=20):

    length = len(artist_ids)
    resp = ""

    for i in range(0, length, limit):
        # body = json.dumps(artist_ids[i:i + limit])
        # print("saving artists: " + body)

        try:
            resp = requests.put(SPOTIFY_URI + "following",
                                headers=PUT_HEADERS,
                                params={"type": "artist"},
                                data={
                                    json.dumps(artist_ids[i:i + limit])
                                    }
                                )
            print(resp.text)

        except Exception as e:
            print("oh crap, get request failed, don't ask why " + e.__str__())

        time.sleep(2)


def put_albums(album_ids, limit=20):

    length = len(album_ids)
    resp = ""

    for i in range(0, length, limit):

        try:
            resp = requests.put(SPOTIFY_URI + "albums",
                                headers=PUT_HEADERS,
                                data=json.dumps(album_ids[i:i + limit]))

            print(resp)

        except Exception as e:
            print("oh crap, get request failed, don't ask why ", resp)

        time.sleep(5)


def delete_albums(album_ids, limit=20):
    length = len(album_ids)
    resp = ""

    for i in range(0, length, limit):
        try:
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

    artist_list = get_artists()
    if artist_list:
        put_artists(artist_list)

    # track_list = get_tracks()
    # print(track_list)
    # if track_list:
    #     put_tracks(track_list)

    # album_list = get_albums()

    # artist_list = get_artists()
    # playlists = get_playlists()

    # if album_list:
    #     put_albums(album_list)
