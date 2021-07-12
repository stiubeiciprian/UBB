package utils;

import java.util.ArrayList;
import java.lang.Math;

public class HashTable<K, V> {
    private ArrayList<Node<K, V>> table;
    private int capacity;
    private int currentSize;

    /**
     * Creates a new hash table of given capacity.
     * @param capacity
     */
    public HashTable(int capacity) {
        this.table = new ArrayList<>();
        this.capacity = capacity;
        this.currentSize = 0;

        for (int i = 0; i < this.capacity; i++) {
            table.add(null);
        }
    }

    /**
     * Returns the position of a key in the table list.
     * @param key
     */
    private int position(K key) {
        int hashCode = Math.abs(key.hashCode());
        return hashCode % capacity;
    }

    /**
     *  Returns the value of a given key or null otherwise.
     * @param key
     */
    public V get(K key) {
        int position = position(key);
        Node<K, V> head = table.get(position);

        while(head != null) {
            if(head.getKey().equals(key)) {
                return head.getValue();
            }
            head = head.getNextNode();
        }

        return null;
    }

    /**
     *  Adds a new key, value pair to the hash table.
     * @param key
     * @param value
     */
    public void add(K key, V value) {
        int position = position(key);
        Node<K, V> head = table.get(position);

        while (head != null) {
            if(head.getKey().equals(key)) {
                head.setValue(value);
                return;
            }
            head = head.getNextNode();
        }

        this.currentSize++;
        head = table.get(position);
        Node<K, V> newNode = new Node<>(key, value);
        newNode.setNextNode(head);
        table.set(position, newNode);
    }

    /**
     * Checks if the given key exists in the hash table.
     * @param key
     */
    public boolean contains(K key) {
        int position = position(key);
        Node<K, V> head = table.get(position);

        while (head != null) {
            if(head.getKey().equals(key)) {
                return true;
            }
            head = head.getNextNode();
        }
        return false;
    }

    /**
     * Returns the size of the hash table.
     * @return size of collection
     */
    public int getCurrentSize() {
        return currentSize;
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();

        for ( Node<K, V> node: table) {
            while (node != null) {
                s.append(node.getValue()).append("\t|").append(node.getKey()).append("\n");
                node = node.getNextNode();
            }
        }

        return s.toString();
    }
}
