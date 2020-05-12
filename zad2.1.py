import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("127.0.0.1", 5000)
s.bind(address)
s.listen(1)
conn, addr = s.accept()

while True:
    data = conn.recv(2048)
    print("Program 2:", data.decode())
    print("Wiadomosc:")
    message = input()
    conn.sendall(str.encode(message))
