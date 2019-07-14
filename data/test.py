import sqlite3 as db
conn=db.connect('hos_patient_data_year_1.db')
cur=conn.cursor()
fo=open('data.csv','w')

from random import randint as r
for row in cur.execute('select dis_id,sum(male+female) as total from patient where month BETWEEN 3 AND 6 group by dis_id order by total asc limit 4'):
	print(row)
import random

conn.close()

	


