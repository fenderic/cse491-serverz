# __init__.py is the top level file in a Python package.

from quixote.publish import Publisher

# this imports the class RootDirectory from the file 'root.py'
from .root import RootDirectory
from . import html, image
# for the db stuff
import sqlite3

def create_publisher():
     p = Publisher(RootDirectory(), display_exceptions='plain')
     p.is_thread_safe = True
     return p
 
def setup():                            # stuff that should be run once.
    
    db = sqlite3.connect('images.sqlite')
    db.text_factory = bytes
    c = db.cursor()
    c.execute(
                'CREATE TABLE IF NOT EXISTS image_store \
                (i INTEGER PRIMARY KEY AUTOINCREMENT, image BLOB)'\
             )

    img = open('imageapp/grapered.jpg', 'rb').read()
    c.execute("INSERT INTO image_store (image) VALUES(?)", (img,))
    db.commit()
    db.close()
    
    html.init_templates()

    some_data = open('imageapp/grapered.jpg', 'rb').read()
    image.add_image('imageapp/grapered.jpg', some_data, 'Grapes', 'the default image')

def teardown():                         # stuff that should be run once.
    pass
