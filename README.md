# ESP32 DHT11 Sıcaklık ve Nem Monitörü

Bu proje, ESP32 ve DHT11 sensörü kullanarak gerçek zamanlı sıcaklık ve nem takibi yapan bir web uygulamasıdır.

## Özellikler

- ESP32 üzerinden DHT11 sensör verilerini okuma
- Web arayüzünde gerçek zamanlı veri gösterimi
- Her 2 saniyede bir otomatik güncelleme
- Sıcaklık ve nem değerlerini anlık görüntüleme

## Gereksinimler

### Donanım
- ESP32 Geliştirme Kartı
- DHT11 Sıcaklık ve Nem Sensörü
- USB Kablosu

### Yazılım
- Python 3.x
- Flask
- PySerial
- Arduino IDE

## Kurulum

1. Arduino IDE'yi açın ve ESP32 kodunu yükleyin:
   ```cpp
   // esp32_dht11.ino dosyasındaki kodu kullanın
   ```

2. Python bağımlılıklarını yükleyin:
   ```bash
   pip install flask pyserial
   ```

3. Web uygulamasını başlatın:
   ```bash
   python app.py
   ```

4. Tarayıcıda açın:
   ```
   http://localhost:8080
   ```

## Bağlantılar

DHT11 sensörünü ESP32'ye şu şekilde bağlayın:
- VCC -> 3.3V
- GND -> GND
- DATA -> GPIO4

## Lisans

MIT License 