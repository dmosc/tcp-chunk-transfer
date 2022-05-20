import socket


BUFFER_SIZE = 2048
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 3001))
file = open("payload.jpeg", "rb")
chunk = file.read(BUFFER_SIZE)
while chunk:
    client.send(chunk)
    chunk = file.read()
file.close()
client.close()
