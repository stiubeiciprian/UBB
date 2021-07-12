t = -1:0.01:1;

t1 = cos(acos(t));
t2 = cos(2*acos(t));
t3 = cos(3*acos(t));

figure(1)
plot(t,t1)
hold on
plot(t,t2)
plot(t,t3)

legend('t1','t2','t3')