package puzzle;

import puzzle.Board;
import mpi.*;

import java.io.Serializable;
import java.util.*;


public class MPISolver {
    private final static int MAIN = 0;
    private final static int FOUND = -1;

    private final int rank;
    private final int np;

    public MPISolver() {
        rank = MPI.COMM_WORLD.Rank();
        np = MPI.COMM_WORLD.Size();
    }

    public void start() {
        try {
            if (rank == MAIN) {
                this.main();
            } else {
                this.worker();
            }
        } catch (Exception exception) {
            System.out.printf("Error in %d\n", rank);
            exception.printStackTrace();
        }
    }

    private static void Send(int destination, Object[] object) {
        MPI.COMM_WORLD.Send(object, 0, 1, MPI.OBJECT, destination, 0);
    }

    private static Object Recv(int source) {
        Object[] result = new Object[1];
        MPI.COMM_WORLD.Recv(result, 0, 1, MPI.OBJECT, source, 0);
        return result[0];
    }

    private static class ObjectToSend implements Serializable {
        public int numberOfSteps;
        public int bound;
        public Board board;

        public ObjectToSend(int numberOfSteps, int bound, Board board) {
            this.numberOfSteps = numberOfSteps;
            this.bound = bound;
            this.board = board;
        }
    }

    /**
     * getChildren
     *   if the parent is a solution print and exit
     *   if the parent is out of bounds try again with larger bounds
     *   if there is only one child child becomes parent
     * nextIteration
     *   if there are multiple children worker finds the best child
     */
    private void main() {
        int[][] board = new int[][] {
                {1, 2,	3, 4},
                {10, 0,	6, 7},
                {5,	9, 11, 8},
                {13, 14, 15, 12},
        };

        Board initialBoard = new Board(board);
        initialBoard.setParent(null);
        int minBound = initialBoard.getHeuristics();

        List<List<ObjectToSend>> queue = new ArrayList<>();
        queue.add(listOf(new ObjectToSend(0, minBound, initialBoard)));

        while (queue.size() > 0) {
            List<ObjectToSend> currentList = queue.remove(0);
            if (currentList.size() == 1) {
                ObjectToSend current = currentList.get(0);

                // If found, print solution and kill workers
                // else add next moves to the queue
                if (current.bound == FOUND) {
                    printSolution(current.board);
                    killAll();
                    return;
                } else {
                    queue.add(getChildren(current));
                }
            } else {
                List<List<ObjectToSend>> nextInQueue = nextIteration(currentList, currentList.get(0).board.getParent());
                queue.addAll(nextInQueue);
            }
        }
    }

    /**
     * Sends children to worker processes and returns result.
     * @param children - children to distribute to workers.
     * @param parent - parent of the children list
     * @return - resulting board states
     */
    private List<List<ObjectToSend>> nextIteration(List<ObjectToSend> children, Board parent) {
        for (int i = 0; i < children.size(); i += 1) {
            Send(i+1, new Object[] {children.get(i)});
        }

        List<List<ObjectToSend>> nextInQueue = new ArrayList<>();
        for (int i = 0; i < children.size(); i += 1){
            List<ObjectToSend> result = (List<ObjectToSend>) Recv(i+1);
            nextInQueue.add(result);
        }
        return nextInQueue;
    }

    private void printSolution(Board board) {
        if (board.getParent() != null) {
            printSolution(board.getParent());
        }
        System.out.println("---");
        System.out.println(board);
        System.out.println("Manhatan distance: " + board.getHeuristics());

    }

    /**
     * Kills all worker processes.
     */
    private void killAll() {
        for (int i = 1; i < np; i += 1) {
            Send(i, new Object[]{ new ObjectToSend(-1, 0, new Board())});
        }
    }

    private void worker() {
        while (true) {
            ObjectToSend parent = (ObjectToSend) Recv(MAIN);
            if (parent.numberOfSteps == -1) return;
            Send(MAIN, new Object[]{ getChildren(parent) });
        }
    }

    private List<ObjectToSend> getChildren(ObjectToSend current) {
        // Check if solution was found
        if(current.board.isSolution()) {
            return listOf(new ObjectToSend(0, FOUND, current.board));
        }

        // Check if out of bounds
        int score = current.numberOfSteps + current.board.getHeuristics();
        if (score > current.bound || score > 80) {
            return listOf(new ObjectToSend(0, score, current.board));
        }

        List<Board> moves = current.board.possibleMoves();
        List<ObjectToSend> nextInQueue = new ArrayList<>();
        for (Board child : moves) {
            if (hasParent(current.board, child)) continue;
            child.setParent(current.board);
            nextInQueue.add(new ObjectToSend(current.numberOfSteps + 1, current.bound, child));
        }
        return nextInQueue;
    }

    /**
     * Return true if the board already has child as a parent
     * @param board
     * @param child
     * @return
     */
    private boolean hasParent(Board board, Board child) {
        if (board == child) return true;
        if (board.getParent() != null) {
            return hasParent(board.getParent(), child);
        } else return false;
    }

    private static <T> List<T> listOf(T element) {
        List<T> list = new ArrayList<>();
        list.add(element);
        return list;
    }
}
