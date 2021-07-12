package lab6.parallel;

import lab6.polynomial.Polynomial;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class ParallelNaive {

    public static Polynomial multiply(Polynomial a, Polynomial b, int numberOfThreads) {
        ExecutorService executorService = Executors.newFixedThreadPool(numberOfThreads);
        List<Callable<List<Integer>>> callables = new ArrayList<>();
        for (int i = 0; i < a.getOrder(); i++) {
            callables.add(new TrivialThread(a, b, i));
        }
        try {
            List<Future<List<Integer>>> futures = executorService.invokeAll(callables);
            Polynomial result = addPolynomials(futures, a.getOrder(), b.getOrder());
            executorService.shutdown();
            return result;
        } catch (InterruptedException | ExecutionException e) {
            System.err.println("There was a problem while computing");
            return null;
        }
    }

    private static Polynomial addPolynomials(
            List<Future<List<Integer>>> futures, int order1, int order2)
            throws ExecutionException, InterruptedException {
        Polynomial result = new Polynomial(order1 + order2 - 1);
        for (Future<List<Integer>> partialResult : futures) {
            List<Integer> actualPartialResult = partialResult.get();
            for (int i = 0; i < actualPartialResult.size(); i++) {
                result.getCoefficients().set(i, result.getCoefficients().get(i) + actualPartialResult.get(i));
            }
        }
        return result;
    }

    private static class TrivialThread implements Callable<List<Integer>> {
        private final Polynomial a;
        private final Polynomial b;
        private final int indexIna;

        public TrivialThread(Polynomial a, Polynomial b, int indexIna) {
            this.a = a;
            this.b = b;
            this.indexIna = indexIna;
        }

        @Override
        public List<Integer> call() {
            List<Integer> result = new ArrayList<>();
            for (int i = 0; i < a.getOrder() + b.getOrder() - 1; i++) {
                result.add(0);
            }
            for (int j = 0; j < b.getOrder(); j++) {
                result.set(
                        indexIna + j,
                        a.getCoefficients().get(indexIna)
                                * b.getCoefficients().get(j));
            }
            return result;
        }
    }
}