from flask import Flask, render_template, jsonify
import serial
import os

app = Flask(__name__)
ser = None

# Sadece lokal geliştirme ortamında seri port bağlantısı kur
if not os.environ.get('RENDER'):
    try:
        ser = serial.Serial('/dev/tty.usbserial-0001', 115200, timeout=1)
    except:
        print("Seri port bağlantısı kurulamadı!")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    if ser and ser.is_open:
        try:
            data = {}
            while ser.in_waiting:
                line = ser.readline().decode('utf-8').strip()
                
                if "DHT11 - Nem:" in line:
                    parts = line.split('|')
                    nem = float(parts[0].split(':')[1].replace('%', '').strip())
                    sicaklik_dht = float(parts[1].split(':')[1].replace('°C', '').strip())
                    data['dht11'] = {
                        'nem': nem,
                        'sicaklik': sicaklik_dht
                    }
                
                elif "DS18B20 - Sıcaklık:" in line:
                    sicaklik_ds = float(line.split(':')[1].replace('°C', '').strip())
                    data['ds18b20'] = {
                        'sicaklik': sicaklik_ds
                    }
                
                elif "LDR - Işık Şiddeti" in line:
                    isik = int(line.split(':')[1].strip())
                    data['ldr'] = {
                        'isik_seviyesi': isik
                    }
            
            if data:
                return jsonify(data)
                
        except Exception as e:
            print(f"Hata: {e}")
    
    # Eğer seri port bağlantısı yoksa veya Render'da çalışıyorsa örnek veri döndür
    return jsonify({
        'dht11': {'nem': 50, 'sicaklik': 25},
        'ds18b20': {'sicaklik': 24},
        'ldr': {'isik_seviyesi': 500}
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port) 