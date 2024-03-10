 // Globaalsed muutujad
int aku_andur = A0;
int mootori_andur = A1;
int Vout;
int Vout_2;

void setup(){
  Serial.begin(115200);
  pinMode(aku_andur, INPUT);
  pinMode(mootori_andur, INPUT);
}

void loop(){

  //aku temperatuuri anduri kontrollimine
  Vout = analogRead(aku_andur);
  
  if(Vout<0 || Vout>1023){
  Serial.println("Aku temperatuuri andur on katki!");
  }

  //mootori temperatuuri anduri kontrollimine
  Vout_2 = analogRead(mootori_andur);
  
  if(Vout_2<0 || Vout_2>1023){
  Serial.println("Mootori temperatuuri andur on katki!");
  }
}
