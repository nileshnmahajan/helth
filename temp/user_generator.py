from django.utils.crypto import get_random_string
import sqlite3 as sq

conn=sq.connect('hos_data.db')
c=conn.cursor()






c.execute('insert into users(username,password,hos_id) values (?,?,?)',(username,password,h))


alpha='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_@$#%&'
username = get_random_string(length=7, allowed_chars=alpha)
for h in range(3,5084):
	username = get_random_string(length=7, allowed_chars=alpha)
	username=username[0:3]+str(h)+username[3:];
	password = get_random_string(length=8, allowed_chars=alpha)
	print (username,' ',password,' ',h)
	c.execute('insert into users(username,password,hos_id) values (?,?,?)',(username,password,h))
	conn.commit()
conn.close()	