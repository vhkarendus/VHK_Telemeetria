# Telemeetria UI
Rakendus telemeetria komplekti kogutud andmete vaatamiseks. Rakenduses saab andurite graafikud kokku panna, aga ka neid eraldi vaadata.


- Võtab sisendina csv faili, praegu on faili valimine kuupäeva järgi nii et faili nimi peab olema formaadis **yyyy-mm-dd.txt** ja telemeetria rakenduse peaks käivitama failidega samas kaustas. 
- Failide sisu peab olema formaadis: *"data_num, millis, temperature_C_ta, rpm, current, battery_1_v, battery_2_v"* (rida failis)

*(Testimiseks CSV failide loomis rakendus on vales formaadis, nii et seda ei saa kasutada. See on siin alles, et see kunagi ümber teha)*
## Puudu
- arvutatud väärtused - kiirus (ülekande, diameetri ja rpm põhjal), võimsus (pinge ja vool), efektiivsus (kui palju võimsust kiiruseks muutub)

## Kasutamine
Vaja allalaadida: [StreamLit](https://docs.streamlit.io/get-started/installation), Bokeh (versioon 2.4.3), [Python](https://www.python.org/downloads/). Pythoni jaoks uuri oma süsteemi jaoks ise, StreamLit ja Bokeh saab [pip](https://pypi.org/project/pip/)'iga:
```
pip install streamlit
pip install bokeh
```

Samas kaustas andmete failiga jooksuta:
```
streamlit run telem_UI.py
```
