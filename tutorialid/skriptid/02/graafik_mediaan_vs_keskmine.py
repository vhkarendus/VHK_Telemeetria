"""
Python skript mediaani ja keskmise võrdluse illustreerimiseks
Näitab, kuidas mediaan võõrväärtustega paremini toime tuleb
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import median_filter

# Seadista eesti keele tugi
plt.rcParams['font.family'] = 'DejaVu Sans'

# Genereeri simuleeritud andmed
np.random.seed(42)
n_punktid = 100

# Ideaalne signaal
x = np.linspace(0, 10, n_punktid)
ideaalne = 500 + 120 * np.sin(x)

# Toor andmed (ideaalne + müra + võõrväärtused)
müra = np.random.normal(0, 12, n_punktid)
# Lisa rohkem võõrväärtusi
võõrväärtused_indeksid = np.random.choice(n_punktid, 10, replace=False)
müra[võõrväärtused_indeksid] += np.random.choice([-250, 250], 10)
toor = ideaalne + müra

# Lihtne keskmistamine (aken=5)
aken = 5
keskmine = np.convolve(toor, np.ones(aken)/aken, mode='same')

# Mediaanfiltreerimine (aken=5)
mediaan = median_filter(toor, size=aken)

# Loo graafik
plt.figure(figsize=(12, 7))

# Ülemine graafik - kõik koos
plt.subplot(2, 1, 1)
plt.plot(x, toor, 'o', color='#000000', alpha=0.4, markersize=4, label='Toor andmed (koos võõrväärtustega)')
plt.plot(x, keskmine, '-', color='#e74c3c', linewidth=2, label='Lihtne keskmine')
plt.plot(x, mediaan, '-', color='#27ae60', linewidth=2.5, label='Mediaan')
plt.plot(x, ideaalne, '--', color='#3498db', linewidth=2, label='Ideaalne signaal')
plt.ylabel('Väärtus', fontsize=11)
plt.title('Mediaan vs Keskmine - Võõrväärtuste mõju', fontsize=14, fontweight='bold')
plt.legend(fontsize=10, loc='upper right')
plt.grid(True, alpha=0.3)

# Alumine graafik - vea võrdlus
plt.subplot(2, 1, 2)
viga_keskmine = np.abs(keskmine - ideaalne)
viga_mediaan = np.abs(mediaan - ideaalne)
plt.plot(x, viga_keskmine, '-', color='#e74c3c', linewidth=2, label='Keskmine viga')
plt.plot(x, viga_mediaan, '-', color='#27ae60', linewidth=2, label='Mediaani viga')
plt.xlabel('Aeg', fontsize=11)
plt.ylabel('Absoluutne viga', fontsize=11)
plt.title('Vea võrdlus (väiksem on parem)', fontsize=12, fontweight='bold')
plt.legend(fontsize=10, loc='upper right')
plt.grid(True, alpha=0.3)

plt.tight_layout()

# Salvesta pilt
plt.savefig('/mnt/user-data/outputs/graafik_mediaan_vs_keskmine.png', dpi=150, bbox_inches='tight')
print("Graafik salvestatud: graafik_mediaan_vs_keskmine.png")
plt.close()
