/**
 * Main:        arduinoSkriptMall.ino
 * Autor:       Francisco Javier Ortín Cervera
 * Loodud:      09.02.2024
 * Muudatud:    09.02.2024
 *
 * Selgitus:    See on arduino skript malli lühike kirjeldus, peamine info peab olema README failis:
 *              Selleks, et meil oleks nii ühtlane kui võimalik: 
 *              - Funktsiooni nimed peavad olema camelCase-is (ehk iga sõna algus on suur täht)
 *              - Funktsiooni nimed kirjutame inglise keeles, aga kommentaarid võid eesti keeles
 * 
 * Teeked:
 * 
 * TODO:        - Kui vaja võib olla kasuks lisada, mida järgmisena teha
 *              
 */


 // Importimised

 // Globaalsed muutujad

 
void setup(){
  Serial.begin(115200);
}

void loop(){
  // Anduri kood
  
  // Kui anduri andmed on käes tuleb saata jadaside kaudu csv formaadis:
  // timestamp,andmeNimi,andmed
  Serial.print(millis());
  Serial.print(",");
  Serial.print("andur1"); // siin oleks rpm, ta, tm, vool, pingeA1, pingeA2, gps
  Serial.print(",");
  Serial.println(1234);
}