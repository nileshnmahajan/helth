import matplotlib.pyplot as plt
import sqlite3 as db
from django.template.defaultfilters import linebreaksbr


from graphs.graph import fig

def bottom_4_winter(year,month):
	#LEGENDS
	print("year ",year, "graph and data is generating for Winter dession lowest")
	#DATA OF 4
	#month basis male nd female of 1 year 

	name='data/hos_patient_data_year_'+str(year)+'.db'
	conn=db.connect(name)
	conn2=db.connect('hos_data.db')
	cur=conn.cursor()
	cur2=conn2.cursor()
	rog=[]
	data=[]
	for row in cur.execute('select dis_id,sum(male+female) as total from patient where month IN (11,12,1,2) group by dis_id order by total asc limit 4'):
		data.append(row[1])
		q="select dname from disease where id = "+str(row[0])
		for row2 in cur2.execute(q):
			rog.append(row2[0])
	

	colors = ['g', 'pink', 'y','r']
	plt.pie(data,labels=rog , autopct='%1.1f%%',radius=1.1,explode = (0, 0, 0, 0.1),
									  colors=colors)
	plt.legend(bbox_to_anchor=(0.7, 1), loc=2)
	# plt.title("top 4 Disease in winter Season ")
	#plt.show()
	name='graphs/static/g5_'+str(2000+year)+'.png'
	
	fig.savefig(name, dpi=100)
	plt.clf()
	#plt.gcf().clear()
	nm='g5_'+str(2000+year)+'.png'
	tableth=['disease','quntity']
	tabletd=[]
	desc="in year "+str(year+2000)+"there are lowest 4 disease are "+','.join(rog)+" of total patient "+str(sum(data))+"  in winter seson out of that : \n" 
	for i in range(0,len(rog)):
		desc=desc+"\n "+str(data[i]) +" patient of disease  "+rog[i]
	desc=linebreaksbr(desc)

	for i in range(0,4):
			tabletd.append([rog[i],data[i]])
	data=['bottom 4 Disease in winter Season ',nm,desc,tableth,tabletd]
	print("year ",year, "graph and data is generating for Winter dession lowest finish")
	return data
	
	