#include <SI114X.h>

#define WATER_SENSOR 2
SI114X si1141;

long c = 0;

void setup() {
  Serial.begin(9600);
  pinMode(WATER_SENSOR, INPUT);
}

int getStatus() {
  return (digitalRead(WATER_SENSOR) ? 0 : 2) + (si1141.ReadVisible() < 256 ? 1 : 0);
}

void loop() {
  if (c > 1000000) {
    String o;
    int status = getStatus();
    switch (status) {
      case 0: o = "0"; break;
      case 1: o = "1"; break;
      case 2: o = "2"; break;
      case 3: o = "3"; break;
    }
    Serial.print(o);
    c = 0;
  }
  c ++;
}
