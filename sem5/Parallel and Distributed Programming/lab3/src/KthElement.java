public class KthElement implements Runnable {
    private int startPosition;

    public KthElement(int startPosition) {
        this.startPosition = startPosition;
    }

    /**
     * Each task takes every k-th element (where k is the number of tasks), going row by row. So, task 0 takes elements (0,0), (0,4), (0,8), (1,3), (1,7), (2,2), (2,6), (3,1), (3,5), (4,0), etc.
     */
    @Override
    public void run() {
        int length = Program.ROWS_A * Program.COLS_B;
        int i = startPosition;
        while(i < length) {
            Program.AB[i / Program.COLS_B][i % Program.COLS_B] = Program.computeElement(i / Program.COLS_B, i % Program.COLS_B);
            i += Program.NUMBER_OF_TASKS;
        }
    }
}
