package lab6.parallel;

import lab6.polynomial.Polynomial;

import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;

import lab6.sequential.*;
import lab6.polynomial.*;

public class ParallelKaratsuba {
    private static final int MAX_DEPTH = 10;

    public static Polynomial multiply(Polynomial a, Polynomial b, int numberOfThreads, int currentDepth) throws ExecutionException, InterruptedException {
        if (currentDepth > MAX_DEPTH) {
            return SequentialKaratsuba.multiply(a, b);
        }

        if (a.getOrder() <= 2 || b.getOrder() <= 2) {
            return SequentialKaratsuba.multiply(a, b);
        }

        int halfArraySize = a.getOrder() / 2;
        Polynomial aLow = new Polynomial(halfArraySize);
        aLow.setCoefficients(a.getCoefficients().subList(0, halfArraySize));

        Polynomial aHigh = new Polynomial(halfArraySize);
        aHigh.setCoefficients(a.getCoefficients().subList(halfArraySize, a.getOrder()));

        Polynomial bLow = new Polynomial(halfArraySize);
        bLow.setCoefficients(b.getCoefficients().subList(0, halfArraySize));

        Polynomial bHigh = new Polynomial(halfArraySize);
        bHigh.setCoefficients(b.getCoefficients().subList(halfArraySize, b.getOrder()));

        Polynomial aLowHigh = PolynomialUtils.add(aLow, aHigh);
        Polynomial bLowHigh = PolynomialUtils.add(bLow, bHigh);

        ExecutorService executor = Executors.newFixedThreadPool(numberOfThreads);
        Callable<Polynomial> task1 = () -> ParallelKaratsuba.multiply(aLow, bLow, currentDepth + 1, numberOfThreads);
        Callable<Polynomial> task2 = () -> ParallelKaratsuba.multiply(aHigh, bHigh, currentDepth + 1, numberOfThreads);
        Callable<Polynomial> task3 = () -> ParallelKaratsuba.multiply(aLowHigh, bLowHigh, currentDepth + 1, numberOfThreads);

        Future<Polynomial> lowFuture = executor.submit(task1);
        Future<Polynomial> highFuture = executor.submit(task2);
        Future<Polynomial> lowHighFuture = executor.submit(task3);

        executor.shutdown();

        Polynomial productLow = lowFuture.get();
        Polynomial productHigh = highFuture.get();
        Polynomial productLowHigh = lowHighFuture.get();

        executor.awaitTermination(60, TimeUnit.SECONDS);

        // compute the final result
        Polynomial r1 = PolynomialUtils.shiftRight(productHigh, 2 * halfArraySize);
        Polynomial r2 = PolynomialUtils.shiftRight(PolynomialUtils.subtract(PolynomialUtils.subtract(productLowHigh, productHigh), productLow), halfArraySize);

        return PolynomialUtils.add(PolynomialUtils.add(r1, r2), productLow);
    }
}