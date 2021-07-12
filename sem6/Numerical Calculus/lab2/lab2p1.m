l1 = [1 0];
l2 = [3/2 0 -1/2];
l3 = [5/2 0 3/2 0];
l4 = [35/8 0 -15/4 0 3/8];
x = 0:0.01:1;

subplot(2, 2, 1);
plot(x, polyval(l1,x));
title('l1')

subplot(2, 2, 2);
plot(x, polyval(l2,x));
title('l2')

subplot(2, 2, 3);
plot(x, polyval(l3,x));
title('l3')

subplot(2, 2, 4);
plot(x, polyval(l4,x));
title('l4')