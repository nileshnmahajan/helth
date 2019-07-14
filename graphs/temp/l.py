import numpy as np
import matplotlib.pyplot as plt
import sqlite3 as db

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
def draw_pie2(parameters):
	#LEGENDS

	#DATA OF 4
	#month basis male nd female of 1 year 

	conn=db.connect('hos_patient_data_year_1.db')
	conn2=db.connect('hos_data.db')
	cur=conn.cursor()
	cur2=conn2.cursor()
	rog=[]
	data=[]
	for row in cur.execute('select dis_id,sum(male+female) as total from patient where month BETWEEN 3 AND 6 group by dis_id order by total desc limit 4'):
		data.append(row[1])
		q="select dname from disease where id = "+str(row[0])
		for row2 in cur2.execute(q):
			rog.append(row2[0])
	
	total=0
	for d in data:
			total=total+d
			print(">>")
	for i in range(0,4):
		data[i]=int((data[i]/total)*100)
	print(data);print(rog)	
	colors = ['r', 'y', 'pink','g']
	ax.pie(data,labels=rog , autopct='%1.1f%%',radius=1.3,explode = (0.1, 0, 0, 0),
									  colors=colors)

	ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	ax.set_title("top 4 disese in sumer seson ")
	plt.show()
	fig.savefig('sm.png')
draw_pie2(1)	