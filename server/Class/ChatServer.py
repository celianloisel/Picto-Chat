import socket
from Class.ClientHandler import ClientHandler
import os


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
        if not os.path.exists('../logs.csv'):
            open('logs.txt', 'a').close()

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Le serveur de chat est en cours d'exécution sur {self.host}:{self.port}...")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Nouvelle connexion de {client_address}")
            with open('logs.txt', "a") as fichier:
                fichier.write(f"Nouvelle connexion de {client_address}\n")
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

    def private_message(self, username, content, destinataire):
        for client in self.clients:
            try:
                if client.username == username:
                    message = "(MP) "+ destinataire +" : "+ content
                    client.client_socket.sendall(message.encode('utf-8'))
            except Exception as e:
                print(f"Erreur lors de l'envoi du message privé au client {client.client_address}: {e}")
               

    def create_group_message(self, sender, msg):
        print(msg)
        parts = msg.split(" ")
        clients_to_add = []
        print(parts)
        for client in self.clients:
            try:
                if client.username in parts:
                    clients_to_add.append(client.username)
            except Exception as e:
                print(f"Erreur lors de la création de groupe : {client.client_address}: {e}")
        # Faire quelque chose avec la liste clients_to_add
        client_names = ",".join(clients_to_add)
        real_c = client_names.split(",")
        print (real_c)
        print (clients_to_add)
        for client in self.clients:
            print (client.username+"    test")
            if client.username in real_c:
                try:
                    message = "(Group) "+ sender +" a créer un groupe contanant : "+ client_names
                    client.client_socket.sendall(message.encode('utf-8'))
                except Exception as e:
                    print(f"Erreur lors de la création de groupe : {client.client_address}: {e}")
            


    def remove_client(self, client):
        if client in self.clients:
            self.clients.remove(client)
            client.client_socket.close()
            print(f"Le client {client.client_address} s'est déconnecté.")
            with open('logs.txt', "a") as fichier:
                fichier.write(f"Nouvelle connexion de {client.client_address}\n")

    def stop(self):
        for client in self.clients:
            client.client_socket.close()
        self.server_socket.close()
        print("Le serveur de chat s'est arrêté.")
