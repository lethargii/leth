function [aire] = intSimson(f, a, b, n)
aire=0; %On initialise l'aire à 0
x=linspace(a,b,n);
distPP=x(2)-x(1);
for i=1:n-1
    aire=aire+distPP/6*((4*f((x(i)+x(i+1))/2)+f(x(i))+f(x(i+1)) )); %On applique la formulle donnée
end

end