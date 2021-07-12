package puzzle;

import puzzle.Board;
import puzzle.FifteenPuzzleException;
import puzzle.MPISolver;

import java.util.Scanner;
import java.util.Stack;
import java.util.concurrent.ExecutionException;

import mpi.*;


public class Main {
    public static void main(String[] args) {
        
        solveUsingThreads();
//        solveUsingMpi(args);
    }

    private static void solveUsingThreads() {
        int[][] board = new int[][] {
                {1, 2,	3, 4},
                {10, 0,	6, 7},
                {5,	9, 11, 8},
                {13, 14, 15, 12},
        };

        Board puzzle = new Board(board);
        Solver solver = new Solver(4);

        try {
            Stack<Board> solution = solver.findSolution(puzzle);

            for (Board boardIteration : solution) {
                System.out.println("Manhatan distance: " + boardIteration.getHeuristics());
                System.out.println(boardIteration.toString());
            }

        } catch (ExecutionException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    private static void solveUsingMpi(String[] args) {
        MPI.Init(args);
        new MPISolver().start();
    }

}