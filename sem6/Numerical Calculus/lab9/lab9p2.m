addpath(pwd)

a = 0;
b = 1;

f = @(x) 2./(1+x.^2);
epsilon = 0.0001;
real_value = pi/2;

function y = romberg(a, b, f, k)
  h = b-a;
  if  k == 0
    y = h/2 * (f(a) + f(b));
  else
    q_last = romberg(a, b, f, k-1);
    j = [1:2^(k-1)];
    rng = (2*j - 1) ./ 2^k;
    s = sum(f(a + rng .* h));
    y = 1/2 * q_last + h/2^k *s;
  end
end

k=0;
approx = romberg(a,b,f,k);

while abs(approx - real_value) >= epsilon
  approx = romberg(a,b,f,k);
  k = k+1;
end

printf("k = %d, approx = %f\n", k, approx); 
