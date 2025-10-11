#include <Arduino.h>

const int NUM_CHANNELS = 8;
int channels[NUM_CHANNELS];

void readChannel()
{
    static char buf[50];
    static int index = 0; 

    while (Serial1.available())
    {
        char c = Serial1.read();

        if (c == '<')
        {           
            index = 0;            
        }
        else if (c == '>')
        {      
            buf[index] = '\0';    //null terminating the buffer
            char *ptr = buf;
            for (int i = 0; i < NUM_CHANNELS; i++) {
                channels[i] = atoi(ptr);
                while (*ptr && *ptr != ' ') ptr++;  // skip digits
                if (*ptr) ptr++;                    // skip space
            }
        } 
        else if (index < sizeof(buf) - 1)
        {
            buf[index++] = c;
        }
    }
}

