# Telemeetria UI

Võtab sisendina csv faili, praegu on faili valimine kuupäeva järgi nii et faili nimi peaks olema formaadis **yyyy-mm-dd.txt**. 

Failide sisu peaks olema formaadis: *"data_num, millis, temperature_C_ta, rpm, current, battery_1_v, battery_2_v"* (rida failis)

Rakenduses saab andurite graafikud kokku panna, aga ka neid eraldi vaadata.

Testimiseks CSV failide loomis rakendus on vales formaadis, nii et seda ei saa kasutada! See on siin alles, et see kunagi ümber teha 

## Puudu
- arvutatud väärtused - kiirus (ülekande, diameetri ja rpm põhjal), võimsus (pinge ja vool), efektiivsus (kui palju võimsust kiiruseks muutub)

## Kasutamine
Vaja allalaadida: [StreamLit](https://docs.streamlit.io/get-started/installation), Bokeh (versioon 2.4.3), [Python](https://www.python.org/downloads/)

```
pip install streamlit
pip install bokeh
```

Samas kaustas andmete failiga jooksuta:
```streamlit run telem_UI.py```
