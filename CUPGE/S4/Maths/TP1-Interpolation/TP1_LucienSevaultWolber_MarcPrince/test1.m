% Test 1
% On essaie avec la fonction 2x^2 + 1
func=[2 0 1];
% On teste pour n = 1, 2
n = length(func);
figure('Name','Graphique de f(x) et pn(x)','NumberTitle','off');
for i=1:n
  % On prend i + 1 points d'interpolation entre -10 et 10
  xi=linspace(-10,10,i+1);
  % On calcule les yi
  yi=polyval(func,xi);
  % On calcule le polynome interpolateur
  polyLg=polyLagrange(xi,yi);
  % Créer le graphique
  subplot(1,2,i);
  % On affiche la courbe réelle et le polynome interpolateur
  x=linspace(-10,10,100);
  plot(x, polyval(func,x), 'r');
  hold on;                      
  plot(x, polyval(polyLg,x), 'b'); 
  hold off;     
  % On ajoute des labels et une légende
  xlabel('x');
  ylabel('y');
  legend('f(x)', 'pn(x)');
  title(['n=', num2str(i)]);
end