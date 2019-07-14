import sqlite3
from random import randint as r
connect=[]
cursor=[]

for i in range(1,19):
	name='hos_patient_data_year_'+str(i)+'.db'
	connect.append(sqlite3.connect(name))
	
		
for file in connect:
		cursor.append(file.cursor())

		
for count in range(0,18):
	cursor[count].execute('''CREATE TABLE patient
         (ID INTEGER  PRIMARY KEY AUTOINCREMENT,
         month  NUMERIC    NOT NULL,
		 hos_id  NUMERIC    NOT NULL,
		 dis_id  NUMERIC    NOT NULL,
		 male  NUMERIC    NOT NULL,
 		 female  NUMERIC    NOT NULL);''')
	connect[count].commit()
	for m in range(1,13):
		for h in range(1,501):
			for d in range(1,101):
				q=random.sample(range(1, 501), 2)
				mq=q[0];fq=q[1]
				query="insert into patient(month,hos_id,dis_id,male,female) values("+str(m)+","+str(h)+","+str(d)+","+str(mq)+","+str(fq)+")"
				cursor[count].execute(query)
			print('file',count+1,' month',m,'hospital>>>',h,'finish remain file ',18-count,' months ',12-m ,'hospital',500-h)
		connect[count].commit()
		print('file',count+1,' month>>>>>',m,'finish  remain file ',18-count,' months ',12-m)
	print('file>>>>',count+1,'finish remain file ',18-count)	
	connect[count].close()
	print('hos_patient_data_year_',count,'.db  write')
