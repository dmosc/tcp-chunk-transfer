import socket


BUFFER_SIZE = 2048
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 3001))
server.listen()

client_socket, client_address = server.accept()
out_file = open("out.jpeg", "wb")
chunk = client_socket.recv(BUFFER_SIZE)
while chunk:
    out_file.write(chunk)
    chunk = client_socket.recv(BUFFER_SIZE)
out_file.close()
client_socket.close()
