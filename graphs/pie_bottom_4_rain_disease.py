#bottom 4 diseases in rain Season on pie chart
import matplotlib.pyplot as plt
import sqlite3 as db
from graphs.graph import fig
from django.template.defaultfilters import linebreaksbr
def bottom_4_rain(year,month):
	print("year ",year, "graph and data is generating for rain dession lowest")
	#LEGENDS
	#DATA OF 4
	#month basis male nd female of 1 year 
	#select db of that year user selected which year
	name='data/hos_patient_data_year_'+str(year)+'.db'
	conn=db.connect(name)
	conn2=db.connect('hos_data.db')
	cur=conn.cursor()
	cur2=conn2.cursor()
	rog=[]
	data=[]
	
	for row in cur.execute('select dis_id,sum(male+female) as total from patient where month IN (7,8,9,10) group by dis_id order by total asc limit 4'):
		data.append(row[1])
		q="select dname from disease where id = "+str(row[0])
		for row2 in cur2.execute(q):
			rog.append(row2[0])
	
	tableth=['disease','quntity']
	tabletd=[]
	for i in range(0,4):
			tabletd.append([rog[i],data[i]])
	desc="in year "+str(year+2000)+"there are minimum 4 disease are "+','.join(rog)+" of total patient "+str(sum(data))+"  in rain seson out of that :\n " 
	for i in range(0,len(rog)):
		desc=desc+"\n "+str(data[i]) +" patient of disease  "+rog[i]
	desc=linebreaksbr(desc)
	
	
	# print(data);print(rog)	
	colors = ['g', 'pink', 'y','r']
	plt.pie(data,labels=rog , autopct='%1.1f%%',radius=1.1,explode = (0, 0, 0, 0.1),
									  colors=colors)
								  
	plt.legend(bbox_to_anchor=(0.7, 1), loc=2)
	plt.title("bottom 4 Disease in rain Season")
	#plt.show()
	name='graphs/static/g3_'+str(2000+year)+'.png'
	# 
	fig.savefig(name, dpi=100)
	plt.clf()#clear privius subplots
	#plt.gcf().clear()
	nm='g3_'+str(2000+year)+'.png'
	
	# print(desc)		
	data=['bottom 4 Disease in rain Season',nm,desc,tableth,tabletd]
	print("year ",year, "graph and data is generating for rain dession lowest finish")
	return data