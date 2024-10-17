import rp2
from machine import Pin
from rp2 import PIO
from utime import sleep
import time
import network

ledAlto = Pin(5, Pin.OUT)
ledBaixo = Pin(4, Pin.OUT)
ledMedio = Pin(3, Pin.OUT)
led_interno = Pin("LED", Pin.OUT)

# Define the pins for the trigger and echo
trigger = Pin(21, Pin.OUT)
echo = Pin(22, Pin.IN)

@rp2.asm_pio(out_init=[PIO.OUT_LOW])
def echo():
    wrap_target()
    mov(pins, isr)     
    mov(isr, invert(isr))
    pull(noblock)      
    mov(x, osr)
    mov(y, x)
    label("loop")
    jmp(y_dec, "loop")  
    wrap()

sm = rp2.StateMachine(0, echo, freq=1_000_000, out_base=Pin(7))
sm.active(1)

def play(freq):
  if freq:
    sm.put(1_000_000//freq)
  else:
    sm.put(0)

def conectar_wifi(rede, senha):
    # Istância do objeto WLAN como 'Cliente':
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    if not wifi.isconnected():
        print("Conectando à rede WiFi...")
        wifi.connect(rede, senha)
        while not wifi.isconnected(): pass
    print("Wifi Conectado! Endereço IP:", wifi.ifconfig()[0])
    return wifi.active()
   
def ultrasonico():
    trigger.low()
    utime.sleep_us(3)
    trigger.high()
    utime.sleep_us(3)
    trigger.low()

    while echo.value() == 0:
        sinalOff = utime.ticks_us()
    while echo.value() == 1:
        sinalOn = utime.ticks_us()

    tempo = sinalOn - sinalOff
    distancia = (tempo * 0.03429) / 1.9
           
    if distancia > 100:
        print("Nível de água alto detectada!")
        play(2000)
        ledAlto.toggle()
        sleep(0.2)
        play(9000)
        ledAlto.toggle()
        sleep(0.2)
        play(0)  
        ledAlto.toggle()
        sleep(0.2)
        ledBaixo.off()
        ledMedio.off()
        
    elif distancia >= 50:
        print("Nível de água médio detectada!")  
        play(2000)
        ledMedio.toggle()
        sleep(0.2)
        play(9000)
        ledMedio.toggle()
        sleep(0.2)
        play(0)  
        ledMedio.toggle()
        sleep(0.2)
        ledBaixo.off()
        ledAlto.off()
    else:
        print("Nível de água baixo!.")
        ledAlto.off()
        ledMedio.off()
        play(1000)
        ledBaixo.toggle()
        sleep(0.5)
        play(9000)

    print(f"Distância do Sensor = {distancia} cm")

#Main
conectar_wifi("Gustavo", "1234567")
led_interno.on()

while True:
    ultrasonico()
    #utime.sleep(1)