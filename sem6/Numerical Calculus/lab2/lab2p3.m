f=exp(0);

function p = taylor(x, n)
  p=0;
  for k=0:n 
      p = p + (x-0)^k/factorial(k); 
  end
end


hold on
for n=1:6
    for x=-1:0.01:3
        plot(x, taylor(x,n))
    end
end
