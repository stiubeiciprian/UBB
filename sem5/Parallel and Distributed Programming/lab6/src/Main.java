import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

public class Main {

    private static int[][] generateMatrix(int n) {
        Random random = new Random();
        int[][] matrix = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    matrix[i][j] = 0;
                } else {
                    matrix[i][j] = random.nextInt(2);
                }
            }
        }
        return matrix;
    }

    public static void main(String[] args) {
        int[][] m = {
          {0, 1, 0, 0, 0},
          {0, 0, 1, 0, 0},
          {0, 0, 0, 1, 0},
          {0, 0, 0, 0, 1},
          {1, 0, 0, 0, 0},
        };

//        int[][] m = generateMatrix(100);
        Graph graph = new Graph(m);
        System.out.println(graph);

        ExecutorService executorService = Executors.newFixedThreadPool(graph.size);

        List<HamiltonianThread> threads = new ArrayList<>();
        for (int i = 0; i < graph.size; i++) {
            threads.add(new HamiltonianThread(graph, i));
            executorService.submit(threads.get(i));
        }

        long tic = System.currentTimeMillis();

        try {
            if (!executorService.awaitTermination(1, TimeUnit.SECONDS)) {
                executorService.shutdownNow();
            }
            long tac = System.currentTimeMillis();

            if (threads.stream().anyMatch(thread -> thread.finished)) {
                threads = threads.stream().filter(thread -> thread.finished).collect(Collectors.toList());
                System.out.println("The cycle is:");
                threads.get(0).cycle.forEach(v -> System.out.print(v + " "));
                System.out.println("\nExecuted in " + (tac - tic) + "ms.");

            } else {
                System.out.println("No hamiltonian cycle found.\nExecuted in " + (tac - tic) + "ms.");
            }
        } catch (InterruptedException ex) {
            executorService.shutdownNow();
            Thread.currentThread().interrupt();
        }
    }

}
