## todo

input to configure ip of the host machine
remove get / feature from fastapi server

## deployment

nginx web server with template.html and script.js
uvicorn --host 0.0.0.0 --port 8000

## how to build

    mkdir build
    cd build
    export PICO_SDK_PATH=<path-to-picoSDK>
    cmake ..
    cd blink
    make -j4

## how to run

simply drag blink.uf2 file to rpi booted as mass storage device (hold BOOTSEL)

## python listener

    virtualenv --python=python3 venv
    source venv/bin/activate
    pip install pyserial
    python3 listener.py

## fastapi websocket console

first configure environment

    virtualenv --python=python3 venv
    source venv/bin/activate
    pip install uvicorn
    pip install uvicorn[standard]
    pip install fastapi
    uvicorn api:app --reload

and then visit localhost:8000