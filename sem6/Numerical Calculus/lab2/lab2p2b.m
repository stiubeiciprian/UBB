figure(1)
hold on
x = -1:0.01:1;

t0 = 1;
t1 = x;
tn = 2.*x.*t1 - t0

function p = T(n)
    x = -1:0.01:1;
    if n==0
        p = 1;
    elseif n==1
        p = x;
    else 
        p = 2.*x.*T(n-1) - T(n-2);
    end
end


for n=1:5
    plot(x,T(n))
end

