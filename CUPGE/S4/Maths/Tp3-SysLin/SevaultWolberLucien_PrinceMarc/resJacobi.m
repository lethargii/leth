function [xk1] = resJacobi(A, b, tol, itermax)
  % Fonction résolvant le système linéaire grâce à la méthode de Jacobi
  % On calcule la taille de A
  N = length(A);
  % On calcule les matrices L, D et U
  [L, D, U] = decompJacobi(A);
  % On initialise l'inverse de D à une matrice nulle
  invD = zeros(N);
  for i=1:N
    % L'inverse d'une matrice diagonale est composée de l'inverse des éléments de la matrice
    invD(i,i) = 1/D(i,i);
  end
  % On initalise le vecteur x au vecteur nul
  xk1 = zeros(length(b),1);
  % On initialise le nombre d'itération et la norme de l'erreur
  iter = 1;
  norminf = tol;
  % On continue d'itérer tant que le nombre d'itérations
  while iter <= itermax && norminf >= tol
    % On recalcule x
    xk = xk1;
    xk1 = invD*(-(L+U)*xk+b);
    % On calcule l'erreur
    norminf = max(abs(xk1-xk));
    % On augmente le nombre d'itération
    iter = iter + 1;
  end
end