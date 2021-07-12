addpath(pwd)

function table = dividedtable (nodes, values)
  table = nan(size(values)(2));
  table(:,1) = values;
  for col=2:length(values)
    table(1:end-col+1,col) = (table(2:end-col+2,col-1) - table(1:end-col+1,col-1)) ./ (nodes(col:end) - nodes(1:end-col+1))';
  endfor
endfunction


function N = newton(nodes, values, x)
  table = dividedtable(nodes, values);
  
  lx = length(x);
  p = ones(1,lx);
  s = table(1,1) * ones(1,lx);
  
  for j=1:lx
    for i=1:length(nodes) - 1
      
      p(j) = p(j) * (x(j) - nodes(i));
      s(j) = s(j) + p(j) * table(1, i+1);
    endfor
  endfor
  
  N=s;
  
endfunction

nodes = [1 1.5 2 3 4];
values = [0 0.17609 0.30103 0.47712 0.60206];

printf("lg 2.5 = %d\n", newton(nodes, values, 2.5))
printf("lg 3.25 = %d\n", newton(nodes, values, 3.25))

i = 10:1:35;
yi = i/10;

printf("Error: %f\n", max(abs(log10(yi) - newton(nodes, values, yi))));
