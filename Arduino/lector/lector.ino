
boolean conected = false;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  while (true){
    if(Serial.available()){
      char letra = Serial.read();
      Serial.println(letra);
      if(letra == 'k'){
        Serial.println("OK");
        conected = true;
        break;
      }
    }
  }

}

void loop() {
  // put your main code here, to run repeatedly:
 
  if(conected){
    int medida = analogRead(A2);
    Serial.println(medida);
    delay(100);

    if(Serial.available()){
      char letra = Serial.read();
      if(letra == 'd'){
        conected = false;
      }
    }
  }

}
