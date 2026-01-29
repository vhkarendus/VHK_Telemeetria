const int thermistor_pin = A2;
const int thermistor_extra_resistor = 5100;
const int thermistor_base_resistance = 3300;
const int thermistor_B_value = 3977;
const int thermistor_base_temperature = 298.15; // 25C in Kelvin
const float c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07;

int thermistor_extra_resistor_out;
float temperature, temperature_C, thermistor_resistance;

void setup() {
Serial.begin(9600);
}

void loop() {

  thermistor_extra_resistor_out = analogRead(thermistor_pin);
  thermistor_resistance = thermistor_extra_resistor * (1023.0 / (float)thermistor_extra_resistor_out - 1.0);


  temperature = thermistor_resistance / thermistor_base_resistance;
  temperature = log(temperature);
  temperature /= thermistor_B_value;
  temperature += 1 / (thermistor_base_temperature + 273.15);
  temperature = 1 / temperature;

  temperature_C = temperature - 273.15;

  // temperature = 1.0 / ((1 / thermistor_base_temperature) + ((log(thermistor_resistance)) / thermistor_B_value));
  // temperature_C = temperature - 273.15;


  Serial.print("Temperature: "); 
  Serial.print(temperature_C);
  Serial.println(" C"); 

  delay(500);
}
