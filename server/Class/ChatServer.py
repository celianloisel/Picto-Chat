import socket
from Class.ClientHandler import ClientHandler


class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []
        self.server_socket = None
        self._usernames = []

    def get_username(self):
        return self._usernames

    def set_username(self, new_value):
        self._usernames = new_value

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Le serveur de chat est en cours d'exécution sur {self.host}:{self.port}...")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Nouvelle connexion de {client_address}")
            client_handler = ClientHandler(client_socket, client_address, self)
            client_handler.start()
            self.clients.append(client_handler)

    def broadcast(self, message):
        for client in self.clients:
            try:
                # Envoyer le message à tous les clients sauf l'expéditeur
                if client.client_address != message:
                    client.client_socket.sendall(message.encode('utf-8'))
            except Exception as e:
                print(f"Erreur lors de l'envoi du message au client {client.client_address}: {e}")
                self.remove_client(client)

    def private_message(self, username, content):
        for client in self.clients:
            try:
                
                # Envoyer le message au client ayant le pseudo correspondant
                if client.client_username == username:
                    client.client_socket.sendall(content.encode('utf-8'))
            except Exception as e:
                print(f"Erreur lors de l'envoi du message privé au client {client.client_address}: {e}")
                self.remove_client(client)

    def remove_client(self, client):
        if client in self.clients:
            self.clients.remove(client)
            client.client_socket.close()
            print(f"Le client {client.client_address} s'est déconnecté.")

    def stop(self):
        for client in self.clients:
            client.client_socket.close()
        self.server_socket.close()
        print("Le serveur de chat s'est arrêté.")
