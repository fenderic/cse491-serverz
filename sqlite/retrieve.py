#retrieve image from the database

import sqlite3
import sys

#connect to database
db = sqlite3.connection('images.sqlite')

#configure to retrieve bytes
db.text_factory = bytes

#get query handle
c = db.cursor()

#select all the images
c.execute('SELECT i, image FROM image_store ORDER BY i DESC LIMIT 1')

#grab first result
i, image = c.fetchone()

#write 'image' data out to sys.argv[1]
print 'writing image', i
open(sys.argv[1], 'w').write(image)

