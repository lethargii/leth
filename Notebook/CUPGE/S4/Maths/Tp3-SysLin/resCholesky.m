function [x] = resCholesky(A, b)
  % Fonction résolvant le système linéaire avec la méthode de Cholesky
  % On calcule la taille de b
  N = length(b);
  % On calcule la matrice L
  L = supCholesky(A);
  % On résous Ly = b
  y = zeros(N, 1);
  for i=1:N
    for j=1:i-1
      b(i) = b(i) - y(j)*L(j,i);
    end
    y(i) = b(i)/L(i,i);
  end
  % On résous LTx = y
  x = zeros(N, 1);
  for i=N:-1:1
    for j=N:-1:i
      y(i) = y(i) - x(j)*L(i,j);
    end
    x(i) = y(i)/L(i,i);
  end
end