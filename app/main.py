from fastapi import FastAPI
import socket
import random
import platform


hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

app = FastAPI()
uname = platform.uname()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/host")
def read_host():
    return {"Hostname": hostname, "IP": ip}


@app.get("/random")
def read_random():
    return random.randrange(1, 1000000)


@app.get("/system")
def read_print():
    return {
        "System": {uname.system},
        "Node Name": {uname.node},
        "Release": {uname.release},
        "Version": {uname.version},
        "Machine": {uname.machine},
        "Processor": {uname.processor},
    }
