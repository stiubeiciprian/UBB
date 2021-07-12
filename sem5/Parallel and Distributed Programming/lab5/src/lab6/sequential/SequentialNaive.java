package lab6.sequential;

import lab6.polynomial.Polynomial;

public class SequentialNaive {

    public static Polynomial multiply(Polynomial a, Polynomial b) {
        Polynomial result = new Polynomial(a.getOrder() + b.getOrder() - 1);
        for (int i = 0; i < a.getOrder(); i++) {
            for (int j = 0; j < b.getOrder(); j++) {
                int newValue = result.getCoefficients().get(i + j) + a.getCoefficients().get(i) * b.getCoefficients().get(j);
                result.getCoefficients().set(i + j, newValue);
            }
        }
        return result;
    }
}