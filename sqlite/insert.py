#inserting an image into the database

import sqlite3


#connect to the database
db = sqlite3.connect('images.sqlite')

#configure to allow binary inserts
db.text_factory = bytes

#grab your stuff in the database
r = open('../imageapp/dice.png', 'rb').read()

#insert yout stuff
db.execute('INSERT INTO image_store (image) VALUES (?)', (r,))
db.commit()
