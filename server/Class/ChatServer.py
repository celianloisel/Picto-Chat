import socket
import threading
from server.Class.User import User


class ChatServer:
    MAX_CONNECTIONS = 5

    def __init__(self, port):
        self._port = port
        self._client_socket = None
        self._connections_thread = threading.Thread(target=self._accept_connections)
        self._messages_thread = threading.Thread(target=self._handle_messages)

    # Rest of the code...

    def _accept_connections(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(('10.57.33.126', int(self._port)))
            server_socket.listen(ChatServer.MAX_CONNECTIONS)
            print(f"Server is listening on port {self._port}")
            while True:
                try:
                    client_socket, client_address = server_socket.accept()
                    user_name = client_socket.recv(20).decode()
                    user = User(client_address, user_name)
                    print(f"Connection established from {client_address} : {user.get_user_name()}")
                    self._client_socket = client_socket  # Store the client_socket as an instance variable

                except Exception as e:
                    print(f"Error accepting connection: {e}")

    def _handle_messages(self):
        while True:
            if self._client_socket:
                data = self._client_socket.recv(1024)
                print(data)
                self._client_socket.sendall(data)

    def execute(self):
        self._connections_thread.start()
        self._messages_thread.start()

        self._connections_thread.join()
        self._messages_thread.join()

        print("Server stopped.")
