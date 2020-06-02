import json
import os
import requests
from dotenv import load_dotenv

MAX_ENTRIES_PER_PAGE = 100

YOUR_GITHUB_USERNAME = ''

load_dotenv()
MY_TOKEN = os.environ.get("MY_TOKEN")
headers = {'Authorization': 'token ' + MY_TOKEN}


def get_all_followers():
    followers = requests.get(
        f'https://api.github.com/users/{YOUR_GITHUB_USERNAME}/followers?per_page={MAX_ENTRIES_PER_PAGE}',
        headers=headers
    ).json()
    return followers


def get_all_following():
    following = requests.get(
        f'https://api.github.com/users/{YOUR_GITHUB_USERNAME}/following?per_page={MAX_ENTRIES_PER_PAGE}',
        headers=headers
    ).json()
    return following


def get_follower_groups(followers: list, following: list):
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
    return negative_followers, extra_followers


def hit_follow_endpoint(username, headers):
    data = {"Content-Length": 0}

    resp = requests.put(
        url=f'https://api.github.com/user/following/{username}',
        data=json.dumps(data),
        headers=headers
    )
    return resp


def hit_unfollow_endpoint(username, headers):
    resp = requests.delete(
        url=f'https://api.github.com/user/following/{username}',
        headers=headers
    )
    return resp


def unfollow_all(negative_followers):
    for username in negative_followers:
        resp = hit_unfollow_endpoint(username, headers)
        if resp.status_code == 204:
            print(f'{username} unfollowed successfully')
        else:
            print(f'Could not unfollow {username}', resp.status_code)


def follow_all(extra_followers):
    for username in extra_followers:
        resp = hit_follow_endpoint(username, headers)
        if resp.status_code == 204:
            print(f'{username} followed successfully')
        else:
            print(f'Could not unfollow {username}', resp.status_code)


if __name__ == '__main__':
    followers = get_all_followers()
    following = get_all_following()

    negative_followers, extra_followers = get_follower_groups(followers, following)
    unfollow_all(negative_followers)
    follow_all(extra_followers)
