"""
Python skript lihtsa keskmistamise illustreerimiseks
Genereerib graafiku, mis näitab toor andmete ja keskmistatud andmete võrdlust
"""

import numpy as np
import matplotlib.pyplot as plt

# Seadista eesti keele tugi
plt.rcParams['font.family'] = 'DejaVu Sans'

# Genereeri simuleeritud andmed
np.random.seed(42)
n_punktid = 100

# Ideaalne signaal (sinuslaine)
x = np.linspace(0, 10, n_punktid)
ideaalne = 500 + 100 * np.sin(x)

# Toor andmed (ideaalne + müra)
müra = np.random.normal(0, 15, n_punktid)
# Lisa mõned võõrväärtused
võõrväärtused_indeksid = np.random.choice(n_punktid, 5, replace=False)
müra[võõrväärtused_indeksid] += np.random.choice([-150, 150], 5)
toor = ideaalne + müra

# Keskmistamine (lihtne libisev keskmine, aken=10)
aken = 10
keskmistatud = np.convolve(toor, np.ones(aken)/aken, mode='same')

# Loo graafik
plt.figure(figsize=(12, 6))
plt.plot(x, toor, 'o-', color='#000000', alpha=0.4, markersize=3, linewidth=1, label='Toor andmed')
plt.plot(x, keskmistatud, '-', color='#e74c3c', linewidth=2.5, label='Keskmistatud')
plt.plot(x, ideaalne, '--', color='#2ecc71', linewidth=2, label='Ideaalne signaal')

plt.xlabel('Aeg', fontsize=12)
plt.ylabel('Väärtus', fontsize=12)
plt.title('Lihtne keskmistamine - müra vähendamine', fontsize=14, fontweight='bold')
plt.legend(fontsize=11, loc='upper right')
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Salvesta pilt
plt.savefig('/mnt/user-data/outputs/graafik_keskmistamine.png', dpi=150, bbox_inches='tight')
print("Graafik salvestatud: graafik_keskmistamine.png")
plt.close()
