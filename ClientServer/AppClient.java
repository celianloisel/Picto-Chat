import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.SocketTimeoutException;
import java.text.ParseException;
import java.util.ArrayList;

import java.util.Scanner;
import model.Client;

public class AppClient {
    private static Scanner scan = new Scanner(System.in);

    public  void main(String[] args) throws Exception {
        afficherMenu();
        while (true) {
            String choix = scan.nextLine();
            switch (choix) {

                case "1":
                    Chat();
                    break;
                case "q":
                    scan.close();
                    return;
                default:
                    System.out.println("Boulet!!!!");
                    break;
            }
            afficherMenu();
        }
    }

    public void Chat() {
        Client c = new Client();
        do {
            try {
                System.out.println("Saisir pseudo:");
                c.setPseudo(scan.nextLine());
                connectServer(c);
                break;
            } catch (ParseException e) {
                System.out.println(e.getMessage());
            }
        } while (true);
    }

    public void connectServer(Client c) {
        final String SERVER_IP = "10.57.33.126";
        final int SERVER_PORT = 2222;
        try {
            Socket client_socket = new Socket(SERVER_IP, SERVER_PORT);
            System.out.println("Connexion établie avec le serveur.");
    
            PrintWriter out = new PrintWriter(client_socket.getOutputStream(), true);
            // Envoyer la chaîne de caractères
            out.println(c.getPseudo());
    
            // Lancer un thread pour la lecture des messages du serveur
            new Thread(() -> {
                try {
                    BufferedReader in = new BufferedReader(new InputStreamReader(client_socket.getInputStream()));
                    String message;
                    while ((message = in.readLine()) != null) {
                        System.out.println(message);
                    }
                } catch (IOException e) {
                    System.out.println("Erreur : " + e.getMessage());
                }
            }).start();
    
            // Boucle pour les entrées utilisateur
            afficherMenu2();
            while (true) {
                String choix = scan.nextLine();
                switch (choix) {
                    case "/private":
                        Chat();
                        break;
                    default:
                        ChatGeneral(client_socket, c, choix);
                        break;
                }
                
            }
        } catch (IOException e) {
            System.out.println("Erreur : " + e.getMessage());
        }
    }
    
    public  void ChatGeneral(Socket client_socket, Client c, String choix) {
        try {
            PrintWriter out = new PrintWriter(client_socket.getOutputStream(), true);
            out.println(c.getPseudo() + " : " + choix);
            
        } catch (IOException e) {
            System.out.println("Erreur : " + e.getMessage());
        }
    }
    
    

    public void afficherMenu() {
        ArrayList<String> menus = new ArrayList<>();
        menus.add("-- MENU --");
        menus.add("1- Chat");
        menus.add("q- Quitter");
        for (String s : menus) {
            System.out.println(s);
        }
    }
    public void afficherMenu2() {
        ArrayList<String> menus = new ArrayList<>();
        menus.add(" ");
        menus.add("Vous pouvez écrire ci-dessous dans le chat général ou faire /private pour envoyer un message privé");
        menus.add("");
        for (String s : menus) {
            System.out.println(s);
        }
    }
}