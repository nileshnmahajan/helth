import matplotlib.pyplot as plt
import random
fig= plt.figure(figsize=(10,10))

g1=g2=g3=g4=g5=g6=g7=g8=g9=g10=g11=g12=''

from graphs.line_year_month_male_female import male_female as g1
from graphs.male_female_pie_chart import male_female_pie as g2

from graphs.pie_top_4_rain_disease import top_4_rain as g3
from graphs.pie_bottom_4_rain_disease  import bottom_4_rain as g4

from graphs.pie_top_4_summer_disease import top_4_summer as g5
from graphs.pie_bottom_4_summer_disease import bottom_4_summer as g6

from graphs.pie_top_4_winter_disease import top_4_winter as g7
from graphs.pie_bottom_4_winter_disease import bottom_4_winter as g8

from graphs.pie_top_5_female_disease import top_5_female as g9
from graphs.pie_bottom_5_female_disease import bottom_5_female as g10

from graphs.pie_top_5_male_disease import top_5_male as g11
from graphs.pie_bottom_5_male_disease import bottom_5_male as g12
from graphs.scat1 import scatter_month as g13

def draw(year,month):	
	data=[]
	data.append(g1(year,month));
	data.append(g2(year,month));
	data.append(g3(year,month));
	data.append(g4(year,month));
	data.append(g5(year,month));
	data.append(g6(year,month));
	data.append(g7(year,month));
	data.append(g8(year,month));
	data.append(g9(year,month));
	data.append(g10(year,month));
	data.append(g11(year,month));
	data.append(g12(year,month))
	for row in g13(year,month):
		data.append(row)
	# print('recived from g ?>?>?>?>?>',data);
	# random.shuffle(data)
	return data