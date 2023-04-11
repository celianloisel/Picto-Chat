import socket

# Adresse IP et port du serveur de chat
SERVER_IP = '10.57.32.3'
SERVER_PORT = 2222

# Création d'un objet de socket pour le client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connexion au serveur
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print("Connexion établie avec le serveur.")

    # Envoyer des données au serveur
    client_socket.sendall(b"Hello, serveur!")

    # Recevoir les données du serveur
    data = client_socket.recv(1024)
    print(f"Reçu du serveur : {data.decode()}")

    # Fermer la connexion
    client_socket.close()

except Exception as e:
    print(f"Erreur : {e}")
    client_socket.close()
