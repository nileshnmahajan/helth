import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
def draw_pie2(parameters):
	#LEGENDS
	recipe = ["375 g d1",
			  "75 g d2",
			  "250 g d3",
			  "400 g d4"]
	#DATA OF 4
	data = [float(x.split()[0]) for x in recipe]
	ingredients = [x.split()[-1] for x in recipe]

	
	def func(pct, allvals):
		absolute = int(pct/100.*np.sum(allvals))
		return "{:.1f}%\n({:d} g)".format(pct, absolute)


	wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
									  textprops=dict(color="w"))

	ax.legend(wedges, ingredients,
			  title="Ingredients",
			  loc="center left",
			  bbox_to_anchor=(1, 0, 0.5, 1))

	plt.setp(autotexts, size=8, weight="bold")

	ax.set_title("top 4 of month")
	fig.savefig('graphs/static/pie.png')
	#plt.show()