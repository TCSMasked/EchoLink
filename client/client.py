import socket
import threading
import sys

# Connection configuration
HOST = '127.0.0.1'  # Server IP address
PORT = 8080  # Port number
ADDR = (HOST, PORT)
FORMAT = 'utf-8'

# Function to receive messages from the server
def receive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == 'Welcome to the Chatroom!\n':
                continue
            print(message)
        except:
            print('An error occurred while receiving messages from the server.')
            client.close()
            sys.exit()

# Function to send messages to the server
def send():
    while True:
        try:
            message = input()
            client.send(message.encode(FORMAT))
            if message.lower() == 'quit':
                client.close()
                sys.exit()
        except:
            print('An error occurred while sending messages to the server.')
            client.close()
            sys.exit()

# Main execution
if __name__ == '__main__':
    username = input('Enter your username: ')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    client.send(username.encode(FORMAT))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    send_thread = threading.Thread(target=send)
    send_thread.start()
