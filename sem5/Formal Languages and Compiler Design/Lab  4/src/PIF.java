import utils.Pair;

import java.util.ArrayList;

/**
 * Program Internal Form
 *      collection of pairs of (key, value) where:
 *          - the key is a operator, reserved keyword, separator, code for constant(1) or code for identifier(0);
 */
public class PIF {
    private ArrayList<Pair<String, Integer>> pif;

    public PIF() {
        this.pif = new ArrayList<>();
    }

    /**
     * Add key to program internal form.
     * @param key
     *        key to be added to the program internal form
     * @param value
     *        value to be added to the program internal form
     *        
     */
    public void add(String key, Integer value) {
        pif.add(new Pair<>(key, value));
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        for (Pair<String, Integer> pair: pif) {
            s.append(pair.toString()).append("\n");
        }
        return s.toString();
    }
}
