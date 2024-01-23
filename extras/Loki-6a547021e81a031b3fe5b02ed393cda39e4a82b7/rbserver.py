
import socket # connect to server

server_host = "localhost"
server_port = 4444
# 1024 bits at a time to send data over to server
buffer_size = 1024

# socket object creation
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# option that allows reuse of socket if disconnected or cuts
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

# bind socket to server IP address
connection.bind((server_host, server_port))



# backlog (number of connections can be queued before system refuses connections )
connection.listen(5)
print(f"looking for clients as {server_host}:{server_port}")

# accept if client attempts to connect
client_socket, client_address = connection.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!!! YIPEEE")
print("connected YIPEE")

# just sending a message, for demonstration purposes
message = "Hello and Welcome".encode()
client_socket.send(message)



#connection.close() # close connection