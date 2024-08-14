#!/usr/bin/python3
"""
Module contains a recursive function to query the Reddit API and
return titles of all hot articles.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function to query the Reddit API and return titles of
    all hot articles.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Chrome'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    children = data.get('children', [])

    if not children:
        return hot_list if hot_list else None

    for post in children:
        hot_list.append(post['data']['title'])

    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list if hot_list else None
