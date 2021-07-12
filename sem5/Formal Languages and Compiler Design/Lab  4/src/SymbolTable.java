import utils.HashTable;

public class SymbolTable {
    private HashTable<String, Integer> hashTable;
    public SymbolTable() {
        this.hashTable = new HashTable<>(10);
    }

    /**
     * Returns the position of a given token in the symbol table.
     * If the token is not found in the symbol table it adds it then returns the position.
     * @param token token to be searched and/or inserted in the symbol table
     * @return position of token in the symbol table
     */
    public Integer pos(String token) {
        if(hashTable.contains(token)) {
            return hashTable.get(token);
        }
        return this.add(token);
    }

    /**
     * Adds a given token to the symbol table.
     * @param token token to be added to the symbol table
     * @return position of added token
     */
    public Integer add(String token) {
        Integer position = hashTable.getCurrentSize() + 1;
        hashTable.add(token, position);
        return position;
    }

    @Override
    public String toString() {
        return hashTable.toString();
    }
}
