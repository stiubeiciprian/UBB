
public class SymbolTable {
    HashTable<String, Integer> hashTable;
    public SymbolTable() {
        this.hashTable = new HashTable<>(10);
    }

    /**
     * Returns the position of a given token in the symbol table.
     * @param token
     */
    public Integer pos(String token) {
        if(hashTable.contains(token)) {
            return hashTable.get(token);
        }
        return this.add(token);
    }

    /**
     * Adds a given token to the symbol table.
     * @param token
     */
    public Integer add(String token) {
        Integer position = hashTable.getCurrentSize() + 1;
        hashTable.add(token, position);
        return position;
    }
}
