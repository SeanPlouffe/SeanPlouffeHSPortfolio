/*
Name: Sean Plouffe
Description: This program reads from a text file and puts in a map the name as a key and a password as a value
the user can then guess the password
*/

package Unit_11_2;

import java.io.*;
import java.util.*;

public class Main
{

    public static void main(String[] args) throws FileNotFoundException
    {
        File magicWordsFile = new File("txtFiles\\2_lotrMagicWord.txt");
        Map<String, String> magicWordMap;

        magicWordMap = loadFileToMap(magicWordsFile);

        if(magicWordMap == null)
        {
            return;
        }

        String user = getRandomKey(magicWordMap);

        Scanner userInput = new Scanner(System.in);

        System.out.println("Enter password for " + user);
        String inputName = userInput.nextLine();

        while(!inputName.equalsIgnoreCase("stop") && !inputName.equals(magicWordMap.get(user)))
        {
            System.out.println("Wrong, keep trying");
            inputName = userInput.nextLine();
        }

        System.out.println("Correct");

    }

    private static String getRandomKey(Map<String, String> map)
    {

        int randomNumber = (int) (Math.random() * map.size());

        return map.keySet().toArray()[randomNumber].toString();

    }

    private static Map<String, String> loadFileToMap(File magicWordsFile) throws FileNotFoundException
    {
        try {
            if (!magicWordsFile.exists()) {
                return null;
            }

            Map<String, String> magicWordMap = new TreeMap<>();

            Scanner fileInput = new Scanner(magicWordsFile);

            while(fileInput.hasNextLine())
            {
                String currLine = fileInput.nextLine();

                if(currLine.contains(":"))
                {
                    String[] parts = fileInput.nextLine().split(":");
                    String name = parts[0];
                    String magicWord = parts[1];

                    magicWordMap.putIfAbsent(name, magicWord);
                }
            }

            return magicWordMap;

        }
        catch(FileNotFoundException e)
        {
            System.out.println("FileNotFoundException in loadFileToMap");
            return null;
        }
    }

}
