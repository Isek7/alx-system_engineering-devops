#!/usr/bin/python3
'''Module containing subreddit api task'''
import requests


def top_ten(subreddit):
    '''
    queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    If an invalid subreddit is given, the function should print None.
    '''
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0"
            }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
    results = response.json().get("data")
    [print(item.get("data").get("title")) for item in results.get("children")]
