package puzzle;

import puzzle.Board;

import java.util.AbstractMap;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;



public class Solver {
    private final int SOLUTION_FOUND = -1;
    private final ExecutorService executorService;
    private final int INF = Integer.MAX_VALUE;
    private final Stack<Board> solutionStack;
    private final int NUMBER_OF_THREADS;

    public Solver(int numberOfThreads) {
        this.NUMBER_OF_THREADS = numberOfThreads;
        this.executorService = Executors.newFixedThreadPool(numberOfThreads);
        solutionStack = new Stack<>();
    }

    public Stack<Board> findSolution(Board initialBoard) throws ExecutionException, InterruptedException {
        int initialBoardHeuristics = initialBoard.getHeuristics();
        solutionStack.add(initialBoard);
        
        AbstractMap.SimpleEntry<Integer, Stack<Board>> result = null;
        while (true) {
            result = searchParallel(solutionStack, 0, initialBoardHeuristics, NUMBER_OF_THREADS);

            if (result.getKey() == SOLUTION_FOUND) {
                executorService.shutdown();
                return result.getValue();
            }
            initialBoardHeuristics = result.getKey();
        }
    }

    public AbstractMap.SimpleEntry<Integer, Stack<Board>> searchParallel(Stack<Board> stack, int numberOfSteps, int bound, int numberOfThreads) throws ExecutionException, InterruptedException {
        if (numberOfThreads <= 1) {
            return search(stack, numberOfSteps, bound);
        }
        Board currentBoard = stack.peek();
        int score = numberOfSteps + currentBoard.getHeuristics();

        if (score > bound || score > 80) {
            return new AbstractMap.SimpleEntry<>(score, stack);
        }
        if (currentBoard.getHeuristics() == 0) {
            return new AbstractMap.SimpleEntry<>(SOLUTION_FOUND, stack);
        }

        int min = INF;
        List<Board> moves = currentBoard.possibleMoves();
        List<Future<AbstractMap.SimpleEntry<Integer, Stack<Board>>>> futures = new ArrayList<>();


        for (Board next : moves) {
            Stack<Board> copy = (Stack<Board>) stack.clone();
            copy.push(next);
            Future<AbstractMap.SimpleEntry<Integer, Stack<Board>>> f =
                    executorService.submit(() ->
                            searchParallel(copy, numberOfSteps + 1, bound, numberOfThreads / moves.size())
                    );
            futures.add(f);
        }


        for (Future<AbstractMap.SimpleEntry<Integer, Stack<Board>>> f : futures) {
            AbstractMap.SimpleEntry<Integer, Stack<Board>> result = f.get();
            int t = result.getKey();
            if (t == -1) {
                return new AbstractMap.SimpleEntry<>(SOLUTION_FOUND, result.getValue());
            }
            if (t < min) {
                min = t;
            }
        }
        return new AbstractMap.SimpleEntry<>(min, stack);
    }

    public AbstractMap.SimpleEntry<Integer, Stack<Board>> search(Stack<Board> stack, int numberOfSteps, int bound) {
        Board current = stack.peek();

        int score = numberOfSteps + current.getHeuristics();

        if (score > bound || score > 80) {
            return new AbstractMap.SimpleEntry<>(score, stack);
        }
        if (current.getHeuristics() == 0) {
            return new AbstractMap.SimpleEntry<>(SOLUTION_FOUND, stack);
        }
        int min = INF;
        for (Board next : current.possibleMoves()) {
            if (!solutionStack.contains(next)) {
                stack.push(next);
                AbstractMap.SimpleEntry<Integer, Stack<Board>> result = search(stack, numberOfSteps + 1, bound);
                int t = result.getKey();
                if (t == SOLUTION_FOUND) {
                    return new AbstractMap.SimpleEntry<>(SOLUTION_FOUND, stack);
                }
                if (t < min) {
                    min = t;
                }
                stack.pop();
            }
        }
        return new AbstractMap.SimpleEntry<>(min, stack);
    }
}