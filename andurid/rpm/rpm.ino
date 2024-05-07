/**
 * Main:        rpm.ino
 * Autor:       Joonatan Jürisson
 * Loodud:      10.03.2024
 * Muudetud:    07.05.2024
 *
 * Selgitus:    arvutab pöördeid minutis kasutades op-ampiga võimendatud hall-effecti signaali poolt käivitatud interrupti. 
 * 
 * Teeked:
 * 
 * TODO: 
 *              
 */


 // Importimised

 // Globaalsed muutujad

int magnet_count = 1;
int rpm_pin = 2;
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
  attachInterrupt(digitalPinToInterrupt(rpm_pin), motorMagnetInterrupt, FALLING); // interrupt triggerib siis, kui signaal läheb HIGH-ist LOW-iks (falling), sest op-ampil on pull-up resistor
}

void loop(){
  // Anduri kood
    if(digitalRead(rpm_pin) == LOW){
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
