function [L] = supCholesky(A)
  % Fonction calculant la matrice triangulaire supérieure
  % On calcule la taille de A
  N = length(A);
  % On initialise la matrice à calculer à une matrice nulle
  L = zeros(N);
  for i=1:N
    % On calcule les termes de la diagonale
    sum = 0;
    for j=1:i-1
      sum = sum + L(j,i)^2;
    end
    L(i,i) = sqrt(A(i,i) - sum);
    % On calcule les autres termes de la ligne
    for j=i+1:N
      sum = 0;
      for k=1:i-1
        sum = sum + L(k,i)*L(k,j);
      end
      L(i,j) = (A(i,j) - sum)/L(i,i);
    end
  end
end