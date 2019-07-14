#total male female in % of 1 year
import matplotlib.pyplot as plt
import csv
def male_female_pie(year):
	fo=open('hos_patient_data_year_1.csv','r')
	plots = csv.reader(fo, delimiter=',')

	male=0
	female=0
	for row in plots:
			male=male+int(row[4])
			female=female+int(row[5])
	activities = ['Male','Female']
	cols = ['c','m']
	nmale=int((male/(male+female))*100)
	nfemale=int((female/(male+female))*100)
	slices = [nmale,nfemale]
	print (slices)
	plt.pie(slices,
			labels=activities,
			colors=cols,
			startangle=90,
			shadow= True,
			autopct='%1.1f%%')

	plt.title('Interesting Graph\nCheck it out')
	plt.show()