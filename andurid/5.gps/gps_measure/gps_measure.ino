/**
 * Main:        gps_measure.ino
 * Autor:       Juljus
 * Loodud:      20.02.2024
 * Muudatud:    21.02.2024
 *
 * Selgitus:    https://www.circuitbasics.com/how-to-setup-a-gps-sensor-on-the-arduino/ põhjal
 * 
 * Teeked:      - SoftwareSerial
 *              - Adafruit_GPS
 * 
 * TODO:        gps start delay of 1000 ms
 *              
 */


// import
#include <Adafruit_GPS.h>
#include <SoftwareSerial.h>

// globaalsed muutujad
SoftwareSerial gpsSerial(3, 2); // set pin 3 as RX and 3 as TX
Adafruit_GPS GPS(&gpsSerial); // connect adafruitGPS library to the new serial monitor (gpsSerial)
char c;

void setup() {
  Serial.begin(115200);
  GPS.begin(115200);

  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA); // only recieve GPRMC and GPGGA sentences

  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ); // set recieve frequency to 1hz
}

void loop() {

  clearGPS(); // clear out the serial buffer

  // wait until a NMEA sentence is ready to be read and the gps start delay is over
  if (GPS.newNMEAreceived()) {

    GPS.parse(GPS.lastNMEA()); // received and parse the last NMEA sentence

    // print 1 if the gps has a fix, 0 if not
    Serial.print(millis());
    Serial.print(",");
    Serial.print("gpsFix");
    Serial.print(",");
    Serial.println(GPS.fix);

    // in case of a fix
    if (GPS.fix) {

      // // Location in degrees
      // Serial.print(millis());
      // Serial.print(",");
      // Serial.print("locationInDegrees");
      // Serial.print(",(");
      // Serial.print(GPS.latitudeDegrees, 4);
      // Serial.print(",");
      // Serial.print(GPS.longitudeDegrees, 4);
      // Serial.println(")");

      // Speed
      Serial.print(millis());
      Serial.print(",");
      Serial.print("gpsSpeed"); // in km/h
      Serial.print(",");
      Serial.println(GPS.speed * 1.85); // convert from knots to km/h before printing

      // // Altitude
      // Serial.print(millis());
      // Serial.print(",");
      // Serial.print("altitude");
      // Serial.print(",");
      // Serial.println(GPS.altitude);
    }

  }
  else {
    c = GPS.read();
  }

}

// take a reading from the GPS, parse the sentence, and then do nothing with it
void clearGPS() {

  // for the first NMEA sentence
  while (!GPS.newNMEAreceived()) {
    c = GPS.read();
  }
  GPS.parse(GPS.lastNMEA());

  // for the second NMEA sentence
  while (!GPS.newNMEAreceived()) {
    c = GPS.read();
  }
  GPS.parse(GPS.lastNMEA());
}