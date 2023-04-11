import java.io.IOException;
import java.net.Socket;
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
                connectServer();
                break;
            } catch (ParseException e) {
                System.out.println(e.getMessage());
            }
        } while (true);
    }

    public static void connectServer() {
        final String SERVER_IP = "10.57.32.3";
        final int SERVER_PORT = 2222;
        try {
            Socket client_socket = new Socket(SERVER_IP, SERVER_PORT);
            System.out.println("Connexion établie avec le serveur.");
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
}