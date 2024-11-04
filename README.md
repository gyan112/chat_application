Step 1: Create the Server
Create a file named chat_server.py. This will handle incoming connections and message broadcasting between clients.

python

Verify

Open In Editor
Edit
Copy code
import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345  # Port to listen on

# List to keep track of connected clients
clients = []

def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    clients.append(client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"[{addr}] {message}")
                broadcast(message, client_socket)
            else:
                break
        except:
            break

    print(f"[DISCONNECT] {addr} disconnected.")
    clients.remove(client_socket)
    client_socket.close()

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:  # Don't send the message to the sender
            client.send(message.encode('utf-8'))

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("[STARTING] Server is starting...")
    
    while True:
        client_socket, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
Step 2: Create the Client
Create another file named chat_client.py. This will allow users to connect to the server and send messages.

python

Verify

Open In Editor
Edit
Copy code
import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345  # Port to connect to

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            print("An error occurred while receiving a message.")
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Start a thread to listen for incoming messages
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    while True:
        message = input()
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    start_client()
Step 3: Run the Application
Start the Server:

Open a terminal and navigate to the directory where chat_server.py is located.
Run the server using the command:
bash

Verify

Open In Editor
Edit
Copy code
python chat_server.py
Start the Client:

Open another terminal (or multiple terminals for multiple clients) and navigate to the directory where chat_client.py is located.
Run the client using the command:
bash

Verify

Open In Editor
Edit
Copy code
python chat_client.py
Chat:

Once the client is connected, you can start typing messages in the client terminal.
Messages will be broadcasted to all connected clients.
Type exit to close the client.
Explanation of the Code
Server (chat_server.py):

Sets up a socket server that listens for incoming connections.
Each client connection is handled in a separate thread.
When a message is received, it is broadcast to all other connected clients.
Client (chat_client.py):

Connects to the server and starts a thread to listen for incoming messages.
The main thread takes user input and sends it to the server.
Users can exit the chat by typing exit.
Notes
This implementation is basic and does not include features like user authentication, message history, or encryption.
The server can be improved with error handling and logging.
Ensure that both the server and client are running on the same machine or adjust the HOST variable for remote connections.
