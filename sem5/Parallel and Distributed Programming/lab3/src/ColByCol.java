public class ColByCol implements Runnable{
    private int startPosition;
    private int endPosition;


    public ColByCol(int startPosition,int endPosition) {
        this.startPosition = startPosition;
        this.endPosition = endPosition;
    }

    /**
     * Each task computes consecutive elements, going column after column.
     * This is like the previous example, but interchanging the rows with the columns: task 0 takes columns 0 and 1, plus elements 0 and 1 from column 2, and so on.
     */
    @Override
    public void run() {
        for (int i = startPosition; i < endPosition; i++) {
            Program.AB[i % Program.COLS_B][i / Program.COLS_B] = Program.computeElement(i % Program.COLS_B, i / Program.COLS_B);
        }
    }
}
