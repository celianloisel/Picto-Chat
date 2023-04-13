package src.Class;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class ChatClient implements Runnable {
    private final String host;
    private final int port;
    private String username;
    private Socket socket;
    private BufferedReader in;
    private PrintWriter out;


    public ChatClient(String host, int port) {
        this.host = host;
        this.port = port;
    }

    public String getUsername() {
        return this.username;
    }

    public PrintWriter getOut() {
        return out;
    }


    public void connect() throws IOException {
        InterfaceGraphique interfaceGraphique = new InterfaceGraphique();

        // Connexion au serveur
        socket = new Socket(host, port);
        System.out.println("Connecté au serveur : " + host + ":" + port);

        // Création des flux d'entrée et de sortie
        in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        out = new PrintWriter(socket.getOutputStream(), true);

        while (interfaceGraphique.getPseudo() == null) {
            try {
                Thread.sleep(1000); // Attendre 1 seconde
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        username = interfaceGraphique.getPseudo();

        // Envoyer le nom d'utilisateur au serveur
        out.println(username);

        // Attendre la réponse du serveur
        String response = in.readLine();
        if ("OK".equals(response)) {
            interfaceGraphique.NextFrame(username, out, in);
            interfaceGraphique.ajouterPersonne(username);
        } else {
            System.out.println("Le nom d'utilisateur " + username + " est déjà utilisé. Veuillez en choisir un autre.");
            // Fermer la connexion au serveur
            socket.close();
            interfaceGraphique.closeFrame();
            connect();
        }
    }

    public void receiveMessage() throws IOException {
        // Recevoir les messages du serveur
        String message;
        while ((message = in.readLine()) != null) {
            System.out.println(message);
        }
    }

    public void close() throws IOException {
        // Fermeture des flux et de la connexion
        in.close();
        out.close();
        socket.close();
    }

    @Override
    public void run() {
        try {
            // Thread pour recevoir les messages du serveur
            receiveMessage();
        } catch (IOException e) {
            System.err.println("Erreur lors de la réception des messages : " + e.getMessage());
        }
    }
}
