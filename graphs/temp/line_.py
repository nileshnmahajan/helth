#month basis male nd female of 1 year 
import matplotlib.pyplot as plt
import csv
fo=open('hos_patient_data_year_1.csv', 'r')
plots= csv.reader(fo, delimiter=',')
data=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
count=0
#for i in plots:
for row in fo:
	i=row.replace('\n','')
	i=i.split(',')
	count=count+1
	data[(int(i[1])-1)][0]=data[(int(i[1])-1)][0]+int(i[4])
	data[(int(i[1])-1)][1]=data[(int(i[1])-1)][1]+int(i[5])
	print(count)
	if(int(i[1])==4):
		break
print(data)
x=[]
y=[]
for r in data:
	x.append(r[0])
	y.append(r[1])
	base=[1,2,3,4,5,6,7,8,9,10,11,12]
# multiple line plot
plt.plot( base, x,  marker='', color='olive', linewidth=2,label='male')
plt.plot( base, y, marker='', color='red', linewidth=4, linestyle='dashed', label="female")
plt.legend()
plt.show()