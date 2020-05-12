import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("127.0.0.1", 5000)
s.connect(address)

while True:
    print("Wiadomosc:")
    message = input()
    data = s.sendall(str.encode(message))
    response = s.recv(2048)
    print("Program 1:", response.decode())
