#!/usr/bin/python3
'''
Recursive function that queries the Reddit API
and returns a list containing the
titles of all hot articles for a given subreddit.
'''
import itertools
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    '''
    Recursivly return list count
    of hot articles
    '''

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = 'reddit_user'

    if after:
        url += '?after={}'.format(after)
    headers = {'User-Agent': user_agent}
    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        return None

    data = req.json()['data']

    posts = data['children']
    for post in posts:
        count += 1
        hot_list.append(post['data']['title'])

    after = data['after']
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    else:
        return hot_list
