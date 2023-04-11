import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.util.Scanner;
public class Client {
    private static Scanner scan = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        afficherMenu();
        while (true) {
            String choix = scan.nextLine();
            switch (choix) {
                case "1":
                    ajouterContact();
                    break;
                case "2":
                    listerContact();
                    break;
                case "3":
                    listerContact();
                    deleteContact();
                    break;
                case "4":
                    listerContact();
                    modifContact();
                    break;
                case "5":
                    listerContact();
                    searchContact1();
                    break;
                case "6":
                    sortAContact();
                    break;
                case "7":
                    sortDate();
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
    public static void afficherMenu() {
        ArrayList<String> menus = new ArrayList<>();
        menus.add("-- MENU --");
        menus.add("1- Ajouter un contact");
        menus.add("2- Lister les contacts");
        menus.add("3- Supprimer un contact");
        menus.add("4- Modifier un contact");
        menus.add("5- Rechercher un contact sur nom");
        menus.add("6- Trier les contacts");
        menus.add("7- Trier les contacts par date");
        menus.add("q- Quitter");
        for (String s : menus) {
            System.out.println(s);
        }
    }
}