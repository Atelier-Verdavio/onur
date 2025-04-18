from flask import Flask, render_template, jsonify
import serial

app = Flask(__name__)
ser = None

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
            if ser.in_waiting:
                line = ser.readline().decode('utf-8').strip()
                if "Nem:" in line and "Sıcaklık:" in line:
                    nem = float(line.split('Nem:')[1].split('%')[0].strip())
                    sicaklik = float(line.split('Sıcaklık:')[1].split('°C')[0].strip())
                    return jsonify([{
                        'Nem (%)': nem,
                        'Sıcaklık (°C)': sicaklik
                    }])
        except Exception as e:
            print(f"Hata: {e}")
    return jsonify([])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) 