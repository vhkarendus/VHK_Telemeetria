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
 * TODO: 
 *              
 */


 // Importimised

 // Globaalsed muutujad

int magnet_count = 0;
int rpm_pin = 5;
unsigned long last_interval = 0;
float rpm = 0;

void motorMagnetInterrupt(){
  unsigned long temp_interval = millis() - last_interval;
  if(temp_interval > 20){
    last_interval = temp_interval;
  }
}

void setup(){
  Serial.begin(115200);
  attachInterrupt(digitalPinToInterrupt(rpm_pin), motorMagnetInterrupt, RISING);
}

void loop(){
  // Anduri kood

    if(rpm_pin == HIGH){
      if(magnet_count > 0){
        rpm = (float)60000 / (last_interval * magnet_count);
      }
      else
      {
        rpm = 0;
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