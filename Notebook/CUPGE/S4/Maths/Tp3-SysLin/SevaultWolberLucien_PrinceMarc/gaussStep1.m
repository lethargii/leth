function [A, b] = gaussStep1(A, b)
  % Fonction effectuant la première étape du pivot de Gauss
  % On calcule la taille de A
  N = length(A);
  % On constitue la matrice augmentée
  B = [A,b];
  for i=1:N
    % On normalise la ligne de la matrice augmentée par rapport à l'élément de la diagonale
    B(i,:) = B(i,:)/B(i,i);
    for j=i+1:N
      % On soustrait les lignes pour annuler les termes en dessous de la diagonale
      B(j,:) = B(j,:)-B(i,:)*B(j,i);
    end
  end
  % On renvoie les A et b modifiés
  A = B(:,1:N);
  b = B(:,end);
end