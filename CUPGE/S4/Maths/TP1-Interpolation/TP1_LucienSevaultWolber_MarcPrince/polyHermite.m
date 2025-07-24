function [pn] = polyHermite(x, y, z)
  n = length(x);
  pn = 0;
  for i=1:n
    % Calcul de Li
    Li = [1];
    for j=1:n
      if j~=i
        Li = conv(Li, [1 -x(j)])/(x(i)-x(j));
      end
    end
    % Calcul de Li'
    dLi = polyder(Li);
    % Ajout de Hi et Ki
    Li2 = conv(Li, Li)
    Hi = [0 1] -2*polyval(dLi, x(i))*[1 -x(i)];
    Hi = conv(Hi, Li2)
    Ki = conv([1 -x(i)],Li2)
    pn = pn + y(i)*Hi + z(i)*Ki
  end