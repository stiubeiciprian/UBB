public class Transition {
    private String source;
    private String destination;
    private String symbol;

    public Transition(String source, String destination, String symbol) {
        this.source = source;
        this.destination = destination;
        this.symbol = symbol;
    }

    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }

    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    @Override
    public String toString() {
        return "d(" + source + ", " + symbol + ") = " + destination;
    }
}
