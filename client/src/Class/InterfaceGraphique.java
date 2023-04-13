package src.Class;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.PrintWriter;
import java.util.Objects;


public class InterfaceGraphique {

    private String pseudo;
    private JFrame frame;
    private JPanel pseudoPanel;
    private JTextField pseudoTextField;
    private JButton choisirPseudoButton;
    private JTextField textField;
    private JTextArea textArea;
    private JList<String> personList;
    private DefaultListModel<String> personListModel;
    private JPopupMenu popupMenu;

    public String getPseudo() {
        return pseudo;
    }

    public void closeFrame() {
        frame.dispose();
    }

    public void NextFrame(String pseudo, PrintWriter out, BufferedReader in) throws IOException {
        choisirPseudoButton.setEnabled(false);
        frame.remove(pseudoPanel);
        frame.revalidate();
        frame.repaint();
        initChatInterface(pseudo, out, in);
    }

    public InterfaceGraphique() {
        // Créer la fenêtre principale
        frame = new JFrame("Interface Graphique");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 400);

        // Créer le panneau pour choisir le pseudo
        pseudoPanel = new JPanel();
        pseudoTextField = new JTextField(10);
        choisirPseudoButton = new JButton("Choisir Pseudo");
        choisirPseudoButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (!Objects.equals(pseudoTextField.getText(), "")) {
                    pseudo = pseudoTextField.getText();
                }
            }
        });
        pseudoPanel.add(new JLabel("Pseudo : "));
        pseudoPanel.add(pseudoTextField);
        pseudoPanel.add(choisirPseudoButton);

        // Ajouter le panneau pour choisir le pseudo à la fenêtre
        frame.setLayout(new BorderLayout());
        frame.add(pseudoPanel, BorderLayout.CENTER);

        // Afficher la fenêtre
        frame.setVisible(true);
    }

    public void initChatInterface(String pseudo, PrintWriter out, BufferedReader in) throws IOException {
        // Créer le champ de texte pour l'input
        textField = new JTextField();
        textField.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String message = textField.getText();
                MessageSender messageSender = new MessageSender(pseudo, out);
                messageSender.sendMessage(message);
            }
        });

        // Créer la zone pour afficher les messages
        textArea = new JTextArea();
        textArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(textArea);

        // Créer la liste de personnes
        personListModel = new DefaultListModel<String>();
        personList = new JList<String>(personListModel);
        personList.addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent e) {
                if (e.getButton() == MouseEvent.BUTTON3) {
                    personList.setSelectedIndex(personList.locationToIndex(e.getPoint()));
                    popupMenu.show(personList, e.getX(), e.getY());
                }
            }
        });

        // Créer le menu contextuel pour la liste de personnes
        popupMenu = new JPopupMenu();
        JMenuItem menuItem = new JMenuItem("Envoyer un message");
        menuItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String selectedPerson = personList.getSelectedValue();
                textArea.append(selectedPerson + ": Bonjour!\n");
            }
        });
        popupMenu.add(menuItem);

        // Ajouter les composants à la fenêtre
        frame.setLayout(new BorderLayout());
        frame.add(textField, BorderLayout.NORTH);
        frame.add(scrollPane, BorderLayout.CENTER);
        frame.add(personList, BorderLayout.EAST);

        // Afficher la fenêtre
        frame.setVisible(true);

        while (true) {
            String message = in.readLine();
            if (message == null) {
                // Si le message est null, cela signifie que la connexion avec le serveur a été interrompue
                // Fermer l'interface graphique
                frame.dispose();
                break;
            } else {
                // Ajouter le message reçu à la zone de texte
                textArea.append(message + "\n");
            }
        }
    }

    public void ajouterPersonne(String personne) {
        personListModel.addElement(personne);
    }
}
