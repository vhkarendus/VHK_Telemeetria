"""Joonistab SD-kaardi logifaili (07 tutorial) graafikud.
Kasutamine: python logi_graafik.py LOG000.CSV
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt

andmed = pd.read_csv(sys.argv[1] if len(sys.argv) > 1 else "LOG000.CSV")
andmed["aeg_s"] = andmed["aeg_ms"] / 1000

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 6))

ax1.plot(andmed["aeg_s"], andmed["vool_A"], color="tab:red")
ax1.set_ylabel("Vool (A)")
ax1.grid(True)

ax2.plot(andmed["aeg_s"], andmed["temp_C"], color="tab:blue")
ax2.set_ylabel("Temperatuur (°C)")
ax2.set_xlabel("Aeg (s)")
ax2.grid(True)

plt.suptitle("Telemeetria logi")
plt.tight_layout()
plt.show()
