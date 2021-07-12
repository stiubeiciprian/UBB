x = 0:0.1:2*pi

f1 = cos(x)
f2 = sin(x)
f3 = cos(2*x)

plot(x,f1)
hold on
plot(x,f2)
plot(x,f3)

legend('cos x','sin x','cos 2x')