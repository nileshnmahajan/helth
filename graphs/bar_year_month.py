#remaining of cleaning table description
import matplotlib.pyplot as plt
import sqlite3 as db

 
conn=db.connect('hos_patient_data_year_6.db')
conn2=db.connect('hos_data.db')
cur=conn.cursor()
cur2=conn2.cursor()
locations=[]
quantity=[]
sum=1000
for row in cur.execute('select hos_id,sum(male+female) as total from patient where month=7 group by hos_id,month order by total desc limit 10'):
	quantity.append(row[1]-sum)
	sum=sum+500
	q="select location from hospital where id = "+str(row[0])
	for row2 in cur2.execute(q):
		locations.append(row2[0][:8])

print(quantity);print(locations)	


plt.bar(locations, quantity, tick_label =locations,width = 0.5,color = ['r','aqua','c','m','pink','violet','wheat','y','salmon','g'])
 
plt.xlabel('locations')
plt.ylabel('quantity')
plt.xticks(rotation=20)
plt.title('bar char for top 10 locations')
plt.show()