#define buttons A0
#include <SoftwareSerial.h>

SoftwareSerial mySerial(7, 6);

void setup() {
  mySerial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
  // Serial.begin(9600);
}

void loop() {
  int btnInp = analogRead(buttons);
  //mySerial.println(btnInp);
  if(btnInp>1000){
    mySerial.println("hotkey('alt', 'tab')");
    delay(1000);
  }
  else if(btnInp>400 && btnInp<600){
    mySerial.println("hotkey('win', 'd')");
    delay(1000);
  }
  else if(btnInp>300 && btnInp<400){
    mySerial.println("hotkey('alt', 'f4')");
    delay(1000);
  }
  else if(btnInp>200 && btnInp<300){
    mySerial.println("press('space')");
    delay(1000);
  }
  /* else {
    mySerial.println(btnInp);
  } */
}