import serial
import datetime
import csv
import os

# Seri port bağlantısını kur
ser = serial.Serial('/dev/tty.usbserial-0001', 115200)

# CSV dosyası için başlıkları oluştur
headers = ['Tarih', 'Saat', 'Nem (%)', 'Sıcaklık (°C)']

# CSV dosyasını oluştur
filename = 'dht11_verileri.csv'
file_exists = os.path.isfile(filename)

with open(filename, 'a', newline='') as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(headers)

try:
    print("DHT11 sensör verilerini okumaya başlıyorum...")
    print("Çıkmak için Ctrl+C'ye basın")
    print("\nTarih\t\t\tSaat\t\t\tNem\t\tSıcaklık")
    print("-" * 70)
    
    while True:
        if ser.in_waiting:
            # Seri porttan veriyi oku
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            
            # Sadece sensör verisi içeren satırları işle
            if "Nem:" in line and "Sıcaklık:" in line:
                # Şu anki tarih ve saati al
                now = datetime.datetime.now()
                date_str = now.strftime("%Y-%m-%d")
                time_str = now.strftime("%H:%M:%S")
                
                try:
                    # Nem ve sıcaklık değerlerini ayır
                    nem = float(line.split('Nem:')[1].split('%')[0].strip())
                    sicaklik = float(line.split('Sıcaklık:')[1].split('°C')[0].strip())
                    
                    # Ekrana yazdır
                    print(f"{date_str}\t{time_str}\t{nem:>5.1f}%\t\t{sicaklik:>5.1f}°C")
                    
                    # CSV dosyasına kaydet
                    with open(filename, 'a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow([date_str, time_str, nem, sicaklik])
                        
                except (IndexError, ValueError) as e:
                    continue

except KeyboardInterrupt:
    print("\nProgram sonlandırıldı.")
    ser.close() 