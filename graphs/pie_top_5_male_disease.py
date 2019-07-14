#top 5 diseases in male as selected criteria
import matplotlib.pyplot as plt
import sqlite3 as db
from django.template.defaultfilters import linebreaksbr

from graphs.graph import fig
def top_5_male(year,month):
	print("year ",year, "graph and data is generating for male 5  highest")
	#LEGENDS

	#DATA OF 4
	#month basis male nd female of 1 year 

	name='data/hos_patient_data_year_'+str(year)+'.db'
	conn=db.connect(name)
	conn2=db.connect('hos_data.db')
	cur=conn.cursor()
	cur2=conn2.cursor()
	rog=[]
	data=[]
	for row in cur.execute('select dis_id,sum(male) as male from patient group by dis_id order by male desc limit 5'):
		data.append(row[1])
		q="select dname from disease where id = "+str(row[0])
		for row2 in cur2.execute(q):
			rog.append(row2[0])
	

	# print(data);print(rog)	
	colors = ['r', 'y', 'b', 'pink','g']
	plt.pie(data,labels=rog , autopct='%1.1f%%',radius=1.1,explode = (0.1, 0, 0,0, 0),
									  colors=colors)

	plt.legend(bbox_to_anchor=(0.7, 1), loc=2 )
	# plt.title("top 5 Disease in Male ")
	#plt.show()
	name='graphs/static/g6_'+str(2000+year)+'.png'
	# 
	fig.savefig(name, dpi=100)
	plt.clf()#clear privius subplots
	nm='g6_'+str(2000+year)+'.png'
	tableth=['disease','quntity']
	tabletd=[]
	desc="in year "+str(year+2000)+"there are top 5 male disease are "+','.join(rog)+" of total patient "+str(sum(data))+"  in total year  out of that : \n" 
	for i in range(0,len(rog)):
		desc=desc+"\n "+str(data[i]) +" patient of disease  "+rog[i]
	desc=linebreaksbr(desc)
	for i in range(0,5):
			tabletd.append([rog[i],data[i]])
	data=['top 5 Disease in Male ',nm,desc,tableth,tabletd]
	print("year ",year, "graph and data is generating for male 5  highest finish")

	return data
	
	