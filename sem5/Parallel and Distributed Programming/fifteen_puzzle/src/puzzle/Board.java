package puzzle;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.Random;


public class Board implements Serializable {
    private final int[][] board;
    private final int size;
    private int heuristics;
    private int emptyRow, emptyCol;
    private Board parent;
    public enum Shift {UP, DOWN, LEFT, RIGHT}

    public Board() {
        this.size = 1;
        this.board = new int[][] {{0}};
    }

    public Board(int[][] board) {
        this.size = board.length;
        this.board = new int[size][size];
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                this.board[i][j] = board[i][j];
                if(board[i][j] == 0) {
                    emptyRow = i;
                    emptyCol = j;
                }
            }
        }

        this.heuristics = manhattanDistance();
    }

    public Board(Board other) {
        this.size = other.size;
        this.emptyRow = other.emptyRow;
        this.emptyCol = other.emptyCol;
        this.heuristics = other.heuristics;
        this.board = new int[size][size];

        for (int i = 0; i < size; i += 1) {
            for (int j = 0; j < size; j += 1) {
                board[i][j] = other.board[i][j];
            }
        }
    }

    public Board generateSolutionForBoard() {
        int[][] solutionBoard = new int[size][size];
        int counter = 1;
        for (int i = 0; i < size; i += 1) {
            for (int j = 0; j < size; j += 1) {
                solutionBoard[i][j] = counter;
                counter += 1;
            }
        }
        solutionBoard[size-1][size-1] = 0;

        return new Board(solutionBoard);
    }


    private void swap(int row, int col, int newI, int newJ) throws FifteenPuzzleException {
        if (row >= size || col >= size || newI >= size || newJ >= size || row < 0 || col < 0 || newI < 0 || newJ < 0) {
            throw new FifteenPuzzleException(String.format("Can't swap (%d, %d) with (%d, %d)", row, col, newI, newJ));
        }

        int aux = board[row][col];
        board[row][col] = board[newI][newJ];
        board[newI][newJ] = aux;

        if (board[row][col] == 0) {
            emptyRow = row;
            emptyCol = col;
        }
        if (board[newI][newJ] == 0) {
            emptyRow = newI;
            emptyCol = newJ;
        }

        this.heuristics = this.manhattanDistance();
    }

    /**
     * Shift this board
     * @param direction direction to shift in
     * @throws FifteenPuzzleException if at the edge and can't shift
     */
    public void shift(Board.Shift direction) throws FifteenPuzzleException {
        switch (direction) {
            case UP : { swap(emptyRow, emptyCol, emptyRow - 1, emptyCol); break; }
            case DOWN : { swap(emptyRow, emptyCol, emptyRow + 1, emptyCol); break; }
            case LEFT : { swap(emptyRow, emptyCol, emptyRow, emptyCol - 1); break; }
            case RIGHT : { swap(emptyRow, emptyCol, emptyRow, emptyCol + 1); break; }
        }
    }

    /**
     * Get a shifted Board
     * @param direction direction to shift in
     * @return shifted copy of this board
     * @throws FifteenPuzzleException if at the edge and can't shift
     */
    public Board shifted(Board.Shift direction) throws FifteenPuzzleException {
        Board puzzle = new Board(this);
        puzzle.shift(direction);
        return puzzle;
    }

    /**
     * Returns a list of all possible moves.
     * @return list of all possilbe moves
     */
    public List<Board> possibleMoves() {
        List<Board> successorsList = new ArrayList<>();
        for (Shift direction : Shift.values()) {
            try { successorsList.add(shifted(direction));
            } catch (FifteenPuzzleException e) { }
        }
        return successorsList;
    }

    /**
     * Compute the manhattan distance of the current board state.
     * @return manhattan distance of current board state
     */
    public int manhattanDistance() {
        int distance = 0;
        for (int row = 0; row < size; row++) {
            for (int col = 0; col < size; col++) {
                if (board[row][col] == 0) {
                    continue;
                }

                int expectedRow = (board[row][col] - 1) / size;
                int expectedCol = (board[row][col] - 1) % size;
                distance += Math.abs(row - expectedRow) + Math.abs(col - expectedCol);
            }
        }
        return distance;
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < size; i += 1) {
            for (int j = 0; j < size; j += 1) {
                builder.append(board[i][j]).append("\t");
            }
            builder.append("\n");
        }
        return builder.toString();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Board puzzle = (Board) o;
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (board[i][j] != puzzle.board[i][j]) return false;
            }
        }
        return true;
    }

    public Board getParent() {
        return parent;
    }

    public void setParent(Board parent) {
        this.parent = parent;
    }

    public int getHeuristics() {
        return heuristics;
    }

    public boolean isSolution() {
        return this.heuristics == 0;
    }

    @Override
    public int hashCode() {
        int result = Objects.hash(size, heuristics, emptyRow, emptyCol);
        result = 31 * result + Arrays.hashCode(board);
        return result;
    }
}
