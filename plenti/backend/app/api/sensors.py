from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import SensorData
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/sensors/latest", response_model=dict)
async def get_latest_sensor_data(db: Session = Depends(get_db)):
    latest_data = db.query(SensorData).order_by(SensorData.timestamp.desc()).first()
    if not latest_data:
        raise HTTPException(status_code=404, detail="Veri bulunamadı")
    return {
        "temperature": latest_data.temperature,
        "humidity": latest_data.humidity,
        "co2": latest_data.co2,
        "light_intensity": latest_data.light_intensity,
        "timestamp": latest_data.timestamp
    }

@router.get("/sensors/history", response_model=List[dict])
async def get_sensor_history(
    hours: int = 24,
    db: Session = Depends(get_db)
):
    start_time = datetime.utcnow() - timedelta(hours=hours)
    history = db.query(SensorData).filter(
        SensorData.timestamp >= start_time
    ).order_by(SensorData.timestamp.desc()).all()
    
    return [{
        "temperature": data.temperature,
        "humidity": data.humidity,
        "co2": data.co2,
        "light_intensity": data.light_intensity,
        "timestamp": data.timestamp
    } for data in history] 