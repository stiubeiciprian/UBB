import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class FiniteAutomata {
    private List<String> states;
    private List<String> alphabet;
    private String startingState;
    private List<String> finalStates;
    private List<Transition> transitions;

    public void readFromFile(String filename) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(filename));

        states = Arrays.asList( reader.readLine().split(","));
        alphabet = Arrays.asList(reader.readLine().split(","));
        startingState = reader.readLine();
        finalStates = Arrays.asList(reader.readLine().split(","));

        String line = reader.readLine();
        transitions = new ArrayList<>();
        while (line != null) {
            String[] transition = line.split(",");

            String source = transition[0];
            String destination = transition[1];
            String symbol = transition[2];

            transitions.add(new Transition(source, destination, symbol));

            line = reader.readLine();
        }
    }

    public boolean checkSequence(String sequence) {
        String currentState = startingState;

        String[] characters = sequence.split("");
        for (String symbol: characters) {
            try {
                String nextState = nextState(currentState, symbol);

                if (nextState.equals("")) {
                    return false;
                }

                currentState = nextState;

            } catch (NondeterministicException e) {
                System.out.println("Finite automata is nondeterministic.");
                return false;
            }
        }

        return finalStates.contains(currentState);
    }

    private String nextState(String source, String symbol) throws NondeterministicException {
        List<Transition> nextStates = transitions.stream().filter(t -> t.getSource().equals(source) && t.getSymbol().equals(symbol)).collect(Collectors.toList());

        if (nextStates.size() == 1) {
            return nextStates.get(0).getDestination();
        }

        if (nextStates.size() > 1) {
            throw new NondeterministicException("Finite automata is not deterministic.");
        }

        return "";
    }

    public List<String> getStates() {
        return states;
    }

    public List<String> getAlphabet() {
        return alphabet;
    }

    public String getStartingState() {
        return startingState;
    }

    public List<String> getFinalStates() {
        return finalStates;
    }

    public List<Transition> getTransitions() {
        return transitions;
    }
}
