# image handling API

#import cPickle
#import os
import sqlite3

#IMAGE_DB_FILE = 'images.db'

#images = {}

def initialize():
    load()

def load():
#    global images
#    if os.path.exists(IMAGE_DB_FILE):
#        fp = open(IMAGE_DB_FILE, 'rb')
#        images = cPickle.load(fp)
#        fp.close()
#
#        print 'Loaded: %d images' % (len(images))
    return

def save():
#    fp = open(IMAGE_DB_FILE, 'wb')
#    cPickle.dump(images, fp)
#    fp.close()
    return

def add_image(filename, data):
#    if images:
#        image_num = max(images.keys()) + 1
#    else:
#        image_num = 0
#        
#    images[image_num] = (filename, data)
#    
#    save()
#    
#    return image_num

    db = sqlite3.connect('images.sqlite')
    db.text_factory = bytes
    c = db.cursor()
    c.execute('INSERT INTO image_store (image) VALUES(?)', (data,))
    db.commit()
    db.close()

def get_image(num):
#    return images[num]
    db = sqlite3.connect('images.sqlite')
    db.text_factory = bytes
    c = db_cursor()
#    c.execute('SELECT i,image FROM image_store WHERE i IS', num)
    i, image = c.fetchone()
    return image

def get_latest_image():
#    image_num = max(images.keys())
#    return images[image_num]
    db = sqlite3.connect('images.sqlite')
    db.text_factory = bytes
    c = db_cursor()
    c.execute('SELECT i,image FROM image_store ORDER BY i DESC LIMIT 1')
    i, image = c.fetchone()
    db.close()
    return image

