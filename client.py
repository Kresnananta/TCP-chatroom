import socket
import threading
import sys

# Client configuration
SERVER_HOST = 'localhost'
SERVER_PORT = 12000

def receive_messages(client_socket):
    """Receive messages from server in a separate thread"""
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                sys.stdout.write("\r\033[K")
                sys.stdout.write(message.rstrip('\n') + '\n')
                sys.stdout.write("> ")
                sys.stdout.flush()
            else:
                break
        except:
            break

def main():
    """Connect to server and send messages"""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        
        # Receive welcome message
        welcome = client_socket.recv(1024).decode()
        print(welcome, end='')
        
        # Start receiving thread
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.daemon = True
        receive_thread.start()
        
        # Send messages
        while True:
            message = input("> ")
            if message.lower() in ("/exit", "/quit"):
                print("Disconnected from chatroom.")
                break
            if message:
                client_socket.send(message.encode())
    
    except KeyboardInterrupt:
        print("\nDisconnected from chatroom.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
