package lab6.sequential;

import lab6.polynomial.Polynomial;
import lab6.polynomial.PolynomialUtils;

public class SequentialKaratsuba {

    // this only works on polynomials of same length
    public static Polynomial multiply(Polynomial a, Polynomial b) {

        // Handle the base case where the polynomial has only one coefficient
        if (a.getOrder() == 1) {
            Polynomial result = new Polynomial(1);
            result.getCoefficients().set(0, a.getCoefficients().get(0) * b.getCoefficients().get(0));
            return result;
        }

        int halfArraySize = a.getOrder() / 2;

        // Declare arrays to hold halved factors
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

        // Recursively call method on smaller arrays and construct the low and high parts of the product
        Polynomial productLow = multiply(aLow, bLow);
        Polynomial productHigh = multiply(aHigh, bHigh);
        Polynomial productLowHigh = multiply(aLowHigh, bLowHigh);

        Polynomial r1 = PolynomialUtils.shiftRight(productHigh, 2 * halfArraySize);
        Polynomial r2 = PolynomialUtils.shiftRight(PolynomialUtils.subtract(PolynomialUtils.subtract(productLowHigh, productHigh), productLow), halfArraySize);

        return PolynomialUtils.add(PolynomialUtils.add(r1, r2), productLow);
    }

    private static void print(Polynomial aLow, Polynomial aHigh, Polynomial bLow, Polynomial bHigh, Polynomial aLowHigh, Polynomial bLowHigh) {
        System.out.println("Poly1 low");
        aLow.getCoefficients().forEach(x -> System.out.print(x + " "));
        System.out.println();
        System.out.println("Poly1 high");
        aHigh.getCoefficients().forEach(x -> System.out.print(x + " "));
        System.out.println();
        System.out.println("Poly1 lowhigh");
        aLowHigh.getCoefficients().forEach(x -> System.out.print(x + " "));
        System.out.println();
        System.out.println("Poly2 low");
        bLow.getCoefficients().forEach(x -> System.out.print(x + " "));
        System.out.println();
        System.out.println("Poly1 high");
        bHigh.getCoefficients().forEach(x -> System.out.print(x + " "));
        System.out.println();
        System.out.println("Poly2 lowhigh");
        bLowHigh.getCoefficients().forEach(x -> System.out.print(x + " "));
        System.out.println();
    }
}