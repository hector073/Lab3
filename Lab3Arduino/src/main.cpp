#include <Arduino.h>

/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/AnalogReadSerial
*/

String msg;
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);

}
//**************************Funciones*****************************
void frecuenciaMuestreo(){
//esta funcion sirve para leer el dato enviado desde python e interpretarlo para luego 
//cambiar la frecuencia de muestreo
  if(Serial.available() > 0){
    msg = Serial.readString();
  }
  
  if(msg == "uno"){

  }

  else if(msg == "cinco"){

  }

  else if(msg == "diez"){
    
  }

}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 36:
  int sensorValue = analogRead(36);
  // print out the value you read:
  Serial.println(sensorValue);
  delay(100);  // delay in between reads for stability
}

