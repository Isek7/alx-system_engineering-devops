#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """ Queries the Reddit API """
    u_agent = 'Mozilla/5.0'
    headers = {'User-Agent': u_agent}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    res = requests.get(url, headers=headers, allow_redirects=False)
    
    if res.status_code != 200:
        return 0
    
    dic = res.json()
    return dic.get('data', {}).get('subscribers', 0)
