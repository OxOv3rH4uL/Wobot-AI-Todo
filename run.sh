#!/bin/bash
echo "Waiting for MySQL to be available..."
python << END
import socket
import time

host = "mysql"
port = 3306
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        s.connect((host, port))
        s.close()
        break
    except socket.error as ex:
        time.sleep(1)
END
echo "MySQL is up and running. Starting the FastAPI application..."
uvicorn main:app --reload --port=8000 --host=0.0.0.0