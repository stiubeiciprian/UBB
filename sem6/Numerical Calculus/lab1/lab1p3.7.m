x = -2:0.1:2
y = -4:0.1:4
[X,Y] = meshgrid(x,y);

g = exp(-((X-1/2).^2 + (Y-1.2).^2));

mesh(X,Y,g)