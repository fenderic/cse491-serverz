#create the database and the table

import sqlite3

db = sqlite3.connect('images.sqlite')
db.execute('CREATE TABLE image_store (i INTEGER PRIMARY KEY, image BLOB)');
db.commit()
db.close()

# i is column with unique id
# image_store is column that contains binary objects (blobs)
