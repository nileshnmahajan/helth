import sqlite3

conn = sqlite3.connect('hos_data.db')

c = conn.cursor()
fp1=open('rog.csv','r',encoding="utf-8")
count=0
for row in fp1:
	count=count+1
	data=row.replace("\n",'')
	c.execute('insert into Disease(dname) values (?)',(data,))
	if(count==2):
		break
conn.commit()
conn.close()

