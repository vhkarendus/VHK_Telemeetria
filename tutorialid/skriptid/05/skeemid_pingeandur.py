"""Joonistab 05 pingeanduri tutoriali skeemid (schemdraw).
pip install schemdraw
"""
import schemdraw
import schemdraw.elements as elm

OUT = "../../images/05-pingeandur/"

# 1) Pingejagur + testtoiteallikas
with schemdraw.Drawing(file=OUT + "05-pingejagur_skeem.png", show=False, dpi=150) as d:
    d.config(fontsize=13)
    src = d.add(elm.BatteryCell().up().reverse().label(["−", "Toiteallikas\n3–12 V", "+"], loc="bot"))
    d.add(elm.Line().right(1.5))
    d.add(elm.Line().right(1))
    r2 = d.add(elm.Resistor().down().label(["R2", "100 kΩ"], loc="top"))
    d.add(elm.Dot())
    node = d.here
    d.push()
    d.add(elm.Line().right(3).label("A0", loc="right"))
    d.add(elm.Dot(open=True))
    d.pop()
    d.push()
    d.add(elm.Line().right(1.5))
    d.add(elm.Capacitor().down().label(["C", "100 nF\n(valikuline)"], loc="bot"))
    d.add(elm.Line().left(1.5))
    d.pop()
    d.add(elm.Resistor().down().label(["R1", "22 kΩ"], loc="top"))
    d.add(elm.Dot())
    d.push()
    d.add(elm.Line().right(3).label("GND", loc="right"))
    d.add(elm.Dot(open=True))
    d.pop()
    d.add(elm.Line().left(2.5))
    d.add(elm.Line().toy(src.start))
    d.add(elm.Ground().at(src.start) if False else elm.Line().length(0))
    d.add(elm.Label().at((node[0] + 3.4, node[1] + 0.9)).label("Arduino Uno", fontsize=12))

# 2) Kaks akut (GreenPower)
with schemdraw.Drawing(file=OUT + "05-kaks_akut_skeem.png", show=False, dpi=150) as d:
    d.config(fontsize=13)
    b1 = d.add(elm.BatteryCell().up().reverse().label(["−", "Aku 1\n12 V", "+"], loc="bot"))
    mid = d.here
    b2 = d.add(elm.BatteryCell().up().reverse().label(["−", "Aku 2\n12 V", "+"], loc="bot"))
    top = d.here
    # jagur kogupingele (A4)
    d.add(elm.Line().at(top).right(6.5))
    d.add(elm.Resistor().down().label(["R2", "100 kΩ"], loc="top"))
    d.add(elm.Dot()); na = d.here
    d.add(elm.Resistor().down().label(["R1", "22 kΩ"], loc="top"))
    d.add(elm.Resistor().down().label(["", ""]).fill(False) if False else elm.Line().down(3))
    gA = d.here
    d.add(elm.Dot())
    # jagur aku 1 pingele (A5)
    d.add(elm.Line().at(mid).right(3.8))
    d.add(elm.Resistor().down().label(["R4", "100 kΩ"], loc="top"))
    d.add(elm.Dot()); nb = d.here
    d.add(elm.Resistor().down().label(["R3", "22 kΩ"], loc="top"))
    d.add(elm.Line().toy(gA))
    gB = d.here
    # GND siin
    d.add(elm.Line().at(b1.start).toy(gA))
    g0 = d.here
    d.add(elm.Line().at(g0).tox(gA))
    d.add(elm.Line().right(3).label("GND", loc="right")); d.add(elm.Dot(open=True))
    d.add(elm.Dot().at(gB))
    d.add(elm.Line().at(na).right(3).label("A4  (kogupinge)", loc="right")); d.add(elm.Dot(open=True))
    d.add(elm.Line().at(nb).toy(na[1] - 1.2) if False else elm.Line().at(nb).tox(na[0] + 3).label("A5  (aku 1)", loc="right"))
    d.add(elm.Dot(open=True))
