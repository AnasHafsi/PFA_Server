#define bit0 4
#define bit1 3
#define bit2 2
#define IN1 9
#define IN2 10
#define IN3 11
#define IN4 12
#define SP1 6
#define SP2 5
int dip = 0;
int dim = 0;

void setup()
{
    pinMode(bit0, INPUT);
    pinMode(bit1, INPUT);
    pinMode(bit2, INPUT);
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(IN3, OUTPUT);
    pinMode(IN4, OUTPUT);
    pinMode(SP1, OUTPUT);
    pinMode(SP2, OUTPUT);
    Serial.begin(9600);
}
void STOP()
{
    Serial.println("STOP");
    analogWrite(SP1, 0);
    analogWrite(SP2, 0);
}
void LEFT()
{
    Serial.println("LEFT");
    digitalWrite(IN1, HIGH);
    digitalWrite(IN3, HIGH);
    analogWrite(SP1, 0);
    analogWrite(SP2, 255);
}
void RIGHT()
{
    Serial.println("RIGHT");
    digitalWrite(IN1, HIGH);
    digitalWrite(IN3, HIGH);
    analogWrite(SP1, 255);
    analogWrite(SP2, 0);
}
void UP()
{
    Serial.println("UP");
    digitalWrite(IN1, HIGH);
    digitalWrite(IN3, HIGH);
    analogWrite(SP1, 255);
    analogWrite(SP2, 255);
}
void BACK()
{
    dim=0;
    Serial.println("BACK");
    digitalWrite(IN2, HIGH);
    digitalWrite(IN4, HIGH);
    analogWrite(SP1, 255);
    analogWrite(SP2, 255);
}
void diagM()
{
    Serial.println("diagM");
    
    if (dim==0)
    {
        Serial.println("dim is 0");
        digitalWrite(IN1, HIGH);
        digitalWrite(IN3, HIGH);
        analogWrite(SP1, 255);
        analogWrite(SP2, 50);
        delay(100);
    }
    dim++;
    analogWrite(SP1, 255);
    analogWrite(SP2, 255);
}
void diagP()
{
    Serial.println("diagP");
    digitalWrite(IN1, HIGH);
    digitalWrite(IN3, HIGH);
    analogWrite(SP1, 50);
    analogWrite(SP2, 250);
    delay(100);
    analogWrite(SP1, 255);
    analogWrite(SP2, 255);
}
void loop()
{
    int a = digitalRead(bit0);
    int b = digitalRead(bit1);
    int c = digitalRead(bit2);
    if (a == HIGH)
    {
        if (b == HIGH)
        {
            if (c = HIGH)
                STOP();
            else
                RIGHT();
        }
        else
        {
            if (c == HIGH)
                diagP();
            else
                UP();
        }
    }
    else
    {
        if (b == HIGH)
        {
            if (c == HIGH)
                diagM();
            else
                LEFT();
        }
    }
}