import sqlite3
conn = sqlite3.connect('hospital.db')
#con.isolation_level = None
c = conn.cursor()

#create table for store hospitals data
for row in c.execute(' select * from Hospital'):
	 print (row) 
for row in c.execute(' select * from Users'):
	 print (row)
for row in c.execute(' select * from Disease'):
	 print (row)
	 
#conn.commit() no require while selecting no changes occure
conn.close()

