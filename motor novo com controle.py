from machine import Pin, PWM
from time import sleep

lpwm = PWM(Pin(1))  # LPWM no pino GP01
rpwm = PWM(Pin(0))  # RPWM no pino GP00

lpwm.freq(1000)  # F= 1kHz
rpwm.freq(1000)

def set_speed(speed, direction):
    if direction == "b":
        lpwm.duty_u16(speed)  
        rpwm.duty_u16(0)
    elif direction == "f":
        lpwm.duty_u16(0)     
        rpwm.duty_u16(speed)
    else:
        lpwm.duty_u16(0)   
        rpwm.duty_u16(0)

speed_stage = 10000

try:
    while True:
        comando = input("Pressionar um comando: b, f ou s. \n")
        if comando.lower() == 'b':
            print("Indo para trás")
            
            set_speed(speed_stage,'b')
        
        elif comando.lower() == 'f':
            print("Indo para frente")
            set_speed(speed_stage,'f')    
        
        elif comando.lower() == 's':
            print("Parando o motor")
            set_speed(speed_stage,'s')
            

except KeyboardInterrupt:
    print("Parando o motor.")
    set_speed(0, "stop")
    
    

