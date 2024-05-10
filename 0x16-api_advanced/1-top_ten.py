#!/usr/bin/python3
"""1-top_ten module."""
import requests


def top_ten(subreddit):
    """Query the Reddit API and print the title of the first 10 hot posts."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params)
    response_data = response.json()
    if response.status_code != 200:
        print(None)
        return
    for post in response_data.get('data').get('children'):
        post_title = post.get('data').get('title')
        print(post_title)
