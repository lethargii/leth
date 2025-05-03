function [L, D, U] = decompJacobi(A)
  % Fonction renvoyant les matrices D, U et L
  % On calcule la taille de A
  N = length(A);
  % On initialise les 3 matrices à une matrice nulle
  D = zeros(N);
  U = zeros(N);
  L = zeros(N);
  for i=1:N
    for j=1:N
      if i==j
        % D est composée des éléments de la diagonale de A
        D(i,j)=A(i,j);
      end
      if i<j
        % U est composée des éléments au dessus de la diagonale de A
        U(i,j)=A(i,j);
      end
      if i>j
        % L est composée des éléments en dessous de la diagonale de A
        L(i,j)=A(i,j);
      end
    end
  end
end