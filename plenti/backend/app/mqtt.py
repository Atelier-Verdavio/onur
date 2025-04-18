import paho.mqtt.client as mqtt
from .config import settings
from .database import SessionLocal
from .models import SensorData
from datetime import datetime
import json

def on_connect(client, userdata, flags, rc):
    print("MQTT Bağlantısı başarılı")
    client.subscribe("plenti/sensors/#")

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        db = SessionLocal()
        
        sensor_data = SensorData(
            temperature=data.get("temperature"),
            humidity=data.get("humidity"),
            co2=data.get("co2"),
            light_intensity=data.get("light_intensity"),
            timestamp=datetime.utcnow()
        )
        
        db.add(sensor_data)
        db.commit()
        db.close()
        
    except Exception as e:
        print(f"Veri işleme hatası: {e}")

client = mqtt.Client()
client.username_pw_set(settings.MQTT_USERNAME, settings.MQTT_PASSWORD)
client.on_connect = on_connect
client.on_message = on_message

def start_mqtt_client():
    client.connect(settings.MQTT_BROKER, settings.MQTT_PORT, 60)
    client.loop_start() 