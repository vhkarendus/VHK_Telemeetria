"""
Python skript lineaarse kalibreerimise illustreerimiseks
Näitab temperatuurianduri kalibreerimist
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Seadista eesti keele tugi
plt.rcParams['font.family'] = 'DejaVu Sans'

# Kalibreerimise andmed (Arduino lugemised vs tegelik temperatuur)
# Näiteks TMP36 anduriga
arduino_vaartused = np.array([147, 204, 261, 317, 374, 430, 487])  # analogRead väärtused
tegelik_temp = np.array([0, 10, 20, 30, 40, 50, 60])  # °C (mõõdetud kalibreerimisega)

# Arvuta lineaarne regressioon (leia sirge parameetrid)
slope, intercept, r_value, p_value, std_err = stats.linregress(arduino_vaartused, tegelik_temp)

# a = slope (tõus, lineaarliige)
# b = intercept (y-teljeläbilõige, vabaliige)
a = slope
b = intercept

# Loo sirge joonis
x_line = np.linspace(100, 550, 100)
y_line = a * x_line + b

# Loo graafik
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Vasak graafik - kalibreerimise punktid ja sirge
ax1.scatter(arduino_vaartused, tegelik_temp, color='#e74c3c', s=100, 
            label='Kalibreerimise punktid', zorder=3, edgecolors='black', linewidth=1.5)
ax1.plot(x_line, y_line, 'b-', linewidth=2.5, label=f'Sirge: y = {a:.4f}x + {b:.2f}')
ax1.grid(True, alpha=0.3)
ax1.set_xlabel('Arduino väärtus (analogRead)', fontsize=12)
ax1.set_ylabel('Temperatuur (°C)', fontsize=12)
ax1.set_title('Lineaarne kalibreerimine - Temperatuuriandur', fontsize=13, fontweight='bold')
ax1.legend(fontsize=10)

# Lisa tekst parameetrite kohta
textstr = f'Lineaarliige (a) = {a:.4f}\nVabaliige (b) = {b:.2f}\nKorrelatsiooni R² = {r_value**2:.4f}'
ax1.text(0.05, 0.95, textstr, transform=ax1.transAxes, fontsize=10,
         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Parem graafik - selgitus parameetrite kohta
ax2.axis('off')
ax2.text(0.1, 0.9, 'Lineaarse kalibreerimise valem:', fontsize=14, fontweight='bold')
ax2.text(0.1, 0.75, 'y = ax + b', fontsize=16, family='monospace', 
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

ax2.text(0.1, 0.60, 'Kus:', fontsize=12, fontweight='bold')
ax2.text(0.15, 0.52, '• y = tegelik väärtus (nt temperatuur °C)', fontsize=11)
ax2.text(0.15, 0.45, '• x = anduri väärtus (analogRead)', fontsize=11)
ax2.text(0.15, 0.38, f'• a = lineaarliige (tõus) = {a:.4f}', fontsize=11, color='blue')
ax2.text(0.15, 0.31, f'• b = vabaliige (algväärtus) = {b:.2f}', fontsize=11, color='blue')

ax2.text(0.1, 0.18, 'Kuidas kasutada:', fontsize=12, fontweight='bold')
ax2.text(0.15, 0.10, '1. Mõõda mitmel tuntud temperatuuril', fontsize=10)
ax2.text(0.15, 0.04, '2. Arvuta a ja b (või kasuta joonistust)', fontsize=10)
ax2.text(0.15, -0.02, '3. Kasuta valemit: temp = a × analogRead + b', fontsize=10)

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/graafik_lineaarne_kalibreerimine.png', dpi=150, bbox_inches='tight')
print("Graafik salvestatud: graafik_lineaarne_kalibreerimine.png")
plt.close()
