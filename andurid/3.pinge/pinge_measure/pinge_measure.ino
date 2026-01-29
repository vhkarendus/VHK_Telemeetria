/**
 * Main:        pinge_measure.ino
 * Autor:       Juljus Putrinš
 * Loodud:      20.02.2024
 * Muudatud:    21.02.2024
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

// importimised

// globaalsed muutujad
float battery_sum_pin = A3;
float battery_1_pin = A4;

float divider_resistor_1 = 20000;
float divider_resistor_2 = 100000;

float calibrate_battery_1 = 0.0;
float calibrate_battery_sum = 0.0;

float battery_sum_pin_val, battery_1_pin_val, battery_sum_pin_v, battery_1_pin_v, battery_sum_v, battery_1_v;

void setup()
{  
  Serial.begin(115200);
}

void loop()
{
  battery_sum_pin_val = analogRead(battery_sum_pin);
  battery_1_pin_val = analogRead(battery_1_pin);

  battery_sum_pin_v = battery_sum_pin_val / 1023 * 5;
  battery_1_pin_v = battery_1_pin_val * 5 / 1023;

  battery_sum_v = battery_sum_pin_v * ((divider_resistor_1 + divider_resistor_2) / divider_resistor_1) * calibrate_battery_sum;
  battery_1_v = battery_1_pin_v * ((divider_resistor_1 + divider_resistor_2) / divider_resistor_1) * calibrate_battery_1;
  
  Serial.print(millis());
  Serial.print(",");
  Serial.print("pingeA1");
  Serial.print(",");
  Serial.println(battery_1_v);

  Serial.print(millis());
  Serial.print(",");
  Serial.print("pingeA2");
  Serial.print(",");
  Serial.println(battery_sum_v - battery_1_v);
}