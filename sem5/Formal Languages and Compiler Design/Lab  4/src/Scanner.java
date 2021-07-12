import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class Scanner {

    public static final String code_for_identifiers = "0";
    public static final String code_for_constants = "1";
    private PIF pif;
    private SymbolTable symbolTable;
    private String filename;

    /**
     * Construct a scanner for a given file.
     * @param filename
     *        path to file containing program for scanning
     */
    public Scanner(String filename) {
        this.pif = new PIF();
        this.symbolTable = new SymbolTable();
        this.filename = filename;
    }

    /**
     * Save program internal form to given file.
     * @param filename
     *        path to file for writing the program internal form
     * @throws IOException if {@code filename} cannot be written
     */
    public void saveProgramInternalFormToFile(String filename) throws IOException {
        FileWriter fileWriter = new FileWriter(filename);
        fileWriter.write(pif.toString());
        fileWriter.close();
    }

    /**
     * Save symbol table to given file.
     * @param filename
     *        path to file for writing the symbol table
     * @throws IOException if {@code filename} cannot be written
     */
    public void saveSymbolTableToFile(String filename) throws IOException {
        FileWriter fileWriter = new FileWriter(filename);
        fileWriter.write(symbolTable.toString());
        fileWriter.close();
    }

    /**
     * Scans program from given file and creates its symbol table and program internal form.
     * The scanning stops and prints a message if it encoutners a lexical error.
     * If the program is lexically correct, a message is printed and the pif is returned.
     * @return {@code PIF} program internal form
     * @throws IOException if file cannot be read
     */
    public PIF scan() throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(filename));
        String line = reader.readLine();
        int lineIndex = 1;

        while (line != null) {
            Queue<String> tokens = detect(line);

            while(!tokens.isEmpty()) {
                String token = tokens.remove();
                if (isReservedKeyword(token) || isOperator(token) || isSeparator(token)) {
                    token = token.equals("\t") ? "TAB" : token;
                    token = token.equals(" ") ? "SPC" : token;
                    pif.add(token, 0);
                } else {
                    if (isIdentifier(token)) {
                        int index = symbolTable.pos(token);
                        pif.add(code_for_identifiers, index);
                    } else {
                        if(isConstant(token)) {
                            int index = symbolTable.pos(token);
                            pif.add(code_for_constants, index);
                        } else {

                            token = token.equals("\t") ? "TAB" : token;
                            token = token.equals(" ") ? "SPC" : token;
                            System.out.println("Lexical error found at line " + lineIndex + ": " + token );
                            return pif;
                        }
                    }
                }
            }

            // Since readLine consumes the end of line character, it needs to be added to the pif manually
            pif.add("EOL", 0);

            line = reader.readLine();
            lineIndex++;
        }
        
        System.out.println("Lexically correct.");
        return pif;
    }

    /**
     * Returns a queue of tokens detected in the given line.
     * @param line
     *        the line for detecting tokens
     * @return queue of detected tokens
     */
    private Queue<String> detect(String line) {
        Queue<String> tokens = new LinkedList<>();

//      [\'][^\']*[\']|["][^"]*["]    match string/char sequence
//      [\s,;:()\[\]]                 matches separators
//      \+\+|--|>=|==|<=|!=           matches double character operators
//      [0-9a-zA-Z_]+                 match alphabet sqeuence
//      (?<=[A-Za-z0-9])\s*+[+-]      match +/- operator, matches if identifier/constant number precedes it
//      [+-]?[1-9]{1}[0-9]*           match constant numbers
//      [+\-*\/%=<>]                  matches single character operators
//      .+                            matches any other sequence of characters
        String regex = "[\\'][^\\']*[\\']|[\"][^\"]*[\"]|[\\s,;:()\\[\\]]|\\+\\+|--|>=|==|<=|!=|[0-9a-zA-Z_]+|(?<=[A-Za-z0-9 ])[+-]|[+-]?[1-9]{1}[0-9]*|[+\\-*\\/%=<>]|.+";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(line);

        while (matcher.find()) {
            tokens.add(matcher.group(0));
        }

        return tokens;
    }

    /**
     * Returns {@code true} if {@param token} is a separator.
     *
     * @param token
     *        the token to be checked
     *
     * @return {@code true} if {@param token} is a separator
     */
    private boolean isSeparator(String token) {
        return token.matches("^[\\s,;:()\\[\\]]$");
    }

    /**
     * Returns {@code true} if {@param token} is a separator.
     *
     * @param token
     *        the token to be checked
     *
     * @return {@code true} if {@param token} is a separator
     */
    private boolean isOperator(String token) {
        return token.matches("^[!=<>]=$|^\\+\\+$|^\\-\\-$|^[\\+\\-*\\/%=<>]$|^and$|^or$|^not$");
    }

    /**
     * Returns {@code true} if {@param token} is a separator.
     *
     * @param token
     *        the token to be checked
     *
     * @return {@code true} if {@param token} is a separator
     */
    private boolean isReservedKeyword(String token) {
        return token.matches("^int$|^bool$|^char$|^string$|^if$|^else$|^elif$|^input$|^print$|^while$|^for$");
    }

    /**
     * Returns {@code true} if {@param token} is an identifier.
     * An identifier is formed using letters (lowercase and uppercase), digits and '_' (underscore).
     *      * But it's first character must be a letter or '_' (underscore).
     *
     * @param token
     *        the token to be checked
     *
     * @return {@code true} if {@param token} is an identifier
     */
    private boolean isIdentifier(String token) {
        return token.matches("^[a-zA-Z_]+[0-9a-zA-Z_]*$");
    }

    /**
     * Returns {@code true} if {@param token} is a constant.
     * Consants can be characters, strings or integer numbers (e.g. 'c', "string", -132).
     *
     * @param token
     *        the token to be checked
     *
     * @return {@code true} if {@param token} is a constant
     */
    private boolean isConstant(String token) {
        return token.matches("^0|[+-]?[1-9]{1}[0-9]*$") || token.matches("^\".*\"$|^\\'.\\'$");
    }
    
}
