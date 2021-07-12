addpath(pwd)

function table = dividedtabledouble (nodes, values, derivative_values)
  
  n = 2 * length(values);
  table = nan(n);
  table(:,1) = repelem(values, 2);
  table(1:2:n-1, 2) = derivative_values;
  table(2:2:n-2, 2) = diff(values) ./ diff(nodes);
  nodes = repelem(nodes, 2);
  for col=3:n
      table(1:end-col+1,col) =(table(2:end-col+2,col-1) - table(1:end-col+1,col-1)) ./ (nodes(col:end) - nodes(1:end-col+1))';
    
  endfor
endfunction

function H = hermite(nodes, values, derivative_values, x)
  table = dividedtabledouble (nodes, values, derivative_values);
  coefs = table(1, :);
  H=zeros(size(x));
  double_nodes = repelem(nodes, 2);
  
  for index=1:length(x)
    product = 1;
    for i=1:length(coefs)
      H(index) = H(index) + coefs(i) * product;
      product = product * (x(index) - double_nodes(i)); 
    endfor
  endfor
endfunction

nodes=[0 3 5 8 13];
values=[0 225 383 623 993];
der_values=[75 77 80 74 72];

dividedtabledouble(nodes,values,der_values)
hermite(nodes, values, der_values, 10)
