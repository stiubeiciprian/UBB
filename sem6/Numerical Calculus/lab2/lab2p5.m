
function table = finitetable (values)
  table = nan(size(values)(2)); # or length  or zeros(length)
  table(:,1) = values;
  for col=2:length(values)
    table(1:end-col+1,col) = ...
    table(2:end-col+2,col-1)- ... 
    table(1:end-col+1,col-1);
  endfor
  