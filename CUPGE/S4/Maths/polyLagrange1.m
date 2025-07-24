function [polFin] = polyLagrange(x,y)
%   Fonction de la fausse position
%
%   * Entree :
%       --> x - ligne Float - point d'interpolation
%       --> y - ligne Float - image du point d'interpolation
%   * Sortie :
%       --> polFin - ligne Float - Polynome de Lagrange
len=length(x);
polFin=zeros(1,len);
for i=1:len
    convolution=[1];
    for j=1:len
        if j~=i
            convolution=conv(convolution,([1 -x(j)]))/(x(i)-x(j));
        end
    end
    convolution=convolution * y(i);
    polFin = polFin + convolution;
end

end
