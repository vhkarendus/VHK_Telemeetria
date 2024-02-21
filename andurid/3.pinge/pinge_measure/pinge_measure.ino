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
int r11 = 10000;
int r12 = 50000;
int r21 = 10000;
int r22 = 50000;
int Pin1 = A0;
int PinK = A1;
int Pin1Value, PinKValue, vOut1, vOutK, vIn1, vInK;

void setup()
{
  pinMode(Pin1, INPUT);
  pinMode(PinK, INPUT);
  
  Serial.begin(115200);
}

void loop()
{
  Pin1Value = analogRead(Pin1);
  PinKValue = analogRead(Pin2);
  
  // arvutab mitu volti jõuab arduino pini (mõlemad akud)
  vOutK = PinKValue * 5 / 1023;

  // arvtab mitu volti on mõlemad akud
  vInK = vOutK * ((r11 + r12) / r11);

  // arvutab mitu volti jõuab arduino pini (üks aku)
  vOut1 = Pin1Value * 5 / 1023;

  // arvutab mitu volti on üks aku
  vIn1 = vOut1 * ((r21 + r22) / r21);
  
  Serial.print(millis());
  Serial.print(",");
  Serial.print("pingeA1");
  Serial.print(",");
  Serial.println(vIn1);

  Serial.print(millis());
  Serial.print(",");
  Serial.print("pingeA2");
  Serial.print(",");
  Serial.println(vInK - vIn1);
}