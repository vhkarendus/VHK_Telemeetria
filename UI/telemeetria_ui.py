import streamlit as st
import csv
from bokeh.plotting import figure
from bokeh.models.tools import HoverTool
from bokeh.models import NumeralTickFormatter
import datetime


d = str(st.date_input("Mis fail? ", datetime.date(2024, 2, 1)))+".csv" # Praegu tegin nii, et saaks võrrelda eri päevade andmeid aga ilmselt oleks vaja täpsemaid aegu või lihtsalt faili nimedega
t1, t2 = st.tabs(["Koos", "Eraldi"])
t1.write("Graafikud koos")
t2.write("Graafikud eraldi")
with t1:
	#dictionary andmetega iga anduri kohta formaadis  andmed={andur:[[aeg][info]]}
	andmed = {'rpm':[[],[]],'vool':[[],[]],'pinge':[[],[]],'temp':[[],[]],'gps': [[],[]]}
	try: # try-except faili avamise/graafikute loomise jaoks
		with open(d, newline='') as f:
			read = csv.reader(f, delimiter=',', quotechar='|') # csv faili read
			for rida in read:
				andmed[rida[1]][0].append(float(rida[0]))
				andmed[rida[1]][1].append(float(rida[2]))
		#Graafiku loomine
		gr = figure(title="telemeetria - "+d,
					x_axis_label="aeg",
					y_axis_label="väärtus")
		gr.add_tools(HoverTool(tooltips=[( 'Väärtus', '@y'),( 'Aeg', '@x'),],)) # hiirega kohal hõljumine
		gr.xaxis[0].formatter = NumeralTickFormatter(format="0.00") # telgede vormistus
		gr.yaxis[0].formatter = NumeralTickFormatter(format="0.00")
		#eri graafikute sisse/välja lülitamine 
		rpm = st.toggle("RPM")
		vool = st.toggle("Voolutugevus")
		pinge = st.toggle("Pinge")
		temp = st.toggle("Temperatuur")
		gps = st.toggle("GPS")
	#andmete lisamine ja joonte näitamine
		if rpm:
			gr.line(andmed["rpm"][0],andmed["rpm"][1], legend_label="RPM", line_width=2, color="red")
		if vool:
			gr.line(andmed["vool"][0],andmed["vool"][1], legend_label="VOOLUTUGEVUS", line_width=2, color="green")
		if pinge:
			gr.line(andmed["pinge"][0],andmed["pinge"][1], legend_label="PINGE", line_width=2, color="black")
		if temp:
			gr.line(andmed["temp"][0],andmed["temp"][1], legend_label="TEMPERATUUR", line_width=2, color="blue")
		if gps:
			gr.line(andmed["gps"][0],andmed["gps"][1], legend_label="GPS", line_width=2, color="pink")
			
		st.bokeh_chart(gr, use_container_width=True) #Graafik 
	except:
		st.write("Fail puudub.")	
with t2:
	#dictionary andmetega iga anduri kohta formaadis  andmed={andur:[[aeg][info]]}
	andmed = {'rpm':[[],[]],'vool':[[],[]],'pinge':[[],[]],'temp':[[],[]],'gps': [[],[]]}
	try: # try-except faili avamise/graafikute loomise jaoks
		with open(d, newline='') as f:
			read = csv.reader(f, delimiter=',', quotechar='|') # csv faili read
			for rida in read:
				andmed[rida[1]][0].append(float(rida[0]))
				andmed[rida[1]][1].append(float(rida[2]))
		#graafikud={nimi:['ühik', 'label', 'värv']}
		graafikud = {'rpm':['RPM','RPM', 'red'],'vool':['A','Voolutugevus','green'],'pinge':['U','Pinge','black'],'temp':['°C','Temperatuur','blue'],'gps': ['gps','GPS','pink']}
		#Graafikute loomine
		for k in graafikud.keys():
			g = figure(title=graafikud[k][1]+" - "+d, x_axis_label="Aeg", y_axis_label=graafikud[k][0])
			g.add_tools(HoverTool(tooltips=[(graafikud[k][1], '@y'),( 'Aeg', '@x'),],)) # hiirega kohal hõljumine
			g.xaxis[0].formatter = NumeralTickFormatter(format="0.00") # telgede vormistus
			g.yaxis[0].formatter = NumeralTickFormatter(format="0.00")
			g.line(andmed[k][0],andmed[k][1], line_width=2, color=graafikud[k][2])
			st.bokeh_chart(g, use_container_width=True) #Graafik 
	except:
		st.write("Fail puudub.")
