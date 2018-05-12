import time
import json
import requests
# from urllib import request, parse

READ_AUTH_TOKEN = "BQBBy909C3SO1d0QeXqL4JCHDKTwA8HXLJycoBtoh29MEoFTEFhoerpDfzUf5asPwBeQnIaTyVhCvz_qTY9ug7_E7YSGIM70QJExPF_WfDIGqzBCULYbFir2NhgCSZGSkbiNJcD2SzLBxBl0Y-47PBYKUHk47z-prwLQZV1IcmeIaKRKmjTDdFmgrmVA2MwpF-DQMFOalO-1LX-Q_1mrTinp6RtfDG0qKZLenPJYAjyG9SbLLhegF-kG58khIunGJlITNw"
MODIFY_AUTH_TOKEN = "BQDTtifzIaXRntfMyG6NmskeXSUg4AEkWLiAOjM_KPfANAKYokSFlcsw1wsDVog26jGwfYN9adCoMe5LrZ0mnJ0cLuA_cJb7KYaVfbwHZGXXWElHxOET3mynJPY_qq305NVen5fX4hSGi_Ef0Jf2e5bsxV70RW5XjfS2cVjc7WVmwtABafvLOdtjYl21EZuVPH25CIy0ahACBQoKtQU0zSXCARbi17b1yjM3BVGRzkYxCmfeQBkplQxbY2vos8Ufk_43cw"

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


def post_albums(album_ids, limit=20):

    length = len(album_ids)
    resp = ""

    for i in range(0, length, limit):
        body = json.dumps(album_ids[i:i + limit])
        print("saving albums: " + body)

        try:
            resp = requests.put(ALBUM_URI, headers=PUT_HEADERS, data=body)

            print(resp)

        except requests.RequestException:
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
                ALBUM_URI,
                headers=PUT_HEADERS,
                data=json.dumps(album_ids[i:i + limit])
            )

            print(response.text)

        except requests.RequestException:
            print("oh crap, get request failed, don't ask why ", resp)

        time.sleep(3)


if __name__ == "__main__":
    album_list = get_albums()

    if album_list:
        post_albums(album_list)

