
t = 0:0.1:10*pi

a = 2
b = 3

x = (a+b)*cos(t) - b*cos((a/b + 1)*t)
y = (a+b)*sin(t) - b*sin((a/b + 1)*t)

plot(x,y)
