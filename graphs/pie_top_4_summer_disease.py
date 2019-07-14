import matplotlib.pyplot as plt
import sqlite3 as db
from django.template.defaultfilters import linebreaksbr



from graphs.graph import fig
##fig, plt = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
def top_4_summer(year,month):
	print("year ",year, "graph and data is generating for summer  highest")
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
	for row in cur.execute('select dis_id,sum(male+female) as total from patient where month BETWEEN 3 AND 6 group by dis_id order by total desc limit 4'):
		data.append(row[1])
		q="select dname from disease where id = "+str(row[0])
		for row2 in cur2.execute(q):
			rog.append(row2[0])
	# print(data);print(rog)	
	colors = ['r', 'y', 'pink','g']
	plt.pie(data,labels=rog , autopct='%1.1f%%',radius=1.1,explode = (0.1, 0, 0, 0),
									  colors=colors)

	plt.legend(bbox_to_anchor=(0.7, 1), loc=2)
	plt.title("top 4 Disease in summer Season ")
	#plt.show()
	name='graphs/static/g10_'+str(2000+year)+'.png'
	# 
	fig.savefig(name, dpi=100)
	plt.clf()#clear privius subplots
	nm='g10_'+str(2000+year)+'.png'
	tableth=['disease','quntity']
	tabletd=[]
	desc="in year "+str(year+2000)+"there are highest 4 disease are "+','.join(rog)+" of total patient "+str(sum(data))+"  in summer seson out of that : \n" 
	for i in range(0,len(rog)):
		desc=desc+"\n "+str(data[i]) +" patient of disease  "+rog[i]
	desc=linebreaksbr(desc)

	for i in range(0,4):
			tabletd.append([rog[i],data[i]])
	data=['top 4 Disease in summer Season',nm,desc,tableth,tabletd]
	print("year ",year, "graph and data is generating for summer  highest finish")
	return data