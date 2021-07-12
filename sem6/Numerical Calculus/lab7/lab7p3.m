addpath(pwd)


axis([0 3 0 5]);
[x y] = ginput(10);


printf("%d",y(5));
xx = x(1):(x(10)-x(1))/100:x(10);

p = polyfit(x, y, 2);
plot(x, y, '*');
clf;
hold on;

k = x(1):(x(10)-x(1))/100:x(10);
plot(x, y, 'x', k, polyval(p, k));