package lab6.polynomial;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class PolynomialUtils {
    public static Polynomial shiftRight(Polynomial p, int offset) {
        Polynomial result = new Polynomial(p.getOrder() + offset);
        List<Integer> coefficients = IntStream.range(0, offset).mapToObj(i -> 0).collect(Collectors.toList());

        coefficients.addAll(p.getCoefficients());
        result.setCoefficients(coefficients);

        return result;
    }

    public static Polynomial add(Polynomial a, Polynomial b) {

        int minDegree = Math.min(a.getOrder(), b.getOrder());
        int maxDegree = Math.max(a.getOrder(), b.getOrder());

        Polynomial result = new Polynomial(maxDegree);

        for (int i = 0; i < minDegree; i++) {
            result.getCoefficients().set(i, a.getCoefficients().get(i) + b.getCoefficients().get(i));
        }

        Polynomial longest = a.getOrder() > b.getOrder() ? a : b;

        for (int i = minDegree; i < maxDegree; i++) {
            result.getCoefficients().set(i, longest.getCoefficients().get(i));
        }
        return result;
    }

    public static Polynomial subtract(Polynomial a, Polynomial b) {
        int minDegree = Math.min(a.getOrder(), b.getOrder());
        int maxDegree = Math.max(a.getOrder(), b.getOrder());

        Polynomial result = new Polynomial(maxDegree);

        for (int i = 0; i < minDegree; i++) {
            result.getCoefficients().set(i, a.getCoefficients().get(i) - b.getCoefficients().get(i));
        }

        Polynomial longest =
                a.getOrder() > b.getOrder() ? a : b;

        for (int i = minDegree; i < maxDegree; i++) {
            result.getCoefficients().set(i, longest.getCoefficients().get(i));
        }

        int i = result.getCoefficients().size() - 1;

        while (result.getCoefficients().get(i) == 0 && i > 0) {
            result.getCoefficients().remove(i);
            i--;
        }

        return result;
    }
}