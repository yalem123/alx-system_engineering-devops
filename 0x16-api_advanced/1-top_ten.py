#!/usr/bin/python3
"""
function that quersies Reddit API and post 
the first 10 lines
"""
import request
import sys


def top_ten(subreddit):
    """
    return the 1st 10 hot posts
    """
    u_agent = 'mozila/5.0'

    header = {
            
            'User_Agent': u_agent
    }

    params = {

            'limits': 10
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        print(None)
        return
    dic = res.json()
    hot_posts = dic['data']['children']
    if len(hot_posts) is 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])    
