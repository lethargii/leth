% Problème 3
% On teste pour n = 5, 10, 15, 20
n = [2 3 4 5 6 7 8 9];
normes = zeros(1, length(n));
func = @(x)1./(1+25*x.^2);
for k=1:length(n)
  % On prend i + 1 points d'interpolation entre -1 et 1
  xi=linspace(-10,10,n(k)+1);
  yi=func(xi);
  zi=gradient(yi,xi);
  pn=polyHermite(xi,yi,zi);
  
  % Créer le graphique
  subplot(3,3,k);
  x=linspace(-10,10,100);
  plot(x, func(x), 'r');
  hold on;
  plot(x, polyval(pn,x), 'b');
  hold off;
  % On calcule la norme infinie de l'erreur
  erreur = abs(func(x)-polyval(pn, x));
  normes(k) = max(erreur);
  % Ajouter des labels et une légende
  xlabel('x');
  ylabel('y');
  legend('f(x)', 'pn(x)');
  title(['n=', num2str(n(k))]);
end

figure(2)
plot(log10(n), log10(normes));
xlabel('x');
ylabel('y');
legend('log(err)', 'pn(x)');
title("log(err) en fonction de log(n)");