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

    public static void main(String[] args) throws Exception {
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

    public static void Chat() {
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

    public static void connectServer(Client c) {
        final String SERVER_IP = "10.57.33.126";
        final int SERVER_PORT = 2222;
        try {
            Socket client_socket = new Socket(SERVER_IP, SERVER_PORT);
            System.out.println("Connexion établie avec le serveur.");
            

            PrintWriter out = new PrintWriter(client_socket.getOutputStream(), true);
            // Envoyer la chaîne de caractères
            
            out.println(c.getPseudo());
            MainChat(client_socket,c);
            
        } catch (IOException e) {
            System.out.println("Erreur : " + e.getMessage());
        }
    }

    public static void MainChat(Socket clientSocket, Client c) throws IOException {
        afficherMenu2();
        while (true) {
            try {
                clientSocket.setSoTimeout(500); // délai d'attente de 500 millisecondes
                BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                String message = in.readLine();
                if (message != null) {
                    System.out.println(message);
                }
            } catch (SocketTimeoutException e) {
                // rien n'a été reçu sur le flux d'entrée, poursuivre l'exécution
            }
            String choix = scan.nextLine();
            switch (choix) {

                case "/private":
                    Chat();
                    break;
                default:
                    String Message = choix;
                    System.out.println("En effet");
                    ChatGeneral(clientSocket,c,choix);
                    break;
            }
            afficherMenu2();
        }
    }

    public static void ChatGeneral(Socket client_socket, Client c, String choix) throws IOException {
        
        try {
            PrintWriter out = new PrintWriter(client_socket.getOutputStream(), true);
                
                
                out.println(c.getPseudo()+" : "+choix);
                System.out.println("message envoyé");
            } catch (IOException e) {
                System.out.println("Erreur : " + e.getMessage());
            }
    }
    

    public static void afficherMenu() {
        ArrayList<String> menus = new ArrayList<>();
        menus.add("-- MENU --");
        menus.add("1- Chat");
        menus.add("q- Quitter");
        for (String s : menus) {
            System.out.println(s);
        }
    }
    public static void afficherMenu2() {
        ArrayList<String> menus = new ArrayList<>();
        menus.add(" ");
        menus.add("Vous pouvez écrire ci-dessous dans le chat général ou faire /private pour envoyer un message privé");
        menus.add("");
        for (String s : menus) {
            System.out.println(s);
        }
    }
}