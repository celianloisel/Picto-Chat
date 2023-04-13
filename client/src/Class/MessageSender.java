package src.Class;

import java.io.PrintWriter;

public class MessageSender {
    private String username;
    private PrintWriter out;

    public MessageSender(String username, PrintWriter out) {
        this.username = username;
        this.out = out;
    }

    public void sendMessage(String message) {
        // Envoyer le message au serveur
        out.println(username + ": " + message);
    }

    public void privateMessage(String message){
        out.println(username + ": " + message);
    }
}
