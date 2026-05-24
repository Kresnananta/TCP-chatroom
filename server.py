import socket
import threading

# Server configuration
SERVER_HOST = '0.0.0.0'  # Listen on all interfaces
SERVER_PORT = 12000
MAX_CLIENTS = 3

# Store connected clients
clients = []
client_names = {}
clients_lock = threading.Lock()

def handle_client(client_socket, client_address):
    """Handle each client connection in a separate thread"""
    client_id = len(clients)
    client_name = f"Client {client_id + 1}"
    
    try:
        # Add client to the list
        with clients_lock:
            clients.append(client_socket)
            client_names[client_id] = client_name
        
        print(f"[SERVER] {client_name} connected from {client_address}")
        
        # Send welcome message to the new client
        client_socket.send("Welcome to chatroom\n".encode())
        
        # Notify other clients about the new client
        notification = f"{client_name} has joined\n"
        with clients_lock:
            for i, other_client in enumerate(clients):
                if other_client != client_socket:
                    try:
                        other_client.send(notification.encode())
                    except:
                        pass
        
        # Keep the connection open to receive messages
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            
            print(f"[{client_name}] {message}")
            
            # Broadcast message to all other clients
            with clients_lock:
                for other_client in clients:
                    if other_client != client_socket:
                        try:
                            other_client.send(f"{client_name}: {message}".encode())
                        except:
                            pass
    
    except Exception as e:
        print(f"[ERROR] Error with {client_name}: {e}")
    
    finally:
        # Remove client from the list
        with clients_lock:
            if client_socket in clients:
                clients.remove(client_socket)
        
        # Notify other clients that this client left
        notification = f"{client_name} has left\n"
        with clients_lock:
            for other_client in clients:
                try:
                    other_client.send(notification.encode())
                except:
                    pass
        
        client_socket.close()
        print(f"[SERVER] {client_name} disconnected")

def start_server():
    """Start the TCP server"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(MAX_CLIENTS)
    
    print(f"[SERVER] Server started on port {SERVER_PORT}")
    print(f"[SERVER] Waiting for {MAX_CLIENTS} clients to connect...\n")
    
    try:
        while True:
            client_socket, client_address = server_socket.accept()
            
            # Create a new thread to handle this client
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.daemon = True
            client_thread.start()
    
    except KeyboardInterrupt:
        print("\n[SERVER] Shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
