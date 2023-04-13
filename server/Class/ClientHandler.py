import threading


class ClientHandler(threading.Thread):
    def __init__(self, client_socket, client_address, server):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.client_address = client_address
        self.server = server

    def run(self):
        username = self.client_socket.recv(1024).decode('utf-8')
        print(f"Nom d'utilisateur reçu : {username}")

        # Vérifier si le nom d'utilisateur est déjà utilisé
        if self.check_username(username):
            # Envoyer une réponse négative au client
            self.client_socket.sendall("NOK\n".encode('utf-8'))
        else:
            # Ajouter le nom d'utilisateur à la liste des pseudonymes des clients connectés
            self.server.get_username().append(username)
            # Envoyer une réponse positive au client
            self.client_socket.sendall("OK\n".encode('utf-8'))

        # Continuer le traitement des données du client
        while True:
            try:
                # Recevoir les données du client
                data = self.client_socket.recv(1024).decode('utf-8')
                print(data)
                if data:
                    # Diffuser le message à tous les clients connectés
                    self.server.broadcast(data)
                else:
                    # Si les données sont vides, le client s'est déconnecté
                    self.server.get_username().remove(username)
                    break
            except Exception as e:
                print(f"Erreur lors de la réception des données du client {self.client_address}: {e}")
                self.server.get_username().remove(username)
                break

    def check_username(self, username):
        print(self.server.get_username())
        if username in self.server.get_username():
            return True
        else:
            return False
