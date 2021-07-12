addpath(pwd)

nodes = [0 10 20 30 40 60 80 100];
values = [0.0061 0.0123 0.0234 0.0424 0.0738 0.1992 0.4736 1.0133];

p1 = polyfit(nodes, values, 2);
p2 = polyfit(nodes, values, 4);

approx1 = polyval(p1, 45)
error1 = abs(0.095848 - approx1)

approx2 = polyval(p2, 45)
error2 = abs(0.095848 - approx2)


plot(nodes, values, '*');
clf;
hold on;  

k = 1:0.1:100;
plot(k, polyval(p1, k), 'r');
plot(k, polyval(p2, k), 'g'); 
plot(nodes, polyval(p1, nodes), 'x');
plot(nodes, polyval(p2, nodes), 'o');
