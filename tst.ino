#include <stdio.h>

#define OUT1 12
#define OUT2 13
#define OUT3 11
#define OUT4 10
#define SP1 5
#define SP2 6

#define ORDER_COMPLETED 8

#define IN1 1
#define IN2 2
#define IN3 3

int paramGlobal[20];
int PARAM_VITES_PAS = 0;

int PARAM_I_FOR_GO_LEFT = 1;
int PARAM_DELAY_GO_LEFT = 2;
int PARAM_STOP_GO_LEFT = 3;

int PARAM_I_FOR_GO_RIGHT = 4;
int PARAM_DELAY_GO_RIGHT = 5;
int PARAM_STOP_GO_RIGHT = 6;

int PARAM_ANNUL_TEST = 7;
int PARAM_I_FOR_GO_FORWARD = 8;
int PARAM_CORRECTION = 9;

int PARAM_VITES_L = 10;
int PARAM_VITES_R = 11;

int valOrder;

int val1;
int val2;
int val3;

void initDefaultParamGlobal()
{

    paramGlobal[PARAM_VITES_PAS] = 78;

    paramGlobal[PARAM_I_FOR_GO_LEFT] = 40;
    paramGlobal[PARAM_DELAY_GO_LEFT] = 48;
    paramGlobal[PARAM_STOP_GO_LEFT] = 70;

    paramGlobal[PARAM_I_FOR_GO_RIGHT] = 43;
    paramGlobal[PARAM_DELAY_GO_RIGHT] = 46;
    paramGlobal[PARAM_STOP_GO_RIGHT] = 70;

    paramGlobal[PARAM_ANNUL_TEST] = 0;
    paramGlobal[PARAM_I_FOR_GO_FORWARD] = 13;
    paramGlobal[PARAM_CORRECTION] = 0;

    paramGlobal[PARAM_VITES_L] = 253;
    paramGlobal[PARAM_VITES_R] = 207;
}

void setup()
{

    initDefaultParamGlobal();
    pinMode(OUT1, OUTPUT);
    pinMode(OUT2, OUTPUT);
    pinMode(OUT3, OUTPUT);
    pinMode(OUT4, OUTPUT);
    pinMode(SP1, OUTPUT);
    pinMode(SP2, OUTPUT);
    Serial.begin(9600);
}

void goForward()
{
    analogWrite(SP1, paramGlobal[PARAM_VITES_L]);
    analogWrite(SP2, paramGlobal[PARAM_VITES_R]);
    digitalWrite(OUT1, LOW);
    digitalWrite(OUT2, HIGH);
    digitalWrite(OUT3, HIGH);
    digitalWrite(OUT4, LOW);
    Serial.println("go FW");
}
void goLeft()
{
    analogWrite(SP1, 255);
    analogWrite(SP2, 255);
    digitalWrite(OUT1, LOW);
    digitalWrite(OUT2, HIGH);
    digitalWrite(OUT3, LOW);
    digitalWrite(OUT4, HIGH);
    Serial.println("go LEFT");
}
void goRight()
{
    analogWrite(SP1, 255);
    analogWrite(SP2, 255);
    digitalWrite(OUT1, HIGH);
    digitalWrite(OUT2, LOW);
    digitalWrite(OUT3, HIGH);
    digitalWrite(OUT4, LOW);
    Serial.println("go Right");
}
void goBack()
{
    analogWrite(SP1, 255);
    analogWrite(SP2, 255);
    digitalWrite(OUT1, HIGH);
    digitalWrite(OUT2, LOW);
    digitalWrite(OUT3, LOW);
    digitalWrite(OUT4, HIGH);
    Serial.println("go Back");
}
void stp()
{

    digitalWrite(OUT1, LOW);
    digitalWrite(OUT3, LOW);
    digitalWrite(OUT2, LOW);
    digitalWrite(OUT4, LOW);
    analogWrite(SP1, 0);
    analogWrite(SP2, 0);
    Serial.println("Stop");
}

void loop()
{

    val1 = digitalRead(IN1);
    val2 = digitalRead(IN2);
    val3 = digitalRead(IN3);

    if (val1 == LOW && val2 == HIGH && val3 == LOW)
        goForward();
    else if (val1 == HIGH && val2 == HIGH && val3 == HIGH)
        goBack();
    else if (val1 == HIGH && val2 == LOW && val3 == LOW)
        goLeft();
    else if (val1 == LOW && val2 == LOW && val3 == HIGH)
        goRight();
    else if (val1 == LOW && val2 == LOW && val3 == LOW)
        stp();
}