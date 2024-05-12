/*
const int analogPin = A0; 
const float voltageRef = 5.0; 

void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(analogPin);
  float voltage = (sensorValue / 1023.0) * voltageRef; // muudab analog väärtus voltideks
  float current = ((voltage - (voltageRef / 2.0)) / 0.185); //muudab voldid ampriteks (ACS712 formula)

  Serial.print("Current: ");
  Serial.print(current);
  Serial.println(" mA");

  delay(1000); // Delay for 1 second
}
/*
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
const int current_sensor_out = A0;
const int current_sensor_ref = A1;
 
void setup(){
  Serial.begin(115200);
}

void loop(){
  // Anduri kood
  int current_sensor_val = analogRead(current_sensor_out);
  int current_sensor_ref_val = analogRead(current_sensor_ref);

  float current_sensor_voltage = (current_sensor_val / 1023.0) * 5; // muudab analog väärtuse voltideks
  float current_sensor_ref_voltage = (current_sensor_ref_val / 1023.0) * 5; // muudab analog väärtuse voltideks
  float current = ((current_sensor_voltage - current_sensor_ref_voltage) / 0.01); //muudab voldid ampriteks (ACS712 formula)

  delay(1000); // Delay for 1 second
  // Kui anduri andmed on käes tuleb saata jadaside kaudu csv formaadis:
  // timestamp,andmeNimi,andmed
  Serial.print(millis());
  Serial.print(",");
  Serial.print("Ammeter"); // siin oleks rpm, ta, tm, vool, pingeA1, pingeA2, gps
  Serial.print(",");
  Serial.println(current);
}