from machine import Pin, Timer
import time

# Configuração do pino de entrada para contagem de pulsos
pulse_pin = Pin(13, Pin.IN, Pin.PULL_DOWN)

# Variáveis globais
pulse_count = 0  # Armazena o número de pulsos
V=0
velocidades=[]

# Função de interrupção para contar pulsos
def pulse_handler(pin):
    global pulse_count
    pulse_count += 1  # Incrementa o contador a cada pulso

# Configuração de interrupção no pino
pulse_pin.irq(trigger=Pin.IRQ_RISING, handler=pulse_handler)

# Timer para reportar a contagem em intervalos regulares
def report_pulse_count(timer):
    global pulse_count
    global V
    global velocidades
    V=pulse_count/7.01667 #cm/s
    velocidades.append(V)
    print("Pulsos em 1 segundo:", pulse_count, ", Velocidade:", V)
    pulse_count = 0  # Reseta o contador após a leitura

# Configura um timer de hardware para 1 segundo
timer = Timer()
timer.init(period=1000, mode=Timer.PERIODIC, callback=report_pulse_count)

while True:
    comando = input("Pressione 's' e Enter para sair: \n")
    if comando.lower() == 's':
        print("Encerrando o loop.")
        break
pulse_pin.irq(handler=None)

print(velocidades)
V_prev=0
P_prev=0
V_med=velocidades[1]
P_med=2
V_est=velocidades[0]
P_est=2
K=0

for i in range(len(velocidades)-1):
    V_prev=V_est
    P_prev=P_est
    K=P_prev/(P_prev+P_med)
    V_med=velocidades[i+1]
    V_est=(1-K)*V_prev+K*V_med
    P_est=(1-K)*P_prev
    print("Velocidade estimadada: {}, Desvio Padrão estimado: {}".format(V_est, P_est))