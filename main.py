from database import Database
from constants import PHOTO_TYPE, VIDEO_TYPE, GIF_TYPE


def get_data(content_type, num, tag):
    db = Database()
    data = []

    if content_type.lower() == 'image':
        data = db.get_media(PHOTO_TYPE, num, tag)
    elif content_type.lower() == 'video':
        data = db.get_media(VIDEO_TYPE, num, tag)
    elif content_type.lower() == 'gif':
        data = db.get_media(GIF_TYPE, num, tag)
    elif content_type.lower() == 'overall':
        data = db.get_overall(num, tag)
    else:
        print "Unable to process request try: \n1. image <num> \n2. video <num> \n3. gif <num> \n4. overall <num>"

    count = 0
    for item in data:
        count += 1
        print "\nItem Number {0}".format(count)
        print "Type: {0}".format(item['type'])
        print "Title: {0}".format(item['title'].encode('ascii', 'ignore'))
        print "URL: {0}".format(item['post_url'])


def run():
    while True:
        print 'Enter the Query: '
        query = raw_input().split()
        content_type = query[0]
        num = int(query[1])
        tag = None

        if len(query) > 2:
            tag = query[2]

        get_data(content_type, num, tag)

        if raw_input('Do you want to continue? (y/n)? ').lower() == 'n':
            break


if __name__ == '__main__':
    run()
