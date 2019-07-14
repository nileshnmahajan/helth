import sqlite3
conn = sqlite3.connect('hospital.db')
#con.isolation_level = None
c = conn.cursor()

#create table for store hospitals data
c.execute('''CREATE TABLE hospital
         (ID INTEGER  PRIMARY KEY AUTOINCREMENT,
         NAME           TEXT    NOT NULL,
         location         TEXT);''')
#create table for diseasr table
c.execute('''CREATE TABLE disease
         (ID INTEGER  PRIMARY KEY AUTOINCREMENT ,
         dname   TEXT);''')

c.execute('''CREATE TABLE Users
         (ID INTEGER  PRIMARY KEY AUTOINCREMENT ,
         username           TEXT    NOT NULL,
         email         TEXT,
		  password         TEXT,
		  hos_id  NUMERIC    NOT NULL);''')
		
		 
c.execute('''CREATE TABLE patient
         (ID INTEGER  PRIMARY KEY AUTOINCREMENT,
         hos_id  NUMERIC    NOT NULL,
		 dis_id  NUMERIC    NOT NULL,
		 year  NUMERIC    NOT NULL,
		 month  NUMERIC    NOT NULL,
		 gender  NUMERIC    NOT NULL,
		 quntity  NUMERIC    NOT NULL);''')
conn.commit()
conn.close()

