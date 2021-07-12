import java.util.ArrayList;
import java.util.List;

public class HamiltonianThread extends Thread {
    private final Graph graph;
    public final int startingVertex;
    public List<Integer> cycle;
    public boolean finished;

    public HamiltonianThread(Graph graph, int startingVertex) {
        this.graph = graph;
        this.startingVertex = startingVertex;
    }

    @Override
    public void run() {
        List<Integer> path = new ArrayList<>();

        for (int i = 0; i < graph.size; i++) {
            path.add(i, -1);
        }

        path.set(0, startingVertex);
        if (!hamiltonianCycleRecursive(graph, path, 1, startingVertex)) {
            finished = false;
            cycle = path;
            return;
        }
        path.add(startingVertex);
        finished = true;
        cycle = path;
    }

    private boolean hamiltonianCycleRecursive(Graph graph, List<Integer> currentPath, int currentPosition, int startingVertex) {
        if (currentPosition == graph.size) {
            // edge from the last included vertex to the first vertex
            return graph.graph[currentPath.get(currentPosition - 1)][currentPath.get(0)] == 1;
        }

        for (int vertex = 0; vertex < graph.size; vertex++) {
            if (vertex != startingVertex && canProceed(vertex, graph, currentPath, currentPosition)) {
                currentPath.set(currentPosition, vertex);
                if (hamiltonianCycleRecursive(graph, currentPath, currentPosition + 1, startingVertex)) {
                    return true;
                }
                // if not leading to solution
                currentPath.set(currentPosition, -1);
            }
        }

        return false;
    }

    private boolean canProceed(int newVertex, Graph graph, List<Integer> currentPath, int currentPosition) {
        // check if edge exists
        if (graph.graph[currentPath.get(currentPosition - 1)][newVertex] == 0) {
            return false;
        }
        // check if already added
        return currentPath.stream().filter(current -> current == newVertex).count() <= 0;
    }
}