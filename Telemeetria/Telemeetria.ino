// INCLUDE --------------------------

#include <SPI.h>
#include <SD.h>


// CONSTANTS ------------------------

// temperature
const int thermistor_pin = A2;
const int thermistor_extra_resistor = 5100;
const int thermistor_base_resistance = 3300;
const int thermistor_B_value = 3977;
const int thermistor_base_temperature = 298.15; // 25C in Kelvin
const float c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07;

// current
const int current_sensor_out = A0;
const int current_sensor_ref = A1;

// voltage
float battery_sum_pin = A3;
float battery_1_pin = A4;

float divider_resistor_1 = 20000;
float divider_resistor_2 = 100000;

float calibrate_battery_1 = 0.0; // erase earlier calibration before calibrating again!!
float calibrate_battery_sum = 0.0; // erase earlier calibration before calibrating again!!

// SD card
const int sd_card_cs = 10;


// VARIABLES -------------------------

// temperature
int thermistor_extra_resistor_out;
float temperature, temperature_C, thermistor_resistance;

// current
int current_sensor_val, current_sensor_ref_val;
float current_sensor_voltage, current_sensor_ref_voltage, current;

// voltage
float battery_sum_pin_val, battery_1_pin_val, battery_sum_pin_v, battery_1_pin_v, battery_sum_v, battery_1_v;

// SD card
File output_file;


// SETUP -----------------------------

void setup() {
  // serial monitor
  Serial.begin(115200);
  while (!Serial) {}

  // SD card
  SD.begin(sd_card_cs);
  SD.remove("output.csv");

}


// LOOP -------------------------------

void loop() {

  // SD card
  output_file = SD.open("output.csv", FILE_WRITE);
  if (!output_file) {
    Serial.println("File not open!!");
  }

  // temperature
  thermistor_extra_resistor_out = analogRead(thermistor_pin);
  thermistor_resistance = thermistor_extra_resistor * (1023.0 / (float)thermistor_extra_resistor_out - 1.0);


  temperature = thermistor_resistance / thermistor_base_resistance;
  temperature = log(temperature);
  temperature /= thermistor_B_value;
  temperature += 1 / (thermistor_base_temperature + 273.15);
  temperature = 1 / temperature;

  temperature_C = temperature - 273.15;


  output_file.print(millis());
  output_file.print(",");
  output_file.print("tm"); // siin oleks rpm, ta, tm, vool, pingeA1, pingeA2, gps
  output_file.print(",");
  output_file.println(temperature_C);

  // Serial.print(millis());
  // Serial.print(",");
  // Serial.print("tm"); // siin oleks rpm, ta, tm, vool, pingeA1, pingeA2, gps
  // Serial.print(",");
  // Serial.println(temperature_C);


  // current
  current_sensor_val = analogRead(current_sensor_out);
  current_sensor_ref_val = analogRead(current_sensor_ref);

  current_sensor_voltage = (current_sensor_val / 1023.0) * 5; // muudab analog väärtuse voltideks
  current_sensor_ref_voltage = (current_sensor_ref_val / 1023.0) * 5; // muudab analog väärtuse voltideks
  current = ((current_sensor_voltage - current_sensor_ref_voltage) / 0.01); //muudab voldid ampriteks (ACS712 formula)

  output_file.print(millis());
  output_file.print(",");
  output_file.print("vool"); // siin oleks rpm, ta, tm, vool, pingeA1, pingeA2, gps
  output_file.print(",");
  output_file.println(current);

  // Serial.print(millis());
  // Serial.print(",");
  // Serial.print("vool"); // siin oleks rpm, ta, tm, vool, pingeA1, pingeA2, gps
  // Serial.print(",");
  // Serial.println(current);

  // voltage
  battery_sum_pin_val = analogRead(battery_sum_pin);
  battery_1_pin_val = analogRead(battery_1_pin);

  battery_sum_pin_v = battery_sum_pin_val / 1023 * 5;
  battery_1_pin_v = battery_1_pin_val * 5 / 1023;

  battery_sum_v = battery_sum_pin_v * ((divider_resistor_1 + divider_resistor_2) / divider_resistor_1) * calibrate_battery_sum;
  battery_1_v = battery_1_pin_v * ((divider_resistor_1 + divider_resistor_2) / divider_resistor_1) * calibrate_battery_1;
  
  output_file.print(millis());
  output_file.print(",");
  output_file.print("pingeA1");
  output_file.print(",");
  output_file.println(battery_1_v);

  output_file.print(millis());
  output_file.print(",");
  output_file.print("pingeA2");
  output_file.print(",");
  output_file.println(battery_sum_v - battery_1_v);

  // Serial.print(millis());
  // Serial.print(",");
  // Serial.print("pingeA1");
  // Serial.print(",");
  // Serial.println(battery_1_v);

  // Serial.print(millis());
  // Serial.print(",");
  // Serial.print("pingeA2");
  // Serial.print(",");
  // Serial.println(battery_sum_v - battery_1_v);


  // SD card
  output_file.close();
}
