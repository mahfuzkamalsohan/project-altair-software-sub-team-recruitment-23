#include "motor.h"

Motor::Motor(int p1, int p2, int en)
  : pin1(p1), pin2(p2), enablePin(en)
{
    pinMode(pin1, OUTPUT);
    pinMode(pin2, OUTPUT);
    pinMode(enablePin, OUTPUT);

    // ensure motor is stopped initially
    digitalWrite(pin1, LOW);
    digitalWrite(pin2, LOW);
    analogWrite(enablePin, 0);
}

void Motor::forward(int speed) {
    digitalWrite(pin1, HIGH);
    digitalWrite(pin2, LOW);
    analogWrite(enablePin, speed);
}

void Motor::backward(int speed) {
    digitalWrite(pin1, LOW);
    digitalWrite(pin2, HIGH);
    analogWrite(enablePin, speed);
}

void Motor::stop() {
    digitalWrite(pin1, LOW);
    digitalWrite(pin2, LOW);
    analogWrite(enablePin, 0);
}
