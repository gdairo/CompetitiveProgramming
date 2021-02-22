import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;

public class Freopen {
    
    private static final String INPUT = "in.txt";
    private static final String OUTPUT = "out.txt";
    
    public static FileInputStream inStream() {
        try {
            return new FileInputStream(INPUT);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return null;
    }

    public static PrintStream outStream() {
        try {
            return new PrintStream(new FileOutputStream(OUTPUT));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return null;
    }
}
