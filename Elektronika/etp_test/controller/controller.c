/**
 * Copyright (c) 2020 Raspberry Pi (Trading) Ltd.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include "pico/stdlib.h"
#include <stdio.h>

const uint LED_PIN = PICO_DEFAULT_LED_PIN;

void lightOn(){
    gpio_put(LED_PIN,1);
    printf("LED light turned on.");
}

void lightOff(){
    gpio_put(LED_PIN,0);
    printf("LED light turned off.");
}

void throwError(){
    printf("Invalid command used.");
}

int main() {
    stdio_init_all();
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);

    char buffer[1];

    while (1) {
        scanf("%c",&buffer);

        switch(buffer[0]){
            case '0':{lightOff();break;} // TURN LED OFF
            case '1':{lightOn();break;} // TURN LED ON
            default:{throwError();break;} // INVALID COMMAND USED
        }
        
        sleep_ms(1000);
    }

    return 0;
}