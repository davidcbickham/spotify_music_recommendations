import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

username = sys.argv[1]

# https://open.spotify.com/user/dbick001?si=12CI2gy4SDC3sQm6s3780A
# username = dbick001

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)


# Create Spotify Object
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()
# print(json.dumps(user, sort_keys=True, indent=4))

displayName = user['display_name']
followers = user['followers']['total']


while True:
    print()
    print(">>> Welcome to Spotipy " + displayName + "!")
    print(">>> You have " + str(followers) + " followers.")
    print()
    print("0 - Search for an artist")
    print("1 - exit")
    print()
    choice = input("Your choice: ")

    # Search for artist
    if choice == "0":
        print()
        SearchQuery = input("Ok, what's their name?: ")
        print()

        searchResults = spotifyObject.search(SearchQuery,1,0,"artist")
        print(json.dumps(searchResults, sort_keys=True, indent=4))

    if choice == "1":
        break





# print(json.dumps(VARIABLE, sort_keys=True, indent=4))


# export SPOTIPY_CLIENT_ID='bf177e9a897347ebbf481db519249ca4'
# export SPOTIPY_CLIENT_SECRET='094aca58f14441bda15dc906cf75c56a'
# export SPOTIPY_REDIRECT_URI='http://google.com/'
