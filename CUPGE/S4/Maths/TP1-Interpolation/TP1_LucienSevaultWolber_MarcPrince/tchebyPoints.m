function [x] = tchebyPoints(a,b,n)
%   Fonction retournant les n+1 points de tchebyChev entre a et b
%
%   * Entree :
%       --> a - float - borne inférieure de l'intervalle d'interpolation
%       --> b - float - borne supérieure de l'intervalle d'interpolation
%       --> n - int - nombre de points de tchebyChev
%   * Sortie :
%       --> x - ligne Float - points de tchebyChev
  % Il y a n+1 à calculer
  x = zeros(1, n+1);
  % On calcule chaque point de tchebyChev
  for i=1:n+1
    % On calcule le point de tchebychev
    x(i) = cos((2*i-1)*pi/(2*(n+1)));
    % On ramène les points dans l'intervalle [a,b]
    x(i) = ((a+b)+(b-a)*x(i))/2;
  end
