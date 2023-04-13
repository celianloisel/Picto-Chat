package src;

import src.Class.ChatClient;
import src.Class.MessageSender;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        String host = "192.168.1.106"; // Adresse IP du serveur
        int port = 2222; // Port du serveur

        ChatClient chatClient = new ChatClient(host, port);
        chatClient.connect();

        // Lancer le client dans un thread séparé
        Thread clientThread = new Thread(chatClient);
        clientThread.start();
    }
}
