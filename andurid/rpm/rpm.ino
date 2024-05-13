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
 * TODO: Kui viimasest magnetis on möödas väga pikk aeg siis otsustatakse kas rpm on 0
 *              
 */


 // Importimised

 // Globaalsed muutujad

int magnet_count = 1;
int rpm_pin = 2;
unsigned long last_interval = 0;
unsigned long last_time = 0;
unsigned long current_time = 0;
float rpm = 0;

void motorMagnetInterrupt(){
  current_time = millis();
  unsigned long temp_interval = current_time - last_time ;
  if(temp_interval > 750){
    last_interval = temp_interval;
    last_time = current_time;
    if(magnet_count > 0){
      rpm = (float)60000 / (last_interval * magnet_count);
      Serial.print(last_interval);
    }
    else{
      rpm = 0;
    } 
  }
}

void setup(){
  Serial.begin(115200);
  attachInterrupt(digitalPinToInterrupt(rpm_pin), motorMagnetInterrupt, RISING); // interrupt triggerib siis, kui signaal läheb HIGH-ist LOW-iks (falling), sest op-ampil on pull-up resistor
}

void loop(){
  // Anduri kood
  
  // Kui anduri andmed on käes tuleb saata jadaside kaudu csv formaadis:
  // timestamp,andmeNimi,andmed
  Serial.print(millis());
  Serial.print(",");
  Serial.print("rpm"); // siin oleks rpm, ta, tm, vool, pingeA1, pingeA2, gps
  Serial.print(",");
  Serial.print(rpm);
  Serial.print(",");
  Serial.println(digitalRead(rpm_pin));
}
