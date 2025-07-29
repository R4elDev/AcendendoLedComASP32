from machine import Pin

from utime import sleep 

print("PROGRAMA DE SEMAFORO DO RAEL")

ledVerde = Pin(15, Pin.OUT)
ledAmarelo = Pin(18, Pin.OUT)
ledVermelho = Pin(4, Pin.OUT)

while True :
    ledVerde.on()
    sleep(20)
    ledVerde.off()
    sleep(0.5)

    ledAmarelo.on()
    sleep(10)
    ledAmarelo.off()
    sleep(0.5)

    ledVermelho.on()
    sleep(7)
    ledVermelho.off()
    sleep(0.5)
    