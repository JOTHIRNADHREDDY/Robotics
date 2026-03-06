#define led 9      
#define button 2  

int brightness = 0;    
int fade = 5;    

void setup() {
  pinMode(led, OUTPUT);
  pinMode(button, INPUT_PULLUP); 
}

void loop() {
  if (digitalRead(button) == LOW) {
    analogWrite(led, brightness);
    brightness = brightness + fade;
    if (brightness <= 0 || brightness >= 255) {
      fade= -fade;
    }
    delay(30);
  } else {
    analogWrite(led, 0);
  }
}
