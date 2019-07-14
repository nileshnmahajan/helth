import sqlite3
import random
from random import randint as r
#from django.utils.crypto import get_random_string
connect=[]
cursor=[]

for i in range(1,19):
	name='hos_patient_data_year_'+str(i)+'.db'
	connect.append(sqlite3.connect(name))	
for file in connect:
		cursor.append(file.cursor())	
for count in range(0,18):
	a=[1,2,3,4,5,6,7,8,9,0];
	i=j=k=l=0;
	numb=[]
	for i in range(0,10):
		for j in range(0,10):
			for k in range(0,10):	
				for l in range(0,10):
					num=str(a[i]),str(a[j]),str(a[k]),str(a[l]);
					num=int(''.join(num))
					if(num not in numb):
						numb.append(num)
	random.shuffle(numb)
	# print(min(numb))
	# print(max(numb))
	# print(numb)
	# exit()
	counter1=0
	counter2=1
	cursor[count].execute('''CREATE TABLE patient
         (ID INTEGER  PRIMARY KEY AUTOINCREMENT,
         month  NUMERIC    NOT NULL,
		 hos_id  NUMERIC    NOT NULL,
		 dis_id  NUMERIC    NOT NULL,
		 male  NUMERIC    NOT NULL,
 		 female  NUMERIC    NOT NULL);''')
	connect[count].commit()
	for m in range(1,13):#12 month
		for h in range(1,6):#5 hospital
			for d in range(1,81):#80 disease
				#2 gender
				mq=numb[counter1]
				fq=numb[counter2]
				
				counter1=counter1+2
				counter2=counter2+2
				
				query="insert into patient(month,hos_id,dis_id,male,female) values("+str(m)+","+str(h)+","+str(d)+","+str(mq)+","+str(fq)+")"
				# print(query)
				cursor[count].execute(query)
				
			# print('file',count+1,' month',m,'hospital>>>',h,'finish remain file ',18-count,' months ',12-m ,'hospital',500-h)
		connect[count].commit()
		print('file',count+1,' month>>>>>',m,'finish  remain file ',18-count,' months ',12-m)
	print('file>>>>',count+1,'finish remain file ',18-count)	
	connect[count].close()
	print('hos_patient_data_year_',count,'.db  write')
