"""Ühendusjoonis: MicroSD moodul + termistori pingejagur (A2) Arduino Unoga."""
from matplotlib.patches import FancyBboxPatch, Rectangle
from joonis_abi import uus, uno, makett, takisti, juhe, punkt

fig, ax = uus(17, 12)
P = uno(ax, 18, 2.5)
makett(ax, 1.5, 1.0, 11, 15)
ax.text(7, 16.5, "Makettplaat", ha="center", fontsize=11, color="#555")
PLUS_Y, MIN_Y = 15.2, 1.8
ax.plot([2, 12], [PLUS_Y, PLUS_Y], color="red", lw=2, zorder=1); ax.text(7, 15.6, "5V rida (+)", color="red", ha="center", fontsize=10)
ax.plot([2, 12], [MIN_Y, MIN_Y], color="#2a62c9", lw=2, zorder=1); ax.text(7, 0.5, "GND rida (−)", color="#2a62c9", ha="center", fontsize=10)

# Termistori pingejagur: 5V -> NTC -> A2 -> 10k -> GND
top, node, bot = (6, 13), (6, 8.5), (6, 4)
juhe(ax, [(6, PLUS_Y), top], "red")
takisti(ax, *top, *node, [], "NTC termistor\n10 kΩ", fc="#333333")
takisti(ax, *node, *bot, [1, 0, 3, "gold"], "10 kΩ\n(pruun-must-oranž)")
juhe(ax, [bot, (6, MIN_Y)], "black")
punkt(ax, node)
juhe(ax, [node, (15.8, 8.5), (15.8, 4.6), (P["A2"][0] + 0.25, 4.6), (P["A2"][0] + 0.25, 3.2), P["A2"]], "#e6b800")
ax.text(14.6, 8.8, "A2", fontsize=11, fontweight="bold", color="#9a7b00")

# Arduino toide rididele
juhe(ax, [P["5V"], (P["5V"][0], 0.3), (0.7, 0.3), (0.7, PLUS_Y), (2.5, PLUS_Y)], "red")
juhe(ax, [P["GND"], (P["GND"][0], 1.0), (13.5, 1.0), (13.5, MIN_Y), (11.5, MIN_Y)], "black")

# SD moodul
sx, sy, sw, sh = 19.5, 15.5, 9.5, 6.0
ax.add_patch(FancyBboxPatch((sx, sy), sw, sh, boxstyle="round,pad=0.05,rounding_size=0.3", fc="#1f4fa8", ec="#123", lw=2, zorder=2))
ax.add_patch(Rectangle((sx + 2.2, sy + 2.4), 5, 3.2, fc="#bfbfbf", ec="#666", zorder=3))
ax.text(sx + 4.7, sy + 4.0, "MicroSD\nkaardipesa", ha="center", va="center", fontsize=9, zorder=4)
names = ["GND", "VCC", "MISO", "MOSI", "SCK", "CS"]
SD = {}
for i, n in enumerate(names):
    x = sx + 1.6 + i * 1.3; y = sy + 0.4
    ax.add_patch(Rectangle((x - 0.2, y - 0.2), 0.4, 0.4, fc="#222", zorder=4))
    ax.text(x, y + 0.45, n, rotation=90, ha="center", va="bottom", fontsize=8, color="white", zorder=4)
    SD[n] = (x, y)

juhe(ax, [SD["GND"], (SD["GND"][0], 14.6), (P["GND_top"][0], 14.6), P["GND_top"]], "black")
juhe(ax, [SD["VCC"], (SD["VCC"][0], 15.2), (11.5, 15.2)], "red")
col = {"MISO": "#2e9e3e", "MOSI": "#8e44ad", "SCK": "#e67e22", "CS": "#1abc9c"}
pin = {"MISO": "D12", "MOSI": "D11", "SCK": "D13", "CS": "D10"}
lvl = {"MISO": 14.0, "MOSI": 13.5, "SCK": 13.0, "CS": 12.5}
for n in ["MISO", "MOSI", "SCK", "CS"]:
    a = SD[n]; b = P[pin[n]]
    juhe(ax, [a, (a[0], lvl[n]), (b[0], lvl[n]), b], col[n])
ax.text(30.0, 13.6, "MISO → D12\nMOSI → D11\nSCK  → D13\nCS   → D10\nVCC  → 5V\nGND  → GND", fontsize=10, family="monospace", va="center")
fig.savefig("../../images/07-sd-kaart/07-sd_yhendus.png", bbox_inches="tight", facecolor="white")
