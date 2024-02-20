int r1 = 10000;
int r2 = 50000;
int mPin = A0;
int value, vOut, vIn;

void setup()
{
  pinMode(mPin, INPUT);
  
  Serial.begin(9600);
}

void loop()
{
  value = analogRead(mPin);
  
  // arvutab mitu volti jõuab arduino pini
  vOut = value * 5 / 1023;

  // arvtab mitu volti on vooluallikas
  vIn = vOut * ((r1 + r2) / r1);
  
  Serial.println(vIn);
}