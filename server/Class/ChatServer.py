import socket
import threading
from Class.User import User


class ChatServer:
    MAX_CONNECTIONS = 5

    def __init__(self, port):
        self._port = port
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.bind(('192.168.1.106', int(self._port)))
        self._server_socket.listen(ChatServer.MAX_CONNECTIONS)
        print(f"Server is listening on port {self._port}")
        self._connections = []
        self._lock = threading.Lock()
        self._usernames = set()  # Utiliser un ensemble pour stocker les pseudos

    def _handle_client(self, client_socket, client_address):
        try:
            user_name = client_socket.recv(20).decode()
            if user_name in self._usernames:  # Vérifier si le pseudo est déjà utilisé
                client_socket.sendall("Ce pseudo est déjà pris. Veuillez en choisir un autre.".encode())
                
                client_socket.close()
                return

            user = User(client_address, user_name)
            print(f"Connection established from {client_address} : {user.get_user_name()}")
            with self._lock:
                self._connections.append(client_socket)
                self._usernames.add(user_name)  # Ajouter le pseudo à l'ensemble
        except Exception as e:
            print(f"Error accepting connection: {e}")

    def _handle_messages(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    with self._lock:
                        self._connections.remove(client_socket)
                    client_socket.close()
                    break
                print(data)
                with self._lock:
                    for connection in self._connections:
                        if connection != client_socket:
                            connection.sendall(data)
            except Exception as e:
                print(f"Error handling messages: {e}")
                break

    def execute(self):
        while True:
            try:
                client_socket, client_address = self._server_socket.accept()
                client_thread = threading.Thread(target=self._handle_client, args=(client_socket, client_address))
                client_thread.start()
                messages_thread = threading.Thread(target=self._handle_messages, args=(client_socket,))
                messages_thread.start()
            except KeyboardInterrupt:
                print("Server stopped.")
                break
            except Exception as e:
                print(f"Error accepting connection: {e}")
