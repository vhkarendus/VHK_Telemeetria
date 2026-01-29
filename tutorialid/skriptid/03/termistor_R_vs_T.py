"""
Termistori R vs T graafik
Näitab NTC termistori mittelineaarset käitumist
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'DejaVu Sans'

# Parameetrid 10kΩ NTC termistorile
R0 = 10000  # 10kΩ @ 25°C
T0 = 298.15  # 25°C Kelvinites
B = 3950    # Beta väärtus

# Temperatuurivahemik
temp_C = np.linspace(-20, 100, 200)
temp_K = temp_C + 273.15

# Arvuta takistus B-võrrandiga
# R = R0 × exp(B × (1/T - 1/T0))
R = R0 * np.exp(B * (1/temp_K - 1/T0))

# Loo graafik
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Vasak graafik - R vs T (lineaarskaalal)
ax1.plot(temp_C, R/1000, 'b-', linewidth=2.5)
ax1.axhline(y=R0/1000, color='r', linestyle='--', linewidth=1.5, label=f'R₀ = {R0/1000}kΩ @ 25°C')
ax1.axvline(x=25, color='r', linestyle='--', linewidth=1.5, alpha=0.5)
ax1.grid(True, alpha=0.3)
ax1.set_xlabel('Temperatuur (°C)', fontsize=12)
ax1.set_ylabel('Takistus (kΩ)', fontsize=12)
ax1.set_title('NTC Termistori käitumine (lineaar)', fontsize=13, fontweight='bold')
ax1.legend(fontsize=10)

# Märgi tähtsad punktid
ax1.plot(0, R[np.argmin(np.abs(temp_C - 0))]/1000, 'go', markersize=10)
ax1.text(0, R[np.argmin(np.abs(temp_C - 0))]/1000 + 5, '0°C', ha='center', fontsize=9)
ax1.plot(25, 10, 'ro', markersize=10)
ax1.text(25, 15, '25°C', ha='center', fontsize=9)
ax1.plot(50, R[np.argmin(np.abs(temp_C - 50))]/1000, 'mo', markersize=10)
ax1.text(50, R[np.argmin(np.abs(temp_C - 50))]/1000 + 3, '50°C', ha='center', fontsize=9)

# Parem graafik - Log skaalal
ax2.semilogy(temp_C, R, 'b-', linewidth=2.5)
ax2.axhline(y=R0, color='r', linestyle='--', linewidth=1.5, label=f'R₀ = {R0}Ω @ 25°C')
ax2.axvline(x=25, color='r', linestyle='--', linewidth=1.5, alpha=0.5)
ax2.grid(True, alpha=0.3, which='both')
ax2.set_xlabel('Temperatuur (°C)', fontsize=12)
ax2.set_ylabel('Takistus (Ω, log skaala)', fontsize=12)
ax2.set_title('NTC Termistori käitumine (log)', fontsize=13, fontweight='bold')
ax2.legend(fontsize=10)

# Lisainfo tekstina
info_text = f'Parameetrid:\nR₀ = {R0/1000}kΩ\nB = {B}K\nT₀ = 25°C'
ax1.text(0.98, 0.97, info_text, transform=ax1.transAxes, 
         fontsize=9, verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/termistor_R_vs_T.png', dpi=150, bbox_inches='tight')
print("Graafik salvestatud: termistor_R_vs_T.png")
plt.close()

# Loo ka tabel näidis väärtustega
print("\nNäidis väärtused:")
print("Temp (°C)\tTakistus (kΩ)")
for t in [0, 10, 20, 25, 30, 40, 50, 75, 100]:
    t_k = t + 273.15
    r = R0 * np.exp(B * (1/t_k - 1/T0))
    print(f"{t}\t\t{r/1000:.2f}")
