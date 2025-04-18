#include "DHT.h"

// DHT11 sensörünün bağlı olduğu pin
#define DHTPIN 4     // GPIO4 pini kullanılıyor

// Sensör tipi DHT11 olarak belirtiliyor
#define DHTTYPE DHT11

// DHT sensör nesnesi oluşturuluyor
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // Seri haberleşme başlatılıyor
  Serial.begin(115200);
  
  // DHT11 sensörü başlatılıyor
  dht.begin();
  
  Serial.println("DHT11 başlatıldı...");
}

void loop() {
  // İki okuma arasında 2 saniye bekleme
  delay(2000);

  // Nem değeri okunuyor
  float nem = dht.readHumidity();
  // Sıcaklık değeri okunuyor (Celsius)
  float sicaklik = dht.readTemperature();

  // Okunan değerlerin geçerli olup olmadığı kontrol ediliyor
  if (isnan(nem) || isnan(sicaklik)) {
    Serial.println("Veri okunamadı!");
    return;
  }

  // Okunan değerler seri porta yazdırılıyor
  Serial.print("Nem: ");
  Serial.print(nem);
  Serial.print(" % | ");
  Serial.print("Sıcaklık: ");
  Serial.print(sicaklik);
  Serial.println(" °C");
} 