#include <SI114X.h>

#define WATER_SENSOR 2
SI114X si1141;

// isRaining | isCloudy
bool currentStatus[] = {false, false};
bool oldStatus[] = {false, false};

void setup()
{
	Serial.begin(9600);
  getStatus(oldStatus);
	pinMode(WATER_SENSOR, INPUT);
}

void getStatus(bool status[]) {
  status[0] = digitalRead(WATER_SENSOR)> 0 ? false : true;
  status[1] = si1141.ReadVisible() < 256 ? false : true ;
}

bool statusChanged() {
  return !(oldStatus[0] == currentStatus[0] && oldStatus[1] == currentStatus[1]);
}

String getOutput() {
  bool isRaining = currentStatus[0];
  bool isCloudy = currentStatus[1];
  if      (isRaining && isCloudy)    return "11";
  else if (!(isRaining || isCloudy)) return "00";
  else if (  isRaining )                return "10";
  else                               return "01";
}

void copyStatus() {
  oldStatus[0] = currentStatus[0];
  oldStatus[1] = currentStatus[1];
}

void loop()
{
	 getStatus(currentStatus);
   if (statusChanged()) {
      Serial.println(getOutput());
   }
   copyStatus();
}
