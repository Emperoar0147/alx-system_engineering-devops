#!/usr/bin/python3
"""
1-top-ten
"""

import requests


def top_ten(subreddit):
    """ Print top ten hot posts """
    if subreddit:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
        headers = {'User-Agent': 'Chrome'}
        response = requests.get(url, headers=headers,  allow_redirects=False)
        if response.status_code == 200:
            posts = response.json().get('data').get('children')
            for post in posts:
                print(post.get('data').get('title'))
        print('None')
