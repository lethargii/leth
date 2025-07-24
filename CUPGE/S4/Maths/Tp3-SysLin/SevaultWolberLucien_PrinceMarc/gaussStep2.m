function [x] = gaussStep2(A, b)
  % Fonction effectuant la deuxième étape du pivot de Gauss
  % On calcule la taille de A
  N = length(A);
  % On initialise le vecteur x au vecteur nul
  x=zeros(N,1);
  % On résous le système linéaire
  for i=N:-1:1
    x(i)=x(i)+b(i);
    if i>1
      for j=i-1:-1:1
        x(j)=x(j)-x(i)*A(j,i);
      end
    end
  end
end