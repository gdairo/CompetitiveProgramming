import java.io.*;
import java.util.Scanner;

class Exer {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        FileInputStream inStream = null;
        PrintStream outStream = null;

        try {
            inStream = new FileInputStream("in.txt");
            outStream = new PrintStream(new FileOutputStream("out.txt"));

            System.setIn(inStream);
            System.setOut(outStream);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            System.out.printf("%7.3f%n", sc.nextDouble());
        }

        sc.close();
        return;
    }
}