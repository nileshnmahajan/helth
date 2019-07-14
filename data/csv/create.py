import sqlite3
from random import randint as r
fh=[]
for i in range(1,19):
	name='hos_patient_data_year_'+str(i)+'.csv'
	fh.append(open(name,'w'))
id=0
for count in range(0,18):
	id=	0
	data='ID,month,hos_id,dis_id,male,female\n'
	fh[count].write(data)
	for m in range(1,13):
		for h in range(1,501):
			for d in range(1,101):
				mq=r(6,500);fq=r(6,500)
				id=id+1
				data=str(id)+","+str(m)+","+str(h)+","+str(d)+","+str(mq)+","+str(fq)+"\n"
				fh[count].write(data)
			print('file',count+1,' month',m,'hospital>>>',h,'finish remain file ',18-count,' months ',12-m ,'hospital',500-h)
		print('file',count+1,' month>>>>>',m,'finish  remain file ',18-count,' months ',12-m)
	print('file>>>>',count+1,'finish remain file ',18-count+1)	
	fh[count].close()
	print('hos_patient_data_year_',count,'.csv  write')
