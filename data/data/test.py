import sqlite3
conn=sqlite3.connect('hos_patient_data_year_1.db')
c=conn.cursor()

for row in c.execute('select * from patient'):
	print (row)