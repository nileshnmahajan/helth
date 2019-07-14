import sqlite3
from random import randint

conn=sqlite3.connect('hos_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE patient
         (ID INTEGER  PRIMARY KEY AUTOINCREMENT,
         hos_id  NUMERIC    NOT NULL,
		 dis_id  NUMERIC    NOT NULL,
		 year  NUMERIC    NOT NULL,
		 month  NUMERIC    NOT NULL,
		 gender  NUMERIC    NOT NULL,
		 quntity  NUMERIC    NOT NULL);''')
conn.commit()

total=19*12

for y in range(0,19):	
	for m in range(1,13):
		for h in range(1,5098):
			for d in range(1,99):
				for g in range(1,3):
					c.execute('insert into patient(hos_id,dis_id,year,month,gender,quntity) values (?,?,?,?,?,?)',(h,d,y,m,g,randint(0, 501)))
		total=total-1
		print ('finish of year ',y,' and month ',m,' remain ',total,' files ')
		conn.commit()
	