import matplotlib.pyplot as plt
import sqlite3 as db
from graphs.graph import fig
from hospital.views import int_to_month as to_month
from hospital.views import get_year,get_month
from django.template.defaultfilters import linebreaksbr
def scatter_month(year,month): 

	name='data/hos_patient_data_year_'+str(year)+'.db'
	conn=db.connect(name)
	conn2=db.connect('hos_data.db')
	cur=conn.cursor()
	cur2=conn2.cursor()
	data=[]
	index=0
	
	if(int(get_year())==year):
		months=range(1,month-1)
		cur_year=int(get_year())
	else:
		months=range(1,13)
	for i in range(0,months[len(months)-1]):
		data.append(i-1)
	for i in range(0,months[len(months)-1]):
		data.append(i-1)	
	print("year ",year, "graph and data is generating of top diseases")

		
	for month in months:

		order=['desc','asc']
		asign=['top','bottom']
		Col=['red','green']
		for kk in range(0,2):
			rog=[]
			quntity=[]
			q='select dis_id,sum(male+female) as total from patient where month='+str(month)+' group by dis_id order by total '+order[kk]+' limit 10'
			for row in cur.execute(q):
				quntity.append(row[1])
				q="select dname from disease where id = "+str(row[0])
				for row2 in cur2.execute(q):
					rog.append(row2[0])
			#print(quntity);print(rog)	
			plt.scatter(rog, quntity, label= "total(male,female)", color= Col[kk], marker='*', s=60) 
			plt.xlabel('Top 10 diseases')
			plt.ylabel('Quantity')
			plt.xticks(rotation=20)
			#plt.title('scatter graph of top 10 diseases')
			plt.legend()
			#plt.show()
			name='graphs/static/g13_'+asign[kk]+'_'+str(month)+'_'+str(2000+year)+'.png'
			# 
			fig.savefig(name, dpi=100)
			plt.clf()#clear privius subplots
			nm='g13_'+asign[kk]+'_'+str(month)+'_'+str(2000+year)+'.png'
			title=asign[kk]+' 10 Disease in  '+str(to_month(month)) +' '+str(year+2000)
			tableth=['disease','quntity']
			tabletd=[]
			for i in range(0,10):
				tabletd.append([rog[i],quntity[i]]) 
			desc="in year "+str(year+2000)+"there are "+asign[kk]+" 10 disease in  "+to_month(month)+" month  are "+','.join(rog)+" of total patient "+str(sum(quntity))+"  in total year out of that : \n" 
			for i in range(0,len(rog)):
				desc=desc+"\n "+str(quntity[i]) +" patient of disease  "+rog[i]
			desc=linebreaksbr(desc)
			data[index]=[title,nm,desc,tableth,tabletd]
			index=index+1
	print("year ",year, "graph and data is generating of top diseases finish")
	return data
