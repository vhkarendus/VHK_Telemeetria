import streamlit as st
import csv
from bokeh.plotting import figure
from bokeh.models.tools import HoverTool
from bokeh.models import NumeralTickFormatter
import datetime

#input rida => data_num, millis, temperature_C_ta, temperature_C_tm, rpm, current, battery_1_v, battery_2_v


d = str(st.date_input("Mis fail? ", datetime.date(2024, 2, 1)))+".csv" # Praegu tegin nii, et saaks võrrelda eri päevade andmeid aga ilmselt oleks vaja täpsemaid aegu või lihtsalt faili nimedega
t1, t2 = st.tabs(["Koos", "Eraldi"])
t1.write("Graafikud koos")
t2.write("Graafikud eraldi")


with t1:
	#dictionary andmetega iga anduri kohta formaadis  andmed={andur:[[aeg][info]]}
	andmed = {'akuT':[[],[]],'mootorT':[[],[]],'rpm':[[],[]],'vool':[[],[]],'aku1Pinge': [[],[]],'aku2Pinge': [[],[]]}
	try: # try-except faili avamise/graafikute loomise jaoks
		with open(d, newline='') as f:
			read = csv.reader(f, delimiter=',', quotechar='|') # csv faili read
			for rida in read:
				andmed['akuT'][0].append(float(rida[0]))
				andmed['akuT'][1].append(float(rida[2]))
				andmed['mootorT'][0].append(float(rida[0]))
				andmed['mootorT'][1].append(float(rida[3]))
				andmed['rpm'][0].append(float(rida[0]))
				andmed['rpm'][1].append(float(rida[4]))
				andmed['vool'][0].append(float(rida[0]))
				andmed['vool'][1].append(float(rida[5]))
				andmed['aku1Pinge'][0].append(float(rida[0]))
				andmed['aku1Pinge'][1].append(float(rida[6]))
				andmed['aku2Pinge'][0].append(float(rida[0]))
				andmed['aku2Pinge'][1].append(float(rida[7]))
		
		#Graafiku loomine
		gr = figure(title="telemeetria - "+d,
					x_axis_label="aeg",
					y_axis_label="väärtus")
		gr.add_tools(HoverTool(tooltips=[( 'Väärtus', '@y'),( 'Aeg', '@x'),],)) # hiirega kohal hõljumine
		gr.xaxis[0].formatter = NumeralTickFormatter(format="0.00") # telgede vormistus
		gr.yaxis[0].formatter = NumeralTickFormatter(format="0.00")
	#andmete lisamine ja joonte näitamine
		#graafikud={nimi:['ühik', 'label', 'värv']}
		graafikud = {'akuT':['°C','Aku temperatuur', 'red', st.toggle("Aku temperatuur")],'mootorT':['°C','Mootori temperatuur','green', st.toggle("Mootori temperatuur")],'rpm':['RPM','RPM','black', st.toggle("RPM")],'vool':['A','Voolutugevus','blue', st.toggle("Voolutugevus")],'aku1Pinge': ['V','Aku 1 pinge','pink', st.toggle("Aku 1 pinge")], 'aku2Pinge': ['V','Aku 2 pinge','orange', st.toggle("Aku 2 pinge")]}
		#Graafikute loomineu
		for k in graafikud.keys():
			if graafikud[k][3]:
				gr.line(andmed[k][0],andmed[k][1], line_width=2, legend_label=graafikud[k][1]+"("+graafikud[k][0]+")", color=graafikud[k][2])	
		st.bokeh_chart(gr, use_container_width=True) #Graafik 
	except:
		st.write("Fail puudub.")	
with t2:
	#dictionary andmetega iga anduri kohta formaadis  andmed={andur:[[aeg][info]]}
	andmed = {'akuT':[[],[]],'mootorT':[[],[]],'rpm':[[],[]],'vool':[[],[]],'aku1Pinge': [[],[]],'aku2Pinge': [[],[]]}
	try: # try-except faili avamise/graafikute loomise jaoks
		with open(d, newline='') as f:
			read = csv.reader(f, delimiter=',', quotechar='|') # csv faili read
			for rida in read:
				andmed['akuT'][0].append(float(rida[0]))
				andmed['akuT'][1].append(float(rida[2]))
				andmed['mootorT'][0].append(float(rida[0]))
				andmed['mootorT'][1].append(float(rida[3]))
				andmed['rpm'][0].append(float(rida[0]))
				andmed['rpm'][1].append(float(rida[4]))
				andmed['vool'][0].append(float(rida[0]))
				andmed['vool'][1].append(float(rida[5]))
				andmed['aku1Pinge'][0].append(float(rida[0]))
				andmed['aku1Pinge'][1].append(float(rida[6]))
				andmed['aku2Pinge'][0].append(float(rida[0]))
				andmed['aku2Pinge'][1].append(float(rida[7]))
		for k in graafikud.keys():
			g = figure(title=graafikud[k][1]+" - "+d, x_axis_label="Aeg", y_axis_label=graafikud[k][0])
			g.add_tools(HoverTool(tooltips=[(graafikud[k][1], '@y'),( 'Aeg', '@x'),],)) # hiirega kohal hõljumine
			g.xaxis[0].formatter = NumeralTickFormatter(format="0.00") # telgede vormistus
			g.yaxis[0].formatter = NumeralTickFormatter(format="0.00")
			g.line(andmed[k][0],andmed[k][1], line_width=2, color=graafikud[k][2])
			st.bokeh_chart(g, use_container_width=True) #Graafik 
	except:
		st.write("Fail puudub.")
