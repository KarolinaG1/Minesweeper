import socket
import json

HOST = "172.104.229.108"
PORT = 9001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    info = json.dumps({"username": "NAME"})
    s.sendall(str.encode(info))
    data = s.recv(2048)
    message = json.dumps({"request": "ALL_ROOMS"})
    s.sendall(str.encode(message))
    response = s.recv(2048).decode()
    print(response)

    message2 = json.dumps({"request": "CREATE_ROOM", "data": "POKOJ"})
    s.sendall(str.encode(message2))
    response2 = s.recv(2048).decode()
    print(response2)

    s.close()
