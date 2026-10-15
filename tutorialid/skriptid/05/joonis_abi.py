"""Abifunktsioonid ühendusjooniste joonistamiseks (Arduino Uno, makettplaat, takistid)."""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle

BAND = {0: "black", 1: "#8B4513", 2: "red", 3: "orange", 4: "yellow", 5: "green",
        6: "blue", 7: "violet", 8: "grey", 9: "white", "gold": "#D4AF37"}

# Uno päiste pinide x-koordinaadid (ühikud), plaadi vasak alumine nurk = (ux, uy)
UNO_W, UNO_H = 13.0, 9.0
DIG = ["AREF", "GND", "13", "12", "~11", "~10", "~9", "8", "", "7", "~6", "~5", "4", "~3", "2", "TX1", "RX0"]
PWR = ["IOREF", "RESET", "3.3V", "5V", "GND", "GND", "Vin", "", "A0", "A1", "A2", "A3", "A4", "A5"]


def uus(w, h):
    fig, ax = plt.subplots(figsize=(w, h), dpi=130)
    ax.set_xlim(0, w * 2); ax.set_ylim(0, h * 2); ax.set_aspect("equal"); ax.axis("off")
    return fig, ax


def uno(ax, ux, uy):
    """Joonistab Arduino Uno ja tagastab dict pinide nimi -> (x, y)."""
    ax.add_patch(FancyBboxPatch((ux, uy), UNO_W, UNO_H, boxstyle="round,pad=0.1,rounding_size=0.4",
                                fc="#00878F", ec="#005A60", lw=2, zorder=1))
    ax.text(ux + UNO_W / 2, uy + UNO_H / 2, "ARDUINO\nUNO", color="white", ha="center", va="center",
            fontsize=14, fontweight="bold", zorder=2)
    ax.add_patch(Rectangle((ux - 0.8, uy + 5.5), 2.2, 2.0, fc="#bbbbbb", ec="#777", zorder=2))  # USB
    ax.text(ux + 0.3, uy + 6.5, "USB", ha="center", va="center", fontsize=7, zorder=3)
    pins = {}
    step = 0.62
    x0 = ux + 2.4
    for i, n in enumerate(DIG):
        if not n:
            continue
        x = x0 + i * step; y = uy + UNO_H - 0.45
        ax.add_patch(Rectangle((x - 0.2, y - 0.2), 0.4, 0.4, fc="#222", zorder=3))
        ax.text(x, y - 0.45, n, rotation=90, ha="center", va="top", fontsize=6.5, color="white", zorder=3)
        if n == "GND":
            pins["GND_top"] = (x, y)
        elif n[0] in "~0123456789":
            pins["D" + n.strip("~")] = (x, y)
        else:
            pins[n] = (x, y)
    x0 = ux + 3.6
    for i, n in enumerate(PWR):
        if not n:
            continue
        x = x0 + i * step; y = uy + 0.45
        ax.add_patch(Rectangle((x - 0.2, y - 0.2), 0.4, 0.4, fc="#222", zorder=3))
        ax.text(x, y + 0.45, n, rotation=90, ha="center", va="bottom", fontsize=6.5, color="white", zorder=3)
        key = n
        if n == "GND":
            key = "GND" if "GND" not in pins else "GND2"
        pins[key] = (x, y)
    return pins


def makett(ax, x, y, w, h):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.2",
                                fc="#f2f2f2", ec="#aaa", lw=1.5, zorder=0))


def takisti(ax, x1, y1, x2, y2, bands, label=None, lpos="right", fc="#E8D3A0"):
    """Takisti punktist (x1,y1) punkti (x2,y2) (vertikaalne või horisontaalne)."""
    ax.plot([x1, x2], [y1, y2], color="#888", lw=2, zorder=4)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    vert = abs(x2 - x1) < abs(y2 - y1)
    L, W = 2.0, 0.7
    if vert:
        ax.add_patch(FancyBboxPatch((mx - W / 2, my - L / 2), W, L, boxstyle="round,pad=0.02,rounding_size=0.25",
                                    fc=fc, ec="#9c8455", zorder=5))
        for i, b in enumerate(bands):
            ax.add_patch(Rectangle((mx - W / 2, my + L / 2 - 0.35 - i * 0.38), W, 0.18, fc=BAND[b], zorder=6))
    else:
        ax.add_patch(FancyBboxPatch((mx - L / 2, my - W / 2), L, W, boxstyle="round,pad=0.02,rounding_size=0.25",
                                    fc=fc, ec="#9c8455", zorder=5))
        for i, b in enumerate(bands):
            ax.add_patch(Rectangle((mx - L / 2 + 0.2 + i * 0.38, my - W / 2), 0.18, W, fc=BAND[b], zorder=6))
    if label:
        if lpos == "right":
            ax.text(mx + 0.7, my, label, va="center", ha="left", fontsize=10, zorder=7)
        elif lpos == "left":
            ax.text(mx - 0.7, my, label, va="center", ha="right", fontsize=10, zorder=7)
        else:
            ax.text(mx, my + 0.6, label, va="bottom", ha="center", fontsize=10, zorder=7)


def juhe(ax, pts, color, lw=3):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=color, lw=lw, solid_capstyle="round", solid_joinstyle="round", zorder=8)
    for p in (pts[0], pts[-1]):
        ax.add_patch(Circle(p, 0.15, fc=color, ec="black", lw=0.5, zorder=9))


def punkt(ax, p):
    ax.add_patch(Circle(p, 0.2, fc="black", zorder=10))
