import json
import os
import requests
from dotenv import load_dotenv

MAX_ENTRIES_PER_PAGE = 100
USER_TO_FOLLOW = ''  # hardcoded for now

load_dotenv()
MY_TOKEN = os.environ.get("MY_TOKEN")

headers = {'Authorization': 'token ' + MY_TOKEN}

followers = requests.get(
    f'https://api.github.com/users/paulinakhew/followers?per_page={MAX_ENTRIES_PER_PAGE}',
    headers=headers
).json()

following = requests.get(
    f'https://api.github.com/users/paulinakhew/following?per_page={MAX_ENTRIES_PER_PAGE}',
    headers=headers
).json()

followers_usernames = []
following_usernames = []

for person in followers:
    followers_usernames.append(person['login'])

for person in following:
    following_usernames.append(person['login'])

negative_followers = [x for x in following_usernames if x not in followers_usernames]
extra_followers = [x for x in followers_usernames if x not in following_usernames]

print("people that don't follow me back", negative_followers, len(negative_followers))
print("people I don't follow back", extra_followers, len(extra_followers))

data = {
    "Content-Length": 0
}

# unfollow users
resp = requests.put(
    url=f'https://api.github.com/user/following/{USER_TO_FOLLOW}',
    data=json.dumps(data),
    headers=headers
)
print(resp.json())
