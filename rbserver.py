
import socket # connect to server

server_host = "192.168.0.81" # 192.168.0.81
server_port = 4444
buffer_size = 1024

class Connection:
    def __init__(self, server_host, server_port,buffer_size=1024):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # option that allows reuse of socket if disconnected or cuts
        self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        self.connection.bind((server_host, server_port))
        # listens and accepts if client attempts to connect
        self.connection.listen(1) # backlog
        print(f"looking for clients as {server_host}:{server_port}")
        self.client_socket, client_address = self.connection.accept() # self allows you to use self.connection anywhere in class
        print(f"{client_address[0]}:{client_address[1]} Connected")
    
    def execute_command(self, command):
        if command.lower() == "exit":
            quit()
        self.client_socket.send(command.encode())
        return self.client_socket.recv(buffer_size).decode() # no decode because no encode clientside fix later>?>?
    
    def quit(self,command):
            print("closed connection")
            #self.client_socket.close()
            self.connection.close()
            
    def run(self):
        while True:
            command = input("Enter a command: ")
            result = self.execute_command(command)
            print(result)

connection = Connection(server_host,server_port,buffer_size)
connection.run()






















"""
# just sending a message, for demonstration purposes
message = "Hello and Welcome".encode()
client_socket.send(message)
"""


#connection.close() # close connection