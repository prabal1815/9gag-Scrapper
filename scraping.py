#!/usr/bin/python

import json
import urllib2
from constants import URL, POSTS_LIMIT, USER_AGENT, GIF_TYPE, VIDEO_TYPE
from database import Database


def scraping():
    db = Database()
    count = 0
    list_of_posts = []

    url = URL
    while count < POSTS_LIMIT:
        next_cursor, posts = get_posts(url)
        for post in posts:
            post_type = post['type']

            if post_type == 'Animated':
                post_type = GIF_TYPE if post['images']['image460sv']['hasAudio'] == 0 else VIDEO_TYPE

            post_info = {
                "type": post_type,
                "title": post['title'],
                "post_url": post['url'],
                "tags": [tags['key'] for tags in post['tags']],
            }
            list_of_posts.append(post_info)
            count += 1
        url = URL + '?' + next_cursor

    db.save(list_of_posts)


def get_posts(url):
    request = urllib2.Request(url, headers={'User-Agent': USER_AGENT})
    response = urllib2.urlopen(request)
    data = json.loads(response.read())['data']
    posts = data['posts']
    next_cursor = data['nextCursor']
    return next_cursor, posts


if __name__ == '__main__':
    scraping()
