#!/usr/bin/python3
""" 2-recursive module """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    response_data = response.json()

    if response.status_code != 200:
        return None

    for post in response_data.get('data', {}).get('children', []):
        hot_list.append(post.get('data', {}).get('title'))

    after = response_data.get('data', {}).get('after')
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
