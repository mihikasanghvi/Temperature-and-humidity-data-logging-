/*
 * demo sketch for PLX DAQ v2 
 * Moving Real Time Data Diagramm
 */

#include<DHT.h>
#include<LiquidCrystal.h>
#include <MySQL_Connection.h>
int Rs=12,E=11,D4=5,D5=4,D6=3,D7=2;
LiquidCrystal lcd(12,11,5,4,3,2);
#define DHTTYPE DHT11
#define DHTPIN 7
DHT dht(DHTPIN,DHTTYPE);

char server[]="127.0.0.1";
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
lcd.begin(16,2);
dht.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
float humidity = dht.readHumidity();
float temp = dht.readTemperature();
lcd.setCursor(0,0);
lcd.print("TEMP:");
lcd.print(temp);
lcd.print((char)223);
lcd.print("C");
lcd.setCursor(0,1);
lcd.print("HUMIDITY:");
lcd.print(humidity);
lcd.print("%");
Serial.print(humidity);
Serial.print('\n');
Serial.print(temp);
Serial.println();
delay(1000);

}
