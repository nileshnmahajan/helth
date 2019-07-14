#total male female in % of 1 year
import matplotlib.pyplot as plt
import csv
from django.template.defaultfilters import linebreaksbr
from graphs.graph import fig
# fig= plt.figure(figsize=(10,10))
import sqlite3 as db
def male_female_pie(year,month):
	print("year ",year, "graph and data is generating of male female ")
	name='data/hos_patient_data_year_'+str(year)+'.db'
	conn=db.connect(name)
	c=conn.cursor()
	male=0
	female=0
	activities = ['Male','Female']
	months=month-1

	
	q='select sum(male),sum(female) from patient where month < '+str(month)
	for row in c.execute(q):
			male=row[0];female=row[1]
	tableth=['gender','quntity']
	tabletd=[]
	tabletd.append([activities[0],male])
	tabletd.append([activities[1],female])
	desc="in year "+str(year+2000)+"there are  total "+str(male+female)+" \n \
	out of that male are of total "+str(male)+ "\n and female are "+str(female)+"\n\nboth male\
	and female are compared hare on total year"
	desc=linebreaksbr(desc)
		
	cols = ['pink','violet']
	slices = [male,female]
	plt.pie(slices,labels=activities,colors=cols,autopct='%1.1f%%',radius=1.1)
#	plt.title('Interesting Graph\nCheck it out')
	plt.legend(bbox_to_anchor=(0.7, 1), loc=2)
	#plt.show()
	name='graphs/static/g7_'+str(2000+year)+'.png'
	# 
	fig.savefig(name, dpi=100)
	plt.clf()#clear privius subplots
	nm='g7_'+str(2000+year)+'.png'
	# print(desc)

	
	data=['total year male female',nm,desc,tableth,tabletd]
	print("year ",year, "graph and data is generating of male female finish")
	return data