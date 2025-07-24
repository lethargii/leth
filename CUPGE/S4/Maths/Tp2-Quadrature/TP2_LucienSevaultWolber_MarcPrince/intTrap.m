function [aire] = intTrap(f, a, b, n)
   aire = 0; %On initialise l'aire à 0
   x = linspace(a, b, n);
   y = f(x);
   h = x(2) - x(1);
   for i=1:n-1
     aire = aire + (y(i)+y(i+1))*h/2; %On ajoute n fois à aire les trapèzes formés
   end