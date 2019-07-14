#top 5 diseases in male as selected criteria
import matplotlib.pyplot as plt
import sqlite3 as db
from django.template.defaultfilters import linebreaksbr

from graphs.graph import fig
##fig, plt = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
def bottom_5_male(year,month):
	print("year ",year, "graph and data is generating for male  lowest")
	#LEGENDS
	#DATA OF 4
	#month basis male nd female of 1 year 

	name='data/hos_patient_data_year_'+str(year)+'.db'
	conn=db.connect(name)
	conn=db.connect(name)
	conn2=db.connect('hos_data.db')
	cur=conn.cursor()
	cur2=conn2.cursor()
	rog=[]
	data=[]
	for row in cur.execute('select dis_id,sum(male) as male from patient group by dis_id order by male asc limit 5'):
		data.append(row[1])
		q="select dname from disease where id = "+str(row[0])
		# print('outer',row)
		for row2 in cur2.execute(q):
			rog.append(row2[0])
			# print('inner',row2)
	# print('checkitttttttttttttttt>>>>>>>>',rog)	

	colors = ['g', 'pink', 'b', 'y','r']
	plt.pie(data,labels=rog , autopct='%1.1f%%',radius=1.1,explode = (0, 0, 0,0, 0.1),
									  colors=colors)

	plt.legend(bbox_to_anchor=(0.7, 1), loc=2)
	plt.title("bottom 5 Disease in Male ")
	#plt.show()
	name='graphs/static/g1_'+str(2000+year)+'.png'
	
	nm='g1_'+str(2000+year)+'.png'
	tableth=['disease','quntity']
	tabletd=[]
	for i in range(0,5):
			tabletd.append([rog[i],data[i]])
	desc="in year "+str(year+2000)+"there are Bottom 5 disease in male are "+','.join(rog)+" of total patient "+str(sum(data))+"  in total year out of that : \n" 
	for i in range(0,len(rog)):
		desc=desc+"\n "+str(data[i]) +" patient of disease  "+rog[i]
	desc=linebreaksbr(desc)
	data=["bottom 5 Disease in Male ",nm,desc,tableth,tabletd]
	fig.savefig(name, dpi=100)
	plt.clf()#clear privius subplots
	print("year ",year, "graph and data is generating for male  lowest finish")
	
	return data