/**
 * Main:        rpm.ino
 * Autor:       Joonatan Jürisson
 * Loodud:      10.03.2024
 * Muudetud:    13.05.2024
 *
 * Selgitus:    arvutab pöördeid minutis kasutades op-ampiga võimendatud hall-effecti signaali poolt käivitatud interrupti. 
 * 
 * Teeked:
 * 
 * TODO: Kui viimasest magnetis on möödas väga pikk aeg siis otsustatakse kas rpm on 0
 * TODO: Debounceimine üle vaadata
 *              
 */


 // Importimised

 // Globaalsed muutujad

const int magnet_count = 1;
const int rpm_pin = 2;
volatile unsigned long last_interval = 0;
volatile unsigned long last_time = 0;
volatile unsigned long current_time = 0;
volatile float rpm = 0;

void motorMagnetInterrupt(){
  current_time = millis();
  unsigned long temp_interval = current_time - last_time ;
  if(temp_interval > 750){ // debounceing, hetkel kõrge väärtus, hall effect näib probleemne olevat
    last_interval = temp_interval;
    last_time = current_time;
    if(magnet_count > 0){
      rpm = (float)60000 / (last_interval * magnet_count);
    }
    else{
      rpm = 0;
    } 
  }
}

void setup(){
  Serial.begin(115200);
  attachInterrupt(digitalPinToInterrupt(rpm_pin), motorMagnetInterrupt, RISING); // funktsioon triggerib siis, kui signaal läheb LOW-ist HIGH-iks (rising)
}

void loop(){
  // Anduri kood
  
  // Kui anduri andmed on käes tuleb saata jadaside kaudu csv formaadis:
  // timestamp,andmeNimi,andmed
  Serial.print(millis());
  Serial.print(",");
  Serial.print("rpm"); // siin oleks rpm, ta, tm, vool, pingeA1, pingeA2, gps
  Serial.print(",");
  Serial.println(rpm);
}
