import os
import requests

MAX_ENTRIES_PER_PAGE = 100

MY_TOKEN = os.getenv("MY_TOKEN")

followers = requests.get(
    f'https://api.github.com/users/paulinakhew/followers?per_page={MAX_ENTRIES_PER_PAGE}',
    {'Authorization': MY_TOKEN}
).json()
following = requests.get(
    f'https://api.github.com/users/paulinakhew/following?per_page={MAX_ENTRIES_PER_PAGE}',
    {'Authorization': MY_TOKEN}
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

# unfollow users
