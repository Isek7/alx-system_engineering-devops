#!/usr/bin/python3
"""Advanced API module using reddit api endpoint"""
import requests


def number_of_subscribers(subreddit):
    """Request reddit api and return subreddit count"""
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    num_subs = 0
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        num_subs = data["data"]["children"][1]["data"]["subreddit_subscribers"]
        return num_subs
    except requests.exceptions.HTTPError as error:
        return num_subs
