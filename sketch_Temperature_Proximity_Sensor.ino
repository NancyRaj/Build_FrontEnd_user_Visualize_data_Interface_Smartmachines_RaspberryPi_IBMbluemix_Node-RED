int senspin=A2;
int proxpin=A1;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
int bitval=analogRead(senspin);
float volt=float(bitval)*5/1023;
int temp=volt*100;

int prox=analogRead(proxpin);
Serial.print(temp);
Serial.print(',');
Serial.println(prox);
delay(3000);
}
