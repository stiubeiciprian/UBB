addpath(pwd)

nodes = [0 pi/2 pi 3*pi/2 2*pi];
values = sin(nodes);
x = 0:0.1:2*pi;

printf("sin(pi/4) = %f\n", sin(pi/4));
printf("cubic natural spline = %f\n", spline(nodes, values, pi/4));
printf("cubic clamped spline = %f\n", spline(nodes, [1 values 1], pi/4));

plot(x, sin(x), 'm')
hold on
plot(x, spline(nodes, values, x), 'b')
plot(x, spline(nodes, [1 values 1], x), 'g')

legend("sin", "natural", "clamped")
