import sqlite3
conn = sqlite3.connect('hospital.db')
#con.isolation_level = None
c = conn.cursor()

fp1=open('hospital_c.csv','r',encoding="utf-8")

for row in fp1:
	data=row.replace("\n",'')
	data=data.split("_")
	c.execute('insert into Hospital(name,location) values (?,?)',(data[0],data[1]))

conn.commit()
conn.close()

