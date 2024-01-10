
import socket # connect to server
import subprocess

server_host = "localhost" # 192.168.0.81
server_port = 4444
buffer_size = 1024

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((server_host, server_port))

# receive the greeting message
message = connection.recv(buffer_size).decode()
print("Server:", message)

# connection.close() # close connection