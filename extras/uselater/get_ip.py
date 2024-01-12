import socket

import socket

def get_ip_address(hostname):
    return socket.gethostbyname(hostname)

# Replace 'hostname_or_address' with the hostname or IP address of the server
ip_address = get_ip_address('brin')
print("IP Address:", ip_address)
