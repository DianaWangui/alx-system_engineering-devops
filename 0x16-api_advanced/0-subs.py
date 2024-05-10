#!/usr/bin/python3
"""0-subs module."""
import requests


def number_of_subscribers(subreddit):
    """Query the Reddit API and returns the number of subscribers."""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        return response.json().get('data').get('subscribers')
    except Exception:
        return 0
