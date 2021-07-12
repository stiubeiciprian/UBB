addpath(pwd)

nodes = [1 2 3 4 5 6 7];
values = [13 15 20 14 15 13 10];

m = length(nodes);
a = (m * sum(nodes.*values) - sum(values) * sum(nodes)) / (m * sum(nodes.^2) - sum(nodes)^2)
b = (sum(nodes.^2) * sum(values) - sum(nodes.*values) * sum(nodes)) / (sum(nodes.^2)*m-sum(nodes)^2)

clf; 
hold on;
title("Problem 1")
xlabel ("time");
ylabel ("temperature");

plot(nodes,values,'x');
phi = @(y)(a*y+b);
fplot(phi,[0,8])
E = norm(values - phi(nodes))^2 


printf("phi(8)= %f\n", phi(8));