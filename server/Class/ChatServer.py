import socket

class ChatServer:
    MAX_CONNECTIONS = 5

    def __init__(self, port):
        self._port = port

    def get_port(self):
        return self._port

    def set_port(self, new_value):
        self._port = new_value

    def execute(self):
        # Création d'un objet de socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # Liaison du socket à une adresse IP (10.57.32.3) et un port spécifique
            server_socket.bind(('10.57.32.3', int(self._port)))
            # Mise en écoute du socket avec un nombre maximum de connexions acceptées (5)
            server_socket.listen(ChatServer.MAX_CONNECTIONS)
            print(f"Le serveur écoute sur le port {self._port}")
            while True:
                try:
                    # Acceptation des connexions entrantes des clients
                    client_socket, client_address = server_socket.accept()
                    print(f"Connexion établie depuis {client_address}")
                    # Ajouter du code pour gérer les connexions clients
                except KeyboardInterrupt:
                    # Gestion de l'arrêt du serveur par l'utilisateur
                    print("Arrêt du serveur par l'utilisateur.")
                    break
                except Exception as e:
                    # Gestion des autres exceptions possibles
                    print(f"Erreur : {e}")
