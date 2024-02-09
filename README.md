# VHK_Telemeetria

## Andurite arendus
Siin on andurid (sulgudes on anduri lühend).
1. Kiirus andur ([rpm](/andurid/1.rpm/README.md)) -> [@theUGG0](https://github.com/theUGG0)
2. Voolu andur ([vool](/andurid/2.vool/README.md)) -> [@KLaidma](https://github.com/KLaidma)
3. Pinge andur ([pinge](/andurid/3.pinge/README.md)) -> [@juljus](https://github.com/juljus)
4. Temperatuuri andur ([temp](/andurid/4.temp/README.md)) -> [@paulkask](https://github.com/paulkask)
5. GPS ([gps](/andurid/5.gps/README.md)) -> [@juljus] (https://github.com/juljus)

### Kuidas arendus käib?
1. Igaüks teeb uut branchi `dev_anduri_lühend` ja hakkab arendama oma anduri kaustas nii, et hiljem on lihtne merge teha. `git chekout -b dev_anduri_lühend`
2. On vaja README failis lisada info võimalikud andurite kohta. Tabeli loomiseks see võiks olla abiks [Markdown table generator](https://www.tablesgenerator.com/markdown_tables)
3. Kaustas teeme 2 kausta (testimiseks ja mõõtmiseks) sama nimega kui anduri skripti nimi (muidu Arduino IDE viskab vea aknat). Skripti loomiseks võib kasutada [malli](/mallid/arduinoSkriptMall/arduinoSkriptMall.ino) 
4. Mõistlik on alustada mõõtmiskoodiga, siis pärast on juba teadmised kuidas õige andur peaks töötama.

## UI
Kasutame [streamlit](https://streamlit.io) koos [bokeh](https://bokeh.org) ja [matplotlib](https://matplotlib.org)

Enne hakkata programmeerimima oleks vaja tutvuda nende teekedega. Selleks on need tutorialid:
- [streamlit installation](https://docs.streamlit.io/get-started/installation)
- [streamlit fundamentals](https://docs.streamlit.io/get-started/fundamentals/main-concepts)
- [streamlit create an app](https://docs.streamlit.io/get-started/tutorials/create-an-app)
- [matplotlib tutorial](https://matplotlib.org/stable/tutorials/pyplot.html#sphx-glr-tutorials-pyplot-py)
