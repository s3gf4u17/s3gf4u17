from fastapi import FastAPI,WebSocket
from fastapi.responses import HTMLResponse
import serial,subprocess
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
subprocess.run(['sudo','chmod','a+wr','/dev/ttyACM0'])
ser=serial.Serial('/dev/ttyACM0',timeout=2)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def mainPage():
    with open("template.html","r") as f:
        html = f.read()
    return HTMLResponse(html)

@app.get("/send/{message}")
async def sendMessage(message):
    #return {"message":message}
    ser.write(message.encode())

@app.get("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            content=ser.readline()
            await websocket.send_text(content)
        except Exception as e:
            print(e)
            break