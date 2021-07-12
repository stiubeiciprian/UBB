package lab6;

import lab6.polynomial.Polynomial;
import lab6.parallel.*;
import lab6.sequential.*;

import java.util.Arrays;
import java.util.concurrent.ExecutionException;

public class Main {
    private static final int NUMBER_OF_THREADS = 4;

    public static void main(String[] args) throws ExecutionException, InterruptedException {
        Polynomial a = new Polynomial(10);
//        a.fillWithRandomNumbers();
        a.setCoefficients(Arrays.asList(1, 1));
        System.out.println(a.toString());

        Polynomial b = new Polynomial(10);
//        b.fillWithRandomNumbers();
        b.setCoefficients(Arrays.asList(1, 1));
        System.out.println(b.toString());

        long tic = System.currentTimeMillis();
        run(a, b);
        long tac = System.currentTimeMillis();
        System.out.println("\nExecuted in " + (tac - tic) + "ms.");
    }

    private static void run(Polynomial a, Polynomial b) throws ExecutionException, InterruptedException {
        Polynomial result;
        result = SequentialNaive.multiply(a, b);
        System.out.println(result.toString());
        result = SequentialKaratsuba.multiply(a, b);
        System.out.println(result.toString());
        result = ParallelNaive.multiply(a, b, NUMBER_OF_THREADS);
        System.out.println(result.toString());
        result = ParallelKaratsuba.multiply(a, b, NUMBER_OF_THREADS, 4);
        System.out.println(result.toString());
    }
}