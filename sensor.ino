#include <SI114X.h>

#define WATER_SENSOR 2
SI114X si1141;

void setup()
{
	Serial.begin(9600);

	pinMode(WATER_SENSOR, INPUT);

	uint8_t conf[4];
}

void loop()
{
	bool isRaining = Serial.println(digitalRead(WATER_SENSOR));
	int visibleLight = si1141.ReadVisible();
	bool isCloudy;
	if (visibleLight > 200)
	{
		isCloudy = true;
	}
	else
	{
		isCloudy = false;
	}

	char recvChar;
}