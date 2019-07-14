import sqlite3
conn=sqlite3.connect('hos_data.db')
c = conn.cursor()



for i in c.execute('select count(*) from patient'):
	print (i)
'''
conn.commit()
print("deleted !!!Total number of rows updated :", conn.total_changes)

c.execute('delete from patient where hos_id>500')
conn.commit()
print("deleted !!!Total number of rows updated :", conn.total_changes)

c.execute('delete from patient where year =18 and month>8')
conn.commit()
print("deleted !!!Total number of rows updated :", conn.total_changes)

c.execute('vacuum')
conn.commit()

print("vacumed !!!Total number of rows updated :", conn.total_changes)
'''
conn.close()
