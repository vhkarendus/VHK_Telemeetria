/**
 * Main:        rpm.ino
 * Autor:       Joonatan Jürisson
 * Loodud:      10.03.2024
 * Muudetud:    11.03.2024
 *
 * Selgitus:    See on arduino skript malli lühike kirjeldus, peamine info peab olema README failis:
 *              Selleks, et meil oleks nii ühtlane kui võimalik: 
 *              - Funktsiooni nimed peavad olema camelCase-is (ehk iga sõna algus on suur täht)
 *              - Funktsiooni nimed kirjutame inglise keeles, aga kommentaarid võid eesti keeles
 * 
 * Teeked:
 * 
 * TODO: tegelikult võiks mõõtmine olla ikkagi täpne - hetkel ei saa 1000ms oodata ja nii ei saa ka korralikult, täpselt mõõta
 *        äkki väline timer?
 *              
 */


 // Importimised

 // Globaalsed muutujad

int magnet_count = 0;
int rpm_pin = 5;
int last_pass_time = 0;
int rpm = 0;


void setup(){
  Serial.begin(115200);
}

void loop(){
  // Anduri kood

    if(rpm_pin == HIGH){
      if(magnet_count > 0){
        rpm = 1 / 1000 * (millis() - last_pass_time) / magnet_count;
        last_pass_time = millis();
      }
      else
      {
        rpm = 0
      }
      
    }
  
  // Kui anduri andmed on käes tuleb saata jadaside kaudu csv formaadis:
  // timestamp,andmeNimi,andmed
  Serial.print(millis());
  Serial.print(",");
  Serial.print("rpm"); // siin oleks rpm, ta, tm, vool, pingeA1, pingeA2, gps
  Serial.print(",");
  Serial.println(rpm);
}