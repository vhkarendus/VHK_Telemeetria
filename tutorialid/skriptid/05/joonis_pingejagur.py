"""Ühendusjoonis: toiteallikas (DC-klemm) -> pingejagur 100k + 22k -> Arduino A0."""
from matplotlib.patches import FancyBboxPatch, Rectangle
from joonis_abi import uus, uno, makett, takisti, juhe, punkt

fig, ax = uus(16, 8.5)
P = uno(ax, 17.5, 4.5)
makett(ax, 5, 1.0, 9.5, 13.5)
ax.plot([5.5, 14], [1.6, 1.6], color="#2a62c9", lw=2, zorder=1); ax.text(9.75, 0.6, "GND rida (−)", color="#2a62c9", ha="center", fontsize=10)
ax.text(9.75, 14.8, "Makettplaat", ha="center", fontsize=11, color="#555")

# DC-pesa klemmiga
ax.add_patch(FancyBboxPatch((0.6, 8.5), 2.8, 3.2, boxstyle="round,pad=0.05,rounding_size=0.3", fc="#222", zorder=3))
ax.add_patch(Rectangle((0.6, 11.7), 2.8, 1.0, fc="#3c9a5f", zorder=3))
ax.text(0.9, 12.9, "−", fontsize=16, ha="center", fontweight="bold"); ax.text(3.15, 12.9, "+", fontsize=16, ha="center", fontweight="bold", color="red")
ax.text(2.0, 7.6, "DC-pesa\nklemmiga\n(toiteallikas\n3–12 V)", ha="center", va="top", fontsize=10)

R2_top, node, R1_bot = (9, 12.5), (9, 8), (9, 3.5)
takisti(ax, *R2_top, *node, ["brown", 0, "yellow", "gold"] if False else [1, 0, 4, "gold"], "R2 = 100 kΩ\n(pruun-must-kollane)")
takisti(ax, *node, *R1_bot, [2, 2, 3, "gold"], "R1 = 22 kΩ\n(punane-punane-oranž)")
punkt(ax, node)

juhe(ax, [(2.7, 12.2), (2.7, 13.8), (9, 13.8), R2_top], "red")                 # + -> R2
juhe(ax, [(1.3, 12.2), (1.3, 13.8 - 0.01), (0.3, 13.8), (0.3, 1.6), (6, 1.6)], "black")  # - -> GND rida
juhe(ax, [R1_bot, (9, 1.6)], "black")
juhe(ax, [(13.5, 1.6), (P["GND"][0], 1.6), P["GND"]], "black")                 # GND rida -> Arduino GND
juhe(ax, [node, (15.5, 8), (15.5, 2.8), (P["A0"][0], 2.8), P["A0"]], "#e6b800")  # sõlm -> A0

ax.text(15.7, 8.3, "A0", fontsize=11, fontweight="bold", color="#9a7b00")
ax.text(17.5 + 6.5, 15.2, "⚠ Klemmi + EI LÄHE otse Arduinosse!", ha="center", fontsize=11, color="red", fontweight="bold")
fig.savefig("../../images/05-pingeandur/05-pingejagur_yhendus.png", bbox_inches="tight", facecolor="white")
