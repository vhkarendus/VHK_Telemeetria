import random
import csv 
from datetime import date

kp = str(date.today())# faili nime jaoks
andurid = {'rpm': 0, 'vool': 17, 'pinge': 14, 'temp': 15, 'gps': 40} #suht suvalised alguspunktid

# andmed csv reas formaadis: timestamp,andmeNimi,andmed
with open(kp+'.csv', 'w', newline='') as csvfile:
	f = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for i in range(10000):
		for j in andurid.keys():
#lihtsalt veidi erinevalt loodud andmed et ei oleks kõik graafikud testides nii sarnased
			if j == 'rpm':
				andurid[j] = round(abs(andurid[j]+random.uniform(-0.1,0.11)), 2)
				f.writerow([str(i),j,str(andurid[j])])
			if j == 'vool':
				andurid[j] = round(abs(andurid[j]+random.uniform(-0.05,0.05)), 2)
				f.writerow([str(i),j,str(andurid[j])])
			if j == 'pinge':
				andurid[j] = round(abs(andurid[j]+random.uniform(-0.05,0.05)), 2)
				f.writerow([str(i),j,str(andurid[j])])
			if j == 'temp':
				andurid[j] = round(abs(andurid[j]+random.uniform(-0.05,0.0502)), 2)
				f.writerow([str(i),j,str(andurid[j])])
			if j == 'gps':
				andurid[j] = round(abs(andurid[j]+random.uniform(-3,3)), 2)
				f.writerow([str(i),j,str(andurid[j])])
