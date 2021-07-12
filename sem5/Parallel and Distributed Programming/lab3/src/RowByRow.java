public class RowByRow implements Runnable {
    private int startPosition;
    private int endPosition;


    public RowByRow(int startPosition,int endPosition) {
        this.startPosition = startPosition;
        this.endPosition = endPosition;
    }

    /**
     * Each task computes consecutive elements, going row after row.
     *
     * So, task 0 computes rows 0 and 1, plus elements 0-1 of row 2 (20 elements in total);
     * task 1 computes the remainder of row 2, row 3, and elements 0-3 of row 4 (20 elements);
     * task 2 computes the remainder of row 4, row 5, and elements 0-5 of row 6 (20 elements);
     * finally, task 3 computes the remaining elements (21 elements).
     *
     */
    @Override
    public void run() {
        for (int i = startPosition; i < endPosition; i++) {
                Program.AB[i / Program.COLS_B][i % Program.COLS_B] = Program.computeElement(i / Program.COLS_B, i % Program.COLS_B);
        }
    }
}