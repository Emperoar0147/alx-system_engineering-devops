#!/usr/bin/python3
"""
Recursive function to query the Reddit API, parse the titles
of all hot articles,
and print a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """
    Recursive function to query the Reddit API, parse the titles ofc
    all hot articles,
    and print a sorted count of given keywords.
    """
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    children = data.get('children', [])

    for child in children:
        title = child.get('data', {}).get('title', '').lower()
        for word in word_list:
            if word.lower() in title:
                counts[word] = counts.get(word, 0) + 1

    after = data.get('after')
    if after:
        count_words(subreddit, word_list, counts, after)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
