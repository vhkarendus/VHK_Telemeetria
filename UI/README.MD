# Telemeetria UI

Algne versioon. Võtab sisendina csv faili, praegu valimine kuupäeva järgi, hiljem peaks nime järgi tegema või kuidagi teisiti. Andurite graafikuid saab kokku panna, saab eraldi vaadata.
Testimis csv failid ka ja nende loomise programm.

## Teha
Oleks vaja määrata graafikute suurused ja muu selline. Selle jaoks on vaja teada mis kujul tulevad andmed, mis vahemikes need on (võibolla ei ole oluline). On vaja ka panna paika õiged andurite nimed ja nende leidmine sellest csv failist, sest praegu on need suvaliselt. Ilmselt on veel asju lisada vaja kui saame teada mida täpsemalt näha on vaja. Kindlasti vaja ka need suurused mida tuleb arvutada (distants, võimsus, mahtuvus, kiirus ja vb veel)

## Kasutamine
Lae alla streamlit ja bokeh (ja python) õiged versioonid. Vt streamlit/ bokeh lehelt kuidas ja mis versioonid.

streamlit run telemeetria_ui.py
