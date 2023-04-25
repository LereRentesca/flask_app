from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.get("/")
def ping():
    return{
        "status":"ok",
        "message":"pong",
        "server_time":datetime.now().strftime("%F %H:%M:%S")
    }