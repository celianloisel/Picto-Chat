import socket
import threading


class ChatServer:
    MAX_CONNECTIONS = 5

    def __init__(self, port):
        self._port = port
        self._connections_thread = threading.Thread(target=self._accept_connections)
        self._messages_thread = threading.Thread(target=self._handle_messages)

    def get_port(self):
        return self._port

    def set_port(self, new_value):
        self._port = new_value

    def _accept_connections(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(('10.57.33.126', int(self._port)))
            server_socket.listen(ChatServer.MAX_CONNECTIONS)
            print(f"Server is listening on port {self._port}")
            while True:
                try:
                    client_socket, client_address = server_socket.accept()
                    print(f"Connection established from {client_address}")

                    # Traiter la connexion client ici

                    print(f"Client {client_address} disconnected")

                except Exception as e:
                    print(f"Error accepting connection: {e}")

    def _handle_messages(self):
        while True:
            # Traiter les messages reçus des clients ici
            pass

    def execute(self):
        self._connections_thread.start()
        self._messages_thread.start()

        self._connections_thread.join()
        self._messages_thread.join()

        print("Server stopped.")
