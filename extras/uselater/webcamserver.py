import pickle
import socket
import struct
import cv2

HOST = ''
PORT = 8089

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
connection.bind((HOST, PORT))
print('Socket bind complete')
connection.listen(10)
print('Socket now listening')

client_connection, addr = connection.accept()

data = b''
payload_size = struct.calcsize("L")

while True:

    # Retrieve message size
    while len(data) < payload_size:
        data += client_connection.recv(4096)

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]

    # Retrieve all data based on message size
    while len(data) < msg_size:
        data += client_connection.recv(4096)

    frame_data = data[:msg_size]
    data = data[msg_size:]

    # Extract frame
    frame = pickle.loads(frame_data)

    # Display
    cv2.imshow('frame', frame)
    cv2.waitKey(1)