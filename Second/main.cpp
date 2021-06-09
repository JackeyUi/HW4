#include"mbed.h"
#include "bbcar.h"
#include "bbcar_rpc.h"
#include <stdio.h>
#include <string.h>


Ticker servo_ticker;
PwmOut pin5(D5), pin6(D6);
BufferedSerial pc(USBTX,USBRX); //tx,rx
BufferedSerial uart(D1,D0); //tx,rx
Thread t;
char recv[1];
//char r[1] = 'r';
//char s[1] = 's';
BBCar car(pin5, pin6, servo_ticker);

void steer() {
    while(1) {
    if (recv[0] == 'r') {
                car.goStraight(100);
                ThisThread::sleep_for(300ms);
            }
    if (recv[0] == 's') {
                car.stop();
                ThisThread::sleep_for(300ms);
            }
    }
}

int main(){
    t.start(steer);
    car.goStraight(100);
                ThisThread::sleep_for(300ms);
    car.stop();
                ThisThread::sleep_for(300ms);
   uart.set_baud(9600);
   while(1){
      if(uart.readable()){
            
            uart.read(recv, sizeof(recv));
            pc.write(recv, sizeof(recv));
            
        }
   }
}

