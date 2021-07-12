addpath(pwd)

[x, y] = ginput(5)

i = 0:0.01:1;
hold on

plot(x, y, '*', i, spline(x, y, i));