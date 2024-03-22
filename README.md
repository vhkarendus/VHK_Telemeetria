# VHK_Telemeetria

## Andurite arendus
Siin on andurid (sulgudes on anduri lühend).
1. Kiirus andur ([rpm](/andurid/1.rpm/README.md)) -> [@theUGG0](https://github.com/theUGG0)
2. Voolu andur ([vool](/andurid/2.vool/README.md)) -> [@KLaidma](https://github.com/KLaidma)
3. Pinge andur ([pinge](/andurid/3.pinge/README.md)) -> [@juljus](https://github.com/juljus)
4. Temperatuuri andur ([temp](/andurid/4.temp/README.md)) -> [@paulkask](https://github.com/paulkask)
5. GPS ([gps](/andurid/5.gps/README.md)) -> [@juljus](https://github.com/juljus)

### Kuidas arendus käib?
1. Igaüks teeb uut branchi `dev_anduri_lühend` ja hakkab arendama oma anduri kaustas nii, et hiljem on lihtne merge teha. `git chekout -b dev_anduri_lühend`
2. On vaja README failis lisada info võimalikud andurite kohta. Tabeli loomiseks see võiks olla abiks [Markdown table generator](https://www.tablesgenerator.com/markdown_tables)
3. Kaustas teeme 2 kausta (testimiseks ja mõõtmiseks) sama nimega kui anduri skripti nimi (muidu Arduino IDE viskab vea aknat). Skripti loomiseks võib kasutada [malli](/mallid/arduinoSkriptMall/arduinoSkriptMall.ino) 
4. Mõistlik on alustada mõõtmiskoodiga, siis pärast on juba teadmised kuidas õige andur peaks töötama.

### Mida on vaja?
- Hall effect sensor (5x) [Lemona](https://www.lemona.ee/hall-effect-switch-unipolar-3pin.html), [Oomipood](https://www.oomipood.ee/kataloog/farnell/toode?sku=2748270)
- Op-amp (5x) [Lemona](https://www.lemona.ee/ic-op-amp.html)
- Voolutugevus sensor (5x (3 on keldris olemas)) [Lemona](https://www.lemona.ee/current-transducer-50a-pcb-hais-50-p.html), [Oomipood](https://www.oomipood.ee/kataloog/farnell/toode?sku=1617433)
- Temperatuuri sensor (10x) [Lemona](https://www.lemona.ee/thermistor-100k-5-ntc-rad.html), [Oomipood](https://www.oomipood.ee/product/640_100k_100k_ntc_b_const_5_4190k_500mw)
- GPS (aga ärme osta äkki) [Lemona](https://www.lemona.ee/gps-module-u-blox-neo-7m-for-arduinor-wpi430.html), [Oomipood](https://www.oomipood.ee/product/product?product_id=1150845)
- Microcontroller (6x) [Lemona](https://www.lemona.ee/dev-kit-evaluation-solder-pads-usb-c-socket-pin-2x7-xiao-seeed-studio.html), [Oomipood](https://www.oomipood.ee/kataloog/farnell/toode?sku=3932158)
- Display (5x) [Lemona](https://www.lemona.ee/joy-it-84x48-lcd-display-spi-sbc-lcd84x48.html)(SPI), [Amazon](https://www.amazon.de/-/en/MakerHawk-Display-Module-SSD1306-Arduino/dp/B07BDFXFRK/ref=sr_1_4?crid=2YI79FQ97O7R3&dib=eyJ2IjoiMSJ9.GMkHnwdfcX58cN8A0OPgSGlCF8pOY2qv9w-8mWbDnAJ1VlcUv8i0Z7dL578gQ8GLJloR2tlM7WBCiT0ef-NpoBM05d7qCIQ5MhzYxDq7a7HvjpusIQ9gNaq7L48Udz7vYVtlfRGtKDNAus1miyKH8qyEBeVqcxBrTEuoFvTteiYjbe85f9CRxthP0WaBcZM-wXLYO5gMg0iWb6TJ-kSSISi0QKbE5YEs4MW1XruR_wU.ozBqg49swyHL7KDgL_vU0wnyNrPtSQ_RBsAeV4DCVNI&dib_tag=se&keywords=arduino+display&qid=1711121486&sprefix=arduino+display,aps,115&sr=8-4)(I2C)
- Micro SD card module (5x) [Amazon](https://www.amazon.de/-/en/ANGEEK-Module-Reader-Arduino-Microcontrollers/dp/B07S6K3RVK/ref=sr_1_4?crid=1VXZP0IE5IY2I&dib=eyJ2IjoiMSJ9.Wd8bGir_Rr53tlAkofkv2YZ_MOz8MVdkb58a6l1kiyrLoaXV4dtn21Bz8rQ6FhQvhkXmGMQtkOLaHayH0JnVVJe8ms-4jVQ7hdRj0qdxQJaSTE5m3mBWE10AsYtsSsQDe8Zp45YK7JzpMzE1cXl9dawvtGbOCQwCqO0cDXBVVI813kbQGXeWFyFGDgWjVDeCbPWF6e5qe85Kxdz23D2ZY-3fcwqAiCDIduUeOdUWxZw.z0X4F8oAnrqWwukdockZu1hSC8VzKt5a69itKWlwyPc&dib_tag=se&keywords=micro+sd+card+arduino&qid=1711121599&sprefix=micro+sd+card+arduino,aps,124&sr=8-4)(SPI)

## UI
Kasutame [streamlit](https://streamlit.io) koos [bokeh](https://bokeh.org) ja [matplotlib](https://matplotlib.org)

Enne hakkata programmeerimima oleks vaja tutvuda nende teekedega. Selleks on need tutorialid:
- [streamlit installation](https://docs.streamlit.io/get-started/installation)
- [streamlit fundamentals](https://docs.streamlit.io/get-started/fundamentals/main-concepts)
- [streamlit create an app](https://docs.streamlit.io/get-started/tutorials/create-an-app)
- [matplotlib tutorial](https://matplotlib.org/stable/tutorials/pyplot.html#sphx-glr-tutorials-pyplot-py)
