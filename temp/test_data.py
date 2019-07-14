import sqlite3
data = sqlite3.connect('data_2001_jan.db')
hos = sqlite3.connect('hospital.db')
#con.isolation_level = None
hc = hos.cursor()
dc = data.cursor()
#create table for store hospitals data
for row in dc.execute('select * from disease'):
	print(row)
'''
data.commit()
print ("1")
for row in hc.execute('select dname from disease'):
	dc.execute('insert into disease(dname) values (?)',(row[0],))

data.commit()

print ("2")
data.close()		
'''
hos.close()