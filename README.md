# TCP Chatroom Project

This project implements a multi-threaded TCP chatroom using Python's `socket` and `threading` libraries. It allows multiple clients to connect to a central server and exchange messages in real-time.

## Project Structure

- `server.py`: The central server script. It manages client connections, handles message broadcasting, and tracks connected clients.
- `client1.py`, `client2.py`, `client3.py`: Identical client scripts used to connect to the server. Each client runs a separate thread for receiving messages to allow simultaneous sending and receiving.

## Technical Details

- **Protocol**: TCP (Transmission Control Protocol)
- **Port**: 12000 (Default)
- **Max Clients**: 3 (Configurable in `server.py`)
- **Concurrency**: Multi-threaded using the `threading` module. Each client connection is handled in its own thread on the server side, and each client uses a background thread for receiving messages.

## How to Run

1. **Start the Server**:
   ```bash
   python server.py
   ```
2. **Start the Clients**:
   Open separate terminal windows for each client and run:
   ```bash
   python client1.py
   python client2.py
   python client3.py
   ```

## Key Features

- **Real-time Broadcasting**: Messages sent by one client are broadcast to all other connected clients.
- **Connection Notifications**: The server notifies all clients when a new user joins or an existing user leaves.
- **Thread-Safe**: Uses `threading.Lock` on the server to manage the list of active client sockets safely.
