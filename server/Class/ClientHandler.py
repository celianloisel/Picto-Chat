import threading


class ClientHandler(threading.Thread):
    def __init__(self, client_socket, client_address, server):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.client_address = client_address
        self.server = server
        

    def run(self):
        username = self.client_socket.recv(1024).decode('utf-8').strip()
        self.username = username
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
                if "/mp" in data:
                    parts = data.split(" ", 4)
                    print(parts)import threading


class ClientHandler(threading.Thread):
    """
    Classe pour gérer les connexions clientes dans un serveur de chat.

    Attributes:
        client_socket (socket.socket): Le socket de la connexion cliente.
        client_address (tuple): L'adresse IP et le port du client.
        server (Server): L'instance du serveur de chat.
        username (str): Le nom d'utilisateur du client.
    """

    def __init__(self, client_socket, client_address, server):
        """
        Initialise une nouvelle instance de la classe ClientHandler.

        Args:
            client_socket (socket.socket): Le socket de la connexion cliente.
            client_address (tuple): L'adresse IP et le port du client.
            server (Server): L'instance du serveur de chat.
        """
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.client_address = client_address
        self.server = server
        self.username = None

    def run(self):
        """
        Méthode exécutée en tant que thread pour gérer la connexion cliente.

        La méthode gère la réception des données du client, la vérification du nom d'utilisateur,
        l'envoi des réponses au client, la diffusion des messages aux autres clients connectés,
        et la gestion des messages privés et de groupe.
        """
        username = self.client_socket.recv(1024).decode('utf-8').strip()
        self.username = username
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
                if "/mp" in data:
                    parts = data.split(" ", 4)
                    print(parts)
                    dest = parts[0]
                    pseudo = parts[3]
                    mp = parts[4]
                    self.server.private_message(pseudo, mp, dest)

                elif "/group" in data:
                    parts = data.split(" ")
                    pseudo = parts[0]
                    self.server.create_group_message(pseudo, data)

                elif data:
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
        """
        Vérifie si un nom d'utilisateur est déjà utilisé par un autre client.

        Args:
            username (str): Le nom d'utilisateur à vérifier.

        Returns:
            bool: True si le nom d'utilisateur est déjà utilisé, sinon False.
        """
        print(self.server.get_username())
        if username in self.server.get_username():
            return True
        else:
            return False

    def send_message_to_user(self, username, message):

                    dest = parts[0]
                    pseudo = parts[3]
                    mp = parts[4]
                    self.server.private_message(pseudo,mp,dest)
                    
                elif "/group" in data:
                    parts = data.split(" ")
                    pseudo = parts[0]
                    self.server.create_group_message(pseudo,data)

                elif data:
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
        
    def send_message_to_user(self, username, message):
        with self._lock:
            for connection in self._connections:
                try:
                    user_name = connection.recv(20).decode()
                    if user_name == username:
                        connection.sendall(message.encode())
                        break
                except Exception as e:
                    print(f"Error sending message to user {username}: {e}")