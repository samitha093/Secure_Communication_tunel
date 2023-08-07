import socket

def connect_to_server(host, port):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        # Receive data from the server (1024 bytes at a time)
        data = client_socket.recv(1024).decode()
        print(f"Server says: {data}")

        # Send a welcome message to the server
        welcome_message = "Hello, server! This is the client."
        client_socket.sendall(welcome_message.encode())
        print("Welcome message sent to the server.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the client socket when done
        client_socket.close()
        print("Client socket closed")

if __name__ == "__main__":
    # Set the host and port to connect to the server
    SERVER_HOST = "127.0.0.1"  # Use "localhost" if the server is on the same machine
    SERVER_PORT = 9999

    connect_to_server(SERVER_HOST, SERVER_PORT)
