package ClientServer.model;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.text.ParseException;

public class Client {
    private String pseudo;

    public String getPseudo() {
        return pseudo;
    }

    public void setPseudo(String pseudo) throws ParseException {
        Pattern pat = Pattern.compile("(?s)(?!.{21})\\s*\\S.*");
        Matcher test = pat.matcher(pseudo);
        if (test.matches()) {
            this.pseudo = pseudo;
        } else {
            throw new ParseException("Pseudo Incorrect", 0);
        }
    }
}
