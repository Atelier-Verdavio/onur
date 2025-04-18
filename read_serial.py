import serial
import time

# Seri port bağlantısını aç
ser = serial.Serial('/dev/tty.usbserial-0001', 115200)
print("DHT11 sensöründen veri okunuyor...")
print("-" * 40)

try:
    while True:
        if ser.in_waiting:
            line = ser.readline().decode('utf-8').strip()
            print(line)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nProgram sonlandırıldı.")
    ser.close() 