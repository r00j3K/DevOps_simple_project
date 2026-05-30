from fastapi import FastAPI, status, HTTPException
import socket;
import psutil
import psycopg2;
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

app = FastAPI()


@app.get("/")
async def root(): 
    return {
        "hostname": f"Hostname: {socket.gethostname()}",
        "version": "1.0.0"
        }

@app.get("/healthy", status_code=200)
async def app_healthy():
    return {"status": "alive"}

@app.get("/ready", status_code=200)
async def app_ready():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
        conn.close()
        return {"status": "app is ready to accept connections"}
    except Exception: 
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not connect to db"
        ) 

@app.get("/metrics", status_code=200)
async def get_os_metrics():
    disk_path = "/" if os.name != "nt" else "."
    return {
        "cpu_usage": psutil.cpu_percent(),
        "ram_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage(disk_path).percent
    }