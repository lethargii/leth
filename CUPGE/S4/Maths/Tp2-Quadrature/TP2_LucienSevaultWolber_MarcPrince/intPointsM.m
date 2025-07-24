function [aire] = intPointsM(f, a, b, n)
aire=0; %On initialise l'aire à 0
Points=linspace(a,b,n);
distPP=Points(2)-Points(1);
Points=Points+distPP/2;
y=f(Points);
for i=1:n-1
    aire=aire+y(i)*distPP; %On ajoute n fois à aire les rectangles formés
end
end