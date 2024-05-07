#!/usr/bin/python3
"""100-count module."""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """Query the Reddit API and count the number of times a word appears."""
    if word_count is None:
        word_count = {}

    if not word_list:
        sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f'{word.lower()}: {count}')
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    head = {'User-Agent': 'Mozilla/5.0'}
    p = {'limit': 100}
    if after:
        p['after'] = after
    response = requests.get(url, headers=head, params=p, allow_redirects=False)
    response_data = response.json()
    if response.status_code != 200:
        return
    if response.status_code == 404:
        return

    for post in response_data.get('data', {}).get('children', []):
        post_title = post.get('data', {}).get('title').lower()
        for word in word_list:
            if word.lower() in post_title:
                word_count[word.lower()] = word_count.get(word.lower(), 0) + 1
        after = response_data.get('data', {}).get('after')
        count_words(subreddit, word_list, after, word_count)
