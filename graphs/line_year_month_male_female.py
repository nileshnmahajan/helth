#month basis male nd female of 1 year 
import matplotlib.pyplot as plt
import csv
import sqlite3 as db
from graphs.graph import fig
from random import randint
from hospital.views import int_to_month
#fig2, ax = plt.subplots()
#fig=plt.figure()
from hospital.views import get_year,get_month
from django.template.defaultfilters import linebreaksbr
def int_to_month(m):
	months=['jan','feb','mar','apr','may','jun','jul','aug','sup','oct','nov','dec']
	count=1
	for mm in months:
		if(count==m):
			return mm
		count=count+1
def male_female(year,month):
	print("year ",year, "graph and data is generating of male female per month")
	name='data/hos_patient_data_year_'+str(year)+'.db'
	conn=db.connect(name)
	cur=conn.cursor()
	if(int(get_year())==year):
		months=range(1,month-1)
		cur_year=int(get_year())
	else:
		months=range(1,13)
	
	male=[];female=[];	base=[]
	
	for i in months:
		male.append(0)
		female.append(0)
		base.append(int_to_month(i))
	for month in months:
		q='select sum(male),sum(female) from patient where month = '+str(month)
		for row in cur.execute(q):
			male[month-1]=male[month-1]+row[0]
			female[month-1]=female[month-1]+row[1]
	
	

	plt.plot( base, male,  marker='*', color='red', linewidth=1,label='male')
	plt.plot( base, female, marker='*', color='green', linewidth=1, label="female")
	xlbl='Months of year '+str(2000+year)
	plt.xlabel(xlbl)
	plt.ylabel('Quantity')
	plt.legend(bbox_to_anchor=(0.7, 1), loc=2)		   
	name='graphs/static/g2_'+str(2000+year)+'.png'
	fig.savefig(name, dpi=100)
	plt.clf()#clear privius subplots
	nm='g2_'+str(2000+year)+'.png'
	tableth=['month','male','female']
	tabletd=[]
	
	for i in months:
			tabletd.append([base[i-1],male[i-1],female[i-1]])
	desc="in year "+str(year+2000)+"there are  total "+str(sum(male+female))+" and out of that male are of total "+str(sum(male))+ "and female are "+str(sum(female))+"both male and female are compared hare on the month basis as shown in graph and table as"
	Max=0
	max_month=0
	for month in months:
		if(Max<(male[month-1]+female[month-1])):
			Max=male[month-1]+female[month-1]
			max_month=month
	
	Min=Max
	min_month=0
	for month in months:
		if(Min>male[month-1]+female[month-1]):
			Min=male[month-1]+female[month-1]
			min_month=month
	desc=linebreaksbr(desc)
	data=['total year male female month',nm,desc,tableth,tabletd]
	print("year ",year, "graph and data is generating of male female Finish")
	return data
	