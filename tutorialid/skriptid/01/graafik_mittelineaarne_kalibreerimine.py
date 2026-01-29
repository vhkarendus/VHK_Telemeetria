"""
Python skript mittelineaarse kalibreerimise illustreerimiseks
Näitab NTC termistori (mittelineaarne) ja lineaarse anduri võrdlust
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit

# Seadista eesti keele tugi
plt.rcParams['font.family'] = 'DejaVu Sans'

# === LINEAARNE ANDUR (näide: TMP36) ===
arduino_linear = np.array([147, 204, 261, 317, 374, 430, 487])
temp_linear = np.array([0, 10, 20, 30, 40, 50, 60])

slope_lin, intercept_lin, _, _, _ = stats.linregress(arduino_linear, temp_linear)
x_lin_fit = np.linspace(100, 550, 100)
y_lin_fit = slope_lin * x_lin_fit + intercept_lin

# === MITTELINEAARNE ANDUR (näide: NTC termistor) ===
# Simuleeritud NTC termistori andmed (logaritmiline seos)
arduino_ntc = np.array([850, 720, 580, 450, 340, 250, 180])
temp_ntc = np.array([0, 10, 20, 30, 40, 50, 60])

# Logaritmiline sobitusfunktsioon
def logarithmic_func(x, a, b):
    return a * np.log(x) + b

# Sobita logaritmiline funktsioon
params_ntc, _ = curve_fit(logarithmic_func, arduino_ntc, temp_ntc)
x_ntc_fit = np.linspace(150, 900, 100)
y_ntc_fit = logarithmic_func(x_ntc_fit, *params_ntc)

# Proovi sobida lineaarset funktsiooni NTC andmetele (näitamaks halba sobivust)
slope_ntc_wrong, intercept_ntc_wrong, _, _, _ = stats.linregress(arduino_ntc, temp_ntc)
y_ntc_linear_wrong = slope_ntc_wrong * x_ntc_fit + intercept_ntc_wrong

# Loo graafikud
fig = plt.figure(figsize=(14, 10))

# === ÜLEMINE RIDA - LINEAARNE ANDUR ===
ax1 = plt.subplot(2, 2, 1)
ax1.scatter(arduino_linear, temp_linear, color='#e74c3c', s=100, 
            label='Mõõtmised', zorder=3, edgecolors='black', linewidth=1.5)
ax1.plot(x_lin_fit, y_lin_fit, 'b-', linewidth=2.5, label='Lineaarne sobitus')
ax1.grid(True, alpha=0.3)
ax1.set_xlabel('Arduino väärtus', fontsize=11)
ax1.set_ylabel('Temperatuur (°C)', fontsize=11)
ax1.set_title('A) Lineaarne andur (TMP36)', fontsize=12, fontweight='bold')
ax1.legend(fontsize=9)
ax1.text(0.05, 0.95, f'y = {slope_lin:.4f}x + {intercept_lin:.2f}', 
         transform=ax1.transAxes, fontsize=9, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

ax2 = plt.subplot(2, 2, 2)
ax2.axis('off')
ax2.text(0.1, 0.85, '✓ LINEAARNE ANDUR', fontsize=13, fontweight='bold', color='green')
ax2.text(0.15, 0.72, '• Seos on sirgjooneline', fontsize=10)
ax2.text(0.15, 0.63, '• Kasutatakse lihtsat valemit:', fontsize=10)
ax2.text(0.20, 0.54, 'y = ax + b', fontsize=11, family='monospace',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
ax2.text(0.15, 0.42, '• Hea täpsus kogu vahemikus', fontsize=10)
ax2.text(0.15, 0.33, '• Lihtne kalibreerimiseks', fontsize=10)
ax2.text(0.1, 0.18, 'Näited:', fontsize=11, fontweight='bold')
ax2.text(0.15, 0.09, '• TMP36, LM35 (temperatuur)', fontsize=9)
ax2.text(0.15, 0.03, '• HC-SR04 (kaugus)', fontsize=9)
ax2.text(0.15, -0.03, '• Pinge-pingestaja andurid', fontsize=9)

# === ALUMINE RIDA - MITTELINEAARNE ANDUR ===
ax3 = plt.subplot(2, 2, 3)
ax3.scatter(arduino_ntc, temp_ntc, color='#e74c3c', s=100, 
            label='Mõõtmised', zorder=3, edgecolors='black', linewidth=1.5)
ax3.plot(x_ntc_fit, y_ntc_fit, 'g-', linewidth=2.5, label='Logaritmiline sobitus (õige)')
ax3.plot(x_ntc_fit, y_ntc_linear_wrong, 'r--', linewidth=2, alpha=0.6, 
         label='Lineaarne sobitus (vale!)')
ax3.grid(True, alpha=0.3)
ax3.set_xlabel('Arduino väärtus', fontsize=11)
ax3.set_ylabel('Temperatuur (°C)', fontsize=11)
ax3.set_title('B) Mittelineaarne andur (NTC termistor)', fontsize=12, fontweight='bold')
ax3.legend(fontsize=9)
ax3.text(0.05, 0.95, f'y = {params_ntc[0]:.2f}·ln(x) + {params_ntc[1]:.2f}', 
         transform=ax3.transAxes, fontsize=9, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))

ax4 = plt.subplot(2, 2, 4)
ax4.axis('off')
ax4.text(0.1, 0.85, '⚠ MITTELINEAARNE ANDUR', fontsize=13, fontweight='bold', color='orange')
ax4.text(0.15, 0.72, '• Seos EI OLE sirgjooneline', fontsize=10)
ax4.text(0.15, 0.63, '• Vajab keerukamat valemit:', fontsize=10)
ax4.text(0.20, 0.54, 'y = a·ln(x) + b  (logaritmiline)', fontsize=10, family='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
ax4.text(0.20, 0.44, 'või y = a·x² + b·x + c  (ruutfunktsioon)', fontsize=9, family='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
ax4.text(0.15, 0.31, '• Lineaarne valem annab VIGU!', fontsize=10, color='red')
ax4.text(0.15, 0.22, '• Keerulisem kalibreerimiseks', fontsize=10)
ax4.text(0.1, 0.10, 'Näited:', fontsize=11, fontweight='bold')
ax4.text(0.15, 0.01, '• NTC termistor (temperatuur)', fontsize=9)
ax4.text(0.15, -0.05, '• LDR (valgus)', fontsize=9)
ax4.text(0.15, -0.11, '• pH sensor', fontsize=9)

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/graafik_mittelineaarne_kalibreerimine.png', dpi=150, bbox_inches='tight')
print("Graafik salvestatud: graafik_mittelineaarne_kalibreerimine.png")
plt.close()
