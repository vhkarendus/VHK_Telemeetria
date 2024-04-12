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
float batterySumPin = A0;
float battery1Pin = A1;

float r1 = 20000;
float r2 = 100000;

float calibrateBattery1 = 0.0;
float calibrateBatterySum = 0.0;

float batterySumPinVal, battery1PinVal, batterySumPinV, battery1PinV, batterySumV, battery1V;

void setup()
{  
  Serial.begin(115200);
}

void loop()
{
  batterySumPinVal = analogRead(batterySumPin);
  battery1PinVal = analogRead(battery1Pin);

  batterySumPinV = batterySumPinVal / 1023 * 5;
  battery1PinV = battery1PinVal * 5 / 1023;

  batterySumV = batterySumPinV * ((r1 + r2) / r1) * calibrateBatterySum;
  battery1V = battery1PinV * ((r1 + r2) / r1) * calibrateBattery1;
  
  Serial.print(millis());
  Serial.print(",");
  Serial.print("pingeA1");
  Serial.print(",");
  Serial.println(battery1V);

  Serial.print(millis());
  Serial.print(",");
  Serial.print("pingeA2");
  Serial.print(",");
  Serial.println(batterySumV - battery1V);
}