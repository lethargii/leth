function [aire] = intRectG(f, a, b, n)
aire=0; %On initialise l'aire à 0
Points=linspace(a,b,n);
y=f(Points);
distPP=Points(2)-Points(1);
for i=1:n-1
    aire=aire+y(i)*distPP; %On ajoute n fois à aire les rectangles formés
end
end