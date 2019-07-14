#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('hos_data.db')
c = conn.cursor()
'''
c.execute("drop TABLE users_old")
conn.commit()
print("drop old")
c.execute("ALTER TABLE users RENAME TO users_old")
conn.commit()
print ("table renamed")
print ("Total number of rows updated :", conn.total_changes)
'''

c.execute('CREATE TABLE Users\
         (ID INTEGER  PRIMARY KEY AUTOINCREMENT ,\
         username           TEXT    NOT NULL,\
         email         TEXT,\
		  password         TEXT,\
		  hos_id  NUMERIC);')
		  
print ("table created")
print ("Total number of rows updated :", conn.total_changes)

c.execute('insert into users(username,password,hos_id) SELECT username,password,hos_id from users_old')
print("data inserted")
print ("Total number of rows updated :", conn.total_changes)

conn.commit()
conn.close()