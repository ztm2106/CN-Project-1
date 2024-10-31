import socket

def start_server(host='0.0.0.0', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection established with client {client_address}")

            while True:
                message = receive_message(client_socket)
                if message:
                    print(f"Server received from client: {message.strip()}")
                    
                    # Respond back to the client with the initial acknowledgment
                    response = "okay\n"
                    print(f"Server sending to client: {response.strip()}")
                    client_socket.sendall(response.encode())

                else:
                    print(f"Client {client_address} disconnected")
                    break

            client_socket.close()
            print(f"Connection closed with client {client_address}")
    
    finally:
        server_socket.close()

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
    start_server()
