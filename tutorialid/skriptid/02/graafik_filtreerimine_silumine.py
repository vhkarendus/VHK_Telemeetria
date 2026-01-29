"""
Python skript filtreerimise ja silumise kombinatsiooni illustreerimiseks
Näitab täielikku protsessi: toor → filtreeritud → silutud
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Seadista eesti keele tugi
plt.rcParams['font.family'] = 'DejaVu Sans'

# Filtreerimise funktsioon - parandatud versioon
def filtreeri_voorvaartused(andmed, max_muutus=150):
    filtreeritud = np.zeros_like(andmed)
    filtreeritud[0] = andmed[0]
    
    for i in range(1, len(andmed)):
        muutus = abs(andmed[i] - filtreeritud[i-1])
        
        if muutus > max_muutus:
            # Võõrväärtus - kasuta eelmist väärtust
            filtreeritud[i] = filtreeritud[i-1]
        else:
            # Normaalne väärtus - kasuta seda
            filtreeritud[i] = andmed[i]
    
    return filtreeritud

# Silumise funktsioon - parandatud versioon (ei tekita servade probleeme)
def silu_andmed(andmed, aken=5):
    # Kasuta pandas rolling mean, mis käsitleb servad paremini
    df = pd.DataFrame({'väärtus': andmed})
    silutud = df['väärtus'].rolling(window=aken, center=True, min_periods=1).mean().values
    return silutud

# Genereeri simuleeritud andmed
np.random.seed(42)
n_punktid = 100

# Ideaalne signaal
x = np.linspace(0, 10, n_punktid)
ideaalne = 500 + 100 * np.sin(x * 0.8)

# Toor andmed (ideaalne + väike müra + võõrväärtused)
müra = np.random.normal(0, 12, n_punktid)

# Lisa mõned võõrväärtused (vähem ja väiksemad)
võõrväärtused_indeksid = np.random.choice(n_punktid, 5, replace=False)
# Võõrväärtused on 200-400 ühikut kõrgemal või madalamal
for idx in võõrväärtused_indeksid:
    müra[idx] += np.random.choice([-250, 250])

toor = ideaalne + müra

# Rakenda filtreerimist ja silumist
filtreeritud = filtreeri_voorvaartused(toor, max_muutus=150)
silutud = silu_andmed(filtreeritud, aken=5)

# Loo graafik (3 paneeliga)
fig, axes = plt.subplots(3, 1, figsize=(12, 10))

# Arvuta kõikide andmete vahemik dünaamiliselt
kõik_väärtused = np.concatenate([toor, filtreeritud, silutud, ideaalne])
y_min = np.min(kõik_väärtused) - 50
y_max = np.max(kõik_väärtused) + 50

# 1. Toor andmed
axes[0].plot(x, toor, 'o-', color='#000000', alpha=0.5, markersize=4, linewidth=1, label='Toor')
axes[0].plot(x, ideaalne, '--', color='#2ecc71', linewidth=2, label='Ideaalne')
axes[0].set_ylabel('Väärtus', fontsize=11)
axes[0].set_title('Samm 1: Toor andmed (müra + võõrväärtused)', fontsize=12, fontweight='bold')
axes[0].legend(fontsize=10)
axes[0].grid(True, alpha=0.3)
axes[0].set_ylim([y_min, y_max])

# 2. Filtreeritud andmed
axes[1].plot(x, toor, 'o', color='#000000', alpha=0.25, markersize=3, label='Toor')
axes[1].plot(x, filtreeritud, 'o-', color='#e74c3c', markersize=4, linewidth=1.5, label='Filtreeritud')
axes[1].plot(x, ideaalne, '--', color='#2ecc71', linewidth=2, label='Ideaalne')
axes[1].set_ylabel('Väärtus', fontsize=11)
axes[1].set_title('Samm 2: Filtreerimine - võõrväärtused eemaldatud', fontsize=12, fontweight='bold')
axes[1].legend(fontsize=10)
axes[1].grid(True, alpha=0.3)
axes[1].set_ylim([y_min, y_max])

# 3. Silutud andmed
axes[2].plot(x, toor, 'o', color='#000000', alpha=0.15, markersize=2, label='Toor')
axes[2].plot(x, filtreeritud, '-', color='#e74c3c', alpha=0.4, linewidth=1, label='Filtreeritud')
axes[2].plot(x, silutud, '-', color='#9b59b6', linewidth=2.5, label='Silutud (lõpptulemus)')
axes[2].plot(x, ideaalne, '--', color='#2ecc71', linewidth=2, label='Ideaalne')
axes[2].set_xlabel('Aeg', fontsize=11)
axes[2].set_ylabel('Väärtus', fontsize=11)
axes[2].set_title('Samm 3: Silumine - sujuv ja stabiilne signaal', fontsize=12, fontweight='bold')
axes[2].legend(fontsize=10)
axes[2].grid(True, alpha=0.3)
axes[2].set_ylim([y_min, y_max])

plt.tight_layout()

# Salvesta pilt
plt.savefig('/mnt/user-data/outputs/graafik_filtreerimine_silumine.png', dpi=150, bbox_inches='tight')
print("Graafik salvestatud: graafik_filtreerimine_silumine.png")
plt.close()

# Loo ka võrdlusgraafik (kõik ühel graafikul)
plt.figure(figsize=(12, 6))
plt.plot(x, toor, 'o', color='#000000', alpha=0.3, markersize=3, label='Toor andmed')
plt.plot(x, filtreeritud, '-', color='#e74c3c', linewidth=1.5, alpha=0.7, label='Filtreeritud')
plt.plot(x, silutud, '-', color='#9b59b6', linewidth=2.5, label='Silutud (lõpptulemus)')
plt.plot(x, ideaalne, '--', color='#2ecc71', linewidth=2, label='Ideaalne signaal')

plt.xlabel('Aeg', fontsize=12)
plt.ylabel('Väärtus', fontsize=12)
plt.title('Filtreerimine + Silumine - Täielik protsess', fontsize=14, fontweight='bold')
plt.legend(fontsize=11, loc='upper right')
plt.grid(True, alpha=0.3)
plt.ylim([y_min, y_max])
plt.tight_layout()

# Salvesta teine variant
plt.savefig('/mnt/user-data/outputs/graafik_filtreerimine_silumine_koik.png', dpi=150, bbox_inches='tight')
print("Graafik salvestatud: graafik_filtreerimine_silumine_koik.png")
plt.close()
