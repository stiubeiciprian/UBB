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

nodes=[1 2];
values=[0 0.6931];
der_values=[1 0.5];

dividedtabledouble(nodes,values,der_values)

x = 1.5;

result = hermite(nodes, values, der_values, x)
absolute_error = abs(log(x) - result)

printf("Abs error = %f\n", absolute_error);