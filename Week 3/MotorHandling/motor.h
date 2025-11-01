#ifndef MOTOR_H
#define MOTOR_H

#include <Arduino.h>

class Motor 
{
    private:
        int pin1;
        int pin2;
        int enablePin;
    public:
        Motor(int p1, int p2, int en);
        void forward(int speed);
        void backward(int speed);
        void stop();

};
#endif 