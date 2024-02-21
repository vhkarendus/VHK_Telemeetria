// https://www.circuitbasics.com/how-to-setup-a-gps-sensor-on-the-arduino/

#include <Adafruit_GPS.h>
#include <SoftwareSerial.h>

SoftwareSerial gpsSerial(3, 2); // set pin 3 as RX and 3 as TX
Adafruit_GPS GPS(&gpsSerial); // connect adafruitGPS library to the new serial monitor (gpsSerial)

char c;

void setup() {
  Serial.begin(9600);
  GPS.begin(9600);

  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA); // only recieve GPRMC and GPGGA sentences

  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ); // set recieve frequency to 1hz
  delay(1000);
}

void loop() {

  clearGPS(); // clear out the serial buffer

  // wait until a NMEA sentence is ready to be read
  while (!GPS.newNMEAreceived()) {
    c = GPS.read();
  }

  GPS.parse(GPS.lastNMEA()); // received and parse the last NMEA sentence

  // print 1 if the gps has a fix, 0 if not
  Serial.print("Fix: ");
  Serial.print(GPS.fix);

  // in case of a fix
  if (GPS.fix) {

    // Location in longitude/latitude
    Serial.print("Location: ");
    Serial.print(GPS.latitude, 4);
    Serial.print(GPS.lat);
    Serial.print(", ");
    Serial.print(GPS.longitude, 4);
    Serial.println(GPS.lon);

    // Location in degrees
    Serial.print("Google Maps location: ");
    Serial.print(GPS.latitudeDegrees, 4);
    Serial.print(", ");
    Serial.println(GPS.longitudeDegrees, 4);

    // Speed
    Serial.print("Speed (km/h): ");
    Serial.println(GPS.speed * 1.85); // convert speed from knots to km/h

    // Altitude
    Serial.print("Altitude: ");
    Serial.println(GPS.altitude);
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