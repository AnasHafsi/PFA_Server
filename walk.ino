#define bit0
#define bit1
#define bit2
#define IN1
#define IN2
#define IN3
#define IN4
#define SP1
#define SP2

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
}
void STOP()
{
    analogWrite(SP1, 0);
    analogWrite(SP2, 0);
}
void LEFT()
{
}
void RIGHT()
{
}
void UP()
{
    digitalWrite(IN1, HIGH);
    digitalWrite(IN3, HIGH);
    analogWrite(SP1, 255);
    analogWrite(SP2, 255);
}
void BACK()
{
    digitalWrite(IN1, HIGH);
    digitalWrite(IN3, HIGH);
    analogWrite(SP1, 255);
    analogWrite(SP2, 255);
}
void diagM()
{
}
void diagP()
{
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
            if (C == HIGH)
                diagP() else UP();
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