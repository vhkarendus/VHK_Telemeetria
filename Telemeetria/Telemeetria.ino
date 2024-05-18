// INCLUDE --------------------------

#include <SPI.h>
#include <SD.h>


// CONSTANTS ------------------------

// temperature
const int thermistor_pin_ta = A2;
const int thermistor_pin_tm = A3;
const int thermistor_extra_resistor = 5100;
const int thermistor_base_resistance = 3300;
const int thermistor_B_value = 3977;
const int thermistor_base_temperature = 25; // in C

// rpm
const int rpm_magnet_count = 1;
const int rpm_pin = 2;

// current
const int current_sensor_out = A0;
const int current_sensor_ref = A1;

// voltage
float battery_sum_pin = A4;
float battery_1_pin = A5;

float divider_resistor_1 = 20000;
float divider_resistor_2 = 100000;

float calibrate_battery_1 = 1.026; // erase earlier calibration before calibrating again!!
float calibrate_battery_2 = 1.089; // erase earlier calibration before calibrating again!!

// SD card
const int sd_card_cs = 10;
const int log_interval = 500;


// VARIABLES -------------------------

// temperature
int thermistor_extra_resistor_out_ta, thermistor_extra_resistor_out_tm;
float temperature_ta, temperature_tm, temperature_C_ta, temperature_C_tm, thermistor_resistance_ta, thermistor_resistance_tm;

// rpm
volatile unsigned long rpm_last_interval = 0;
volatile unsigned long rpm_last_time = 0;
volatile unsigned long rpm_current_time = 0;
volatile float rpm = 0;

// current
int current_sensor_val, current_sensor_ref_val;
float current_sensor_voltage, current_sensor_ref_voltage, current;

// voltage
float battery_sum_pin_val, battery_1_pin_val, battery_sum_pin_v, battery_1_pin_v, battery_sum_v, battery_1_v, battery_2_v;

// SD card
File output_file;
unsigned long data_num = 0;


// FUNCTIONS -------------------------

// rpm
void motorMagnetInterrupt(){
  rpm_current_time = millis();
  unsigned long rpm_temp_interval = rpm_current_time - rpm_last_time ;
  if(rpm_temp_interval > 750){ // debounceing, hetkel kõrge väärtus, hall effect näib probleemne olevat
    rpm_last_interval = rpm_temp_interval;
    rpm_last_time = rpm_current_time;
    if(rpm_magnet_count > 0){
      rpm = (float)60000 / (rpm_last_interval * rpm_magnet_count);
    }
    else{
      rpm = 0;
    } 
  }
}

// SD card
void logData() 
{
  output_file = SD.open("output.csv", FILE_WRITE);
  if (!output_file) {
    Serial.println("File not open!!");
  }

  // log data in format (num, time, temperature_ta, temperature_tm, rpm, current, battery_1_v, battery_2_v)
  output_file.print(data_num);
  output_file.print(",");
  output_file.print(millis());
  output_file.print(",");
  output_file.print(temperature_C_ta);
  output_file.print(",");
  output_file.print(temperature_C_tm);
  output_file.print(",");
  output_file.print(rpm);
  output_file.print(",");
  output_file.print(current);
  output_file.print(",");
  output_file.print(battery_1_v);
  output_file.print(",");
  output_file.println(battery_2_v);

  Serial.println(battery_1_v);
  Serial.println(battery_2_v);

  data_num++;

  output_file.close();
}


// SETUP -----------------------------

void setup() {
  // serial monitor
  Serial.begin(115200);
  while (!Serial) {}

  // rpm
  attachInterrupt(digitalPinToInterrupt(rpm_pin), motorMagnetInterrupt, RISING); // funktsioon triggerib siis, kui signaal läheb LOW-ist HIGH-iks (rising)

  // SD card
  SD.begin(sd_card_cs);
  SD.remove("output.csv");

}


// LOOP -------------------------------

void loop() {

  // temperature
  thermistor_extra_resistor_out_ta = analogRead(thermistor_pin_ta);
  thermistor_extra_resistor_out_tm = analogRead(thermistor_pin_tm);

  thermistor_resistance_ta = thermistor_extra_resistor * (1023.0 / (float)thermistor_extra_resistor_out_ta - 1.0);
  thermistor_resistance_tm = thermistor_extra_resistor * (1023.0 / (float)thermistor_extra_resistor_out_tm - 1.0);


  temperature_ta = thermistor_resistance_ta / thermistor_base_resistance;
  temperature_ta = log(temperature_ta);
  temperature_ta /= thermistor_B_value;
  temperature_ta += 1 / (thermistor_base_temperature + 273.15);
  temperature_ta = 1 / temperature_ta;

  temperature_tm = thermistor_resistance_tm / thermistor_base_resistance;
  temperature_tm = log(temperature_tm);
  temperature_tm /= thermistor_B_value;
  temperature_tm += 1 / (thermistor_base_temperature + 273.15);
  temperature_tm = 1 / temperature_tm;

  temperature_C_ta = temperature_ta - 273.15;
  temperature_C_tm = temperature_tm - 273.15;


  // current
  current_sensor_val = analogRead(current_sensor_out);
  current_sensor_ref_val = analogRead(current_sensor_ref);

  current_sensor_voltage = (current_sensor_val / 1023.0) * 5; // muudab analog väärtuse voltideks
  current_sensor_ref_voltage = (current_sensor_ref_val / 1023.0) * 5; // muudab analog väärtuse voltideks
  current = ((current_sensor_voltage - current_sensor_ref_voltage) / 0.01); //muudab voldid ampriteks (ACS712 formula)


  // voltage
  battery_sum_pin_val = analogRead(battery_sum_pin);
  battery_1_pin_val = analogRead(battery_1_pin);

  battery_sum_pin_v = battery_sum_pin_val / 1023 * 5;
  battery_1_pin_v = battery_1_pin_val * 5 / 1023;

  battery_sum_v = battery_sum_pin_v * ((divider_resistor_1 + divider_resistor_2) / divider_resistor_1);
  battery_1_v = battery_1_pin_v * ((divider_resistor_1 + divider_resistor_2) / divider_resistor_1) * calibrate_battery_1;
  battery_2_v = (battery_sum_v - battery_1_v) * calibrate_battery_2;
  

  // SD card
  if (millis() >= log_interval * data_num) {
    logData();
  }
}
