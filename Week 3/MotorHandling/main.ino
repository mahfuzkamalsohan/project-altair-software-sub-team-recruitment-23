#include "motor.h"

Motor leftMotor(2, 3, 5);   // direction pins 2,3  PWM pin 5
Motor rightMotor(4, 7, 6);  // direction pins 4,7  PWM pin 6


void loop() {
    // Move forward
    leftMotor.forward(200);
    rightMotor.forward(200);
    delay(3000);

    // Stop
    leftMotor.stop();
    rightMotor.stop();
    delay(1000);

    // Move backward
    leftMotor.backward(150);
    rightMotor.backward(150);
    delay(2000);

    // Stop before repeating
    leftMotor.stop();
    rightMotor.stop();
    delay(1000);
}
