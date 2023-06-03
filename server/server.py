import socket
import threading
from datetime import datetime

# Server configuration
HOST = '127.0.0.1'  # Server IP address
PORT = 8080  # Port number
ADDR = (HOST, PORT)
FORMAT = 'utf-8'

# Global variables
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients = []
usernames = []

# Function to broadcast messages to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Function to handle individual client connections
def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if not message:  # Handles disconnection when client closes the socket
                index = clients.index(client)
                clients.remove(client)
                client.close()
                username = usernames[index]
                broadcast(f'[-] {username} has disconnected from the session.'.encode(FORMAT))
                usernames.remove(username)
                break
            elif message.lower() == 'quit':
                index = clients.index(client)
                clients.remove(client)
                client.close()
                username = usernames[index]
                broadcast(f'[-] {username} has disconnected from the session.'.encode(FORMAT))
                usernames.remove(username)
                break
            else:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                broadcast(f'[{timestamp}] {usernames[clients.index(client)]}: {message}'.encode(FORMAT))
                print(f'[{timestamp}] {usernames[clients.index(client)]}: {message}')
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f'[-] {username} has disconnected from the session.'.encode(FORMAT))
            usernames.remove(username)
            break

# Function to start the server and handle new client connections
def start_server():
    server.listen()
    print('[+] Server is listening on', HOST, ':', PORT)
    while True:
        client, address = server.accept()
        print('[+] New connection:', address)
        username = client.recv(1024).decode(FORMAT)
        usernames.append(username)
        clients.append(client)
        print('[+] New user:', username)
        client.send('Welcome to the Chatroom!\n'.encode(FORMAT))
        broadcast(f'[+] {username} has joined the session.'.encode(FORMAT))
        client_thread = threading.Thread(target=handle_client, args=(client,))
        client_thread.start()

# Main execution
if __name__ == '__main__':
    server.bind(ADDR)
    start_server()