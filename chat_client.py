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
