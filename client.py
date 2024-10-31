import socket
import sys

def start_client(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    print(f"Client connected to server at {server_ip}:{server_port}")

    try:
        while True:
            # Take user input and send to the server
            message = input("Enter message: ") + '\n'
            print(f"Client sending to server: {message.strip()}")
            client_socket.sendall(message.encode())

            # Receive and print the response from the server
            server_response = receive_message(client_socket)
            if server_response:
                print(f"Client received from server: {server_response.strip()}")
            else:
                print("Server disconnected")
                break
    finally:
        client_socket.close()

def receive_message(sock):
    message = []
    while True:
        chunk = sock.recv(1).decode()
        if not chunk:
            return None
        message.append(chunk)
        if chunk == '\n':
            break
    return ''.join(message)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python client.py <server_ip> <server_port>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    start_client(server_ip, server_port)
