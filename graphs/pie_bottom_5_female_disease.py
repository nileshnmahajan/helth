#top 5 femALE DISEASE IN SELECTED CRITERIA
import matplotlib.pyplot as plt
import sqlite3 as db
from django.template.defaultfilters import linebreaksbr
from graphs.graph import fig
##fig, plt = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
def bottom_5_female(year,month):
	#LEGENDS
	print("year ",year, "graph and data is generating for female  lowest")
	#DATA OF 4
	#month basis male nd female of 1 year 

	name='data/hos_patient_data_year_'+str(year)+'.db'
	conn=db.connect(name)
	conn2=db.connect('hos_data.db')
	cur=conn.cursor()
	cur2=conn2.cursor()
	rog=[]
	data=[]
	for row in cur.execute('select dis_id,sum(female) as female from patient group by dis_id order by female asc limit 5'):
		data.append(row[1])
		q="select dname from disease where id = "+str(row[0])
		for row2 in cur2.execute(q):
			rog.append(row2[0])
	
	colors = ['g', 'pink', 'b', 'y','r']
	plt.pie(data,labels=rog , autopct='%1.1f%%',radius=1.1,explode = (0, 0, 0,0, 0.1),
									  colors=colors)

	plt.legend(bbox_to_anchor=(0.7, 1), loc=2)
	# plt.title("top 5 Disease in Female ")
	#plt.show()
	name='graphs/static/g8_'+str(2000+year)+'.png'
	# 
	fig.savefig(name, dpi=100)
	plt.clf()#clear privius subplots
	nm='g8_'+str(2000+year)+'.png'
	tableth=['disease','quntity']
	tabletd=[]
	desc="in year "+str(year+2000)+"there are lowest 5 disease are "+','.join(rog)+" of total patient "+str(sum(data))+"  in Female out of that : \n" 
	for i in range(0,len(rog)):
		desc=desc+"\n "+str(data[i]) +" patient of disease  "+rog[i]
	desc=linebreaksbr(desc)
	
	for i in range(0,5):
			tabletd.append([rog[i],data[i]])
	data=['bottom 5 Disease in Female ',nm,desc,tableth,tabletd]
	print("year ",year, "graph and data is generating for female  lowest finish")	
	return data
	