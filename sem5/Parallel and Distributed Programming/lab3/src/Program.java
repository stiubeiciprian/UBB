import java.util.ArrayList;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

/**
 * For running the tasks, also implement 2 approaches:
 *
 * Create an actual thread for each task (use the low-level thread mechanism from the programming language);
 * Use a thread pool.
 *
 * Experiment with various values for (and document the attempts and their performance):
 *
 * The sizes of the matrix;
 * The number of tasks (this is equal to the number of threads when not using a thread pool);
 * The number of threads and other parameters for the thread pool (when using the thread pool).
 */
public class Program {
//    static final int ROWS_A = 9, COLS_A = 1, ROWS_B = 1, COLS_B = 9;
//    static int[][] A = {{1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}};
//    static int[][] B = {{1, 2, 3, 4, 5, 6, 7, 8, 9}};

//    static final int ROWS_A = 9, COLS_A = 9, ROWS_B = 9, COLS_B = 9;
//    static int[][] A = {{1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}};
//    static int[][] B = {{1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}};

    static final int ROWS_A = 3, COLS_A = 3, ROWS_B = 3, COLS_B = 3;
    static int[][] A = {{1,0,0},{0,1,0},{0,0,1}};
    static int[][] B = {{9,9,9},{3,3,3},{1,1,1}};

    static int[][] AB = new int[ROWS_A][COLS_B];

    private static final int NUMBER_OF_THREADS = 4;
    static final int NUMBER_OF_TASKS = 4;

    public static void main(String[] args) {
//        executeThreadPoolColByCol();
//        executeColByCol();
//
//        executeThreadPoolRowByRow();
//        executeRowByRow();

        executeThreadPoolKthElement();
//        executeKthElement();
    }


    public static synchronized void setABElement(int value, int row, int col) {
        AB[row][col] = value;
    }

    public static int computeElement(int row, int col) {
        int sum = 0;

        for (int i = 0; i < COLS_A; i++) {
            sum += A[row][i] * B[i][col];
        }
        
        return sum;
    }
    private static void executeRowByRow() {
        ArrayList<Thread> threads = new ArrayList<>();

        int batchSize = ROWS_A * COLS_B / NUMBER_OF_TASKS;
        int startingPosition = 0;
        for (int i = 0; i < NUMBER_OF_TASKS ; i++) {
            int endPosition = Math.min(startingPosition + batchSize + 1, ROWS_A * COLS_B);
            threads.add(new Thread(new RowByRow(startingPosition, endPosition)));
            startingPosition += batchSize;
        }

        long tic, tac;
        tic = System.currentTimeMillis();

        threads.forEach(Thread::start);

        threads.forEach(t -> {
            try {
                t.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        tac = System.currentTimeMillis();
        System.out.println("Number of threads: " + NUMBER_OF_THREADS + "\nTask number (K): " + NUMBER_OF_TASKS + "\nDuration: " + (tac - tic) + "ms.\nResult:");
        printMatrix(AB);
    }

    private static void executeThreadPoolRowByRow() {
        ExecutorService executorService = Executors.newFixedThreadPool(NUMBER_OF_THREADS);

        long tic, tac;
        tic = System.currentTimeMillis();
        int batchSize = ROWS_A * COLS_B / NUMBER_OF_TASKS;
        int startingPosition = 0;
        for (int i = 0; i < NUMBER_OF_TASKS; ++i) {
            int endPosition = Math.min(startingPosition + batchSize + 1, ROWS_A * COLS_B);
            executorService.submit(new RowByRow(startingPosition, endPosition));
            startingPosition += batchSize;
        }

        try {
            if (!executorService.awaitTermination(1, TimeUnit.SECONDS))
                executorService.shutdown();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        tac = System.currentTimeMillis();
        System.out.println("Number of threads: " + NUMBER_OF_THREADS + "\nStep size (K): " + NUMBER_OF_TASKS + "\nDuration: " + (tac - tic) + "ms.\nResult:");
        printMatrix(AB);
    }

    private static void executeColByCol() {
        ArrayList<Thread> threads = new ArrayList<>();

        int batchSize = ROWS_A * COLS_B / NUMBER_OF_TASKS;
        int startingPosition = 0;
        for (int i = 0; i < NUMBER_OF_TASKS ; i++) {
            int endPosition = Math.min(startingPosition + batchSize + 1, ROWS_A * COLS_B);
            threads.add(new Thread(new ColByCol(startingPosition, endPosition)));
            startingPosition += batchSize;
        }

        long tic, tac;
        tic = System.currentTimeMillis();

        threads.forEach(Thread::start);

        threads.forEach(t -> {
            try {
                t.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        tac = System.currentTimeMillis();
        System.out.println("Number of threads: " + NUMBER_OF_THREADS + "\nTask number (K): " + NUMBER_OF_TASKS + "\nDuration: " + (tac - tic) + "ms.\nResult:");
        printMatrix(AB);
    }

    private static void executeThreadPoolColByCol() {
        ExecutorService executorService = Executors.newFixedThreadPool(NUMBER_OF_THREADS);

        long tic, tac;
        tic = System.currentTimeMillis();
        int batchSize = ROWS_A * COLS_B / NUMBER_OF_TASKS;
        int startingPosition = 0;
        for (int i = 0; i < NUMBER_OF_TASKS; ++i) {
            int endPosition = Math.min(startingPosition + batchSize + 1, ROWS_A * COLS_B);
            executorService.submit(new ColByCol(startingPosition, endPosition));
            startingPosition += batchSize;
        }

        try {
            if (!executorService.awaitTermination(1, TimeUnit.SECONDS))
                executorService.shutdown();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        tac = System.currentTimeMillis();
        System.out.println("Number of threads: " + NUMBER_OF_THREADS + "\nStep size (K): " + NUMBER_OF_TASKS + "\nDuration: " + (tac - tic) + "ms.\nResult:");
        printMatrix(AB);
    }

    private static void executeKthElement() {
        ArrayList<Thread> threads = new ArrayList<>();
        for (int i = 0; i < (ROWS_A * COLS_B) / NUMBER_OF_TASKS ; i++) {
            threads.add(new Thread(new KthElement(i)));
        }

        long tic, tac;
        tic = System.currentTimeMillis();

        threads.forEach(Thread::start);

        threads.forEach(t -> {
            try {
                t.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        tac = System.currentTimeMillis();
        System.out.println("Number of threads: " + NUMBER_OF_THREADS + "\nStep size (K): " + NUMBER_OF_TASKS + "\nDuration: " + (tac - tic) + "ms.\nResult:");
        printMatrix(AB);
    }

    private static void executeThreadPoolKthElement() {
        ExecutorService executorService = Executors.newFixedThreadPool(NUMBER_OF_THREADS);

        long tic, tac;
        tic = System.currentTimeMillis();
        for (int i = 0; i < (ROWS_A * COLS_B) / NUMBER_OF_TASKS; ++i) {
            executorService.submit(new KthElement(i));
        }

        try {
            if (!executorService.awaitTermination(1, TimeUnit.SECONDS))
                executorService.shutdown();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        tac = System.currentTimeMillis();
        System.out.println("Number of threads: " + NUMBER_OF_THREADS + "\nStep size (K): " + NUMBER_OF_TASKS + "\nDuration: " + (tac - tic) + "ms.\nResult:");
        printMatrix(AB);
    }

    private static void printMatrix(int[][] matrix) {
        for (int i = 0; i < ROWS_A; ++i) {
            for (int j = 0; j < COLS_B; ++j) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}