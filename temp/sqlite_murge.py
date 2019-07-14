import sqlite3
conn=sqlite3.connect('data_2001_jan.db')
c = conn.cursor()
#fo=open('p_data_2000_1.csv')

#data=str(id)+","+str(h)+","+str(d)+","+str(g)+","+str(q)+"\n"

c.execute('''CREATE TABLE patient
         (ID INTEGER  PRIMARY KEY AUTOINCREMENT,
         hos_id INTEGER     NOT NULL,
		 dis_id  INTEGER    NOT NULL,
         year  INTEGER    NOT NULL,
		 month  INTEGER    NOT NULL,
		 gender  INTEGER    NOT NULL,
		 quntity  INTEGER    NOT NULL);''')
conn.commit()
'''
for row in fo:
	data=row.replace("\n",'')
	data=data.split(",")
	c.execute('insert into patient(hos_id,dis_id,gender,quntity) values (?,?,?,?)',(data[1],data[2],data[3],data[4]))
'''
conn.commit()
