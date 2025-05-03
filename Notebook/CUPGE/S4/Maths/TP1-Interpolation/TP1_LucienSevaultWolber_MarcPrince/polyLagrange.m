function [polFin] = polyLagrange(x,y)
%   Fonction retournant le polynome de Lagrange
%
%   * Entree :
%       --> x - ligne Float - point d'interpolation
%       --> y - ligne Float - image du point d'interpolation
%   * Sortie :
%       --> polFin - ligne Float - Polynome de Lagrange
len = length(x);
% Le polynome renvoyée a pour degré le nombre de points
polFin=zeros(1,len);
% On calcule chaque Li
for i=1:len
    convolution = [1];
    for j=1:len
        % On ne divise pas par x(i) - x(i)
        if j~=i
            % On multiplie par (x-x(j))/(x(i)-x(j))
            convolution=conv(convolution,([1 -x(j)]))/(x(i)-x(j));
        end
    end
    % On rajoute au polynome de fin le Li calculé
    convolution = convolution * y(i);
    polFin = polFin + convolution;
end

end