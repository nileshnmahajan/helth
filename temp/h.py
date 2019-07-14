import sqlite3
conn = sqlite3.connect('hos_data.db')
#con.isolation_level = None
c = conn.cursor()

c.execute('drop table hospital')

c.execute('''CREATE TABLE hospital
        (ID INTEGER  PRIMARY KEY AUTOINCREMENT,
       NAME           TEXT    NOT NULL,
      location         TEXT);''')

fp1=open('hospitals.csv','r')

for row in fp1:
	data=row.replace("\n",'')
	data=data.split("`")
	print(data)
	c.execute('insert into Hospital(name,location) values (?,?)',(data[0],data[1]))
conn.commit()
conn.close()

