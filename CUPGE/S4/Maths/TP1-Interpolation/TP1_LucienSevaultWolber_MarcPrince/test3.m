% Test 3
% On crée la fonction 1/(1+25x^2)
func=@(x)1./(1+25*x.^2);
% On teste pour n = 5, 10, 15, 20
n = [2 3 5 10 15 20 25 30];
normesequi = zeros(1, length(n));
normestcheby = zeros(1, length(n));
for k=1:length(n)
  % On prend i + 1 points d'interpolation entre -1 et 1
  xi=linspace(-1,1,n(k)+1);
  yi=func(xi);
  pnequi=polyLagrange(xi,yi);
  xi=tchebyPoints(-1,1,n(k));
  yi=func(xi);
  pntcheby=polyLagrange(xi,yi);
  
  % Créer le graphique
  subplot(3,3,k);
  x=linspace(-1,1,100);
  plot(x, func(x), 'r');
  hold on;
  plot(x, polyval(pntcheby,x), 'b');
  hold off;
  % On calcule la norme infinie de l'erreur
  erreurequi = abs(func(x)-polyval(pnequi, x));
  normesequi(k) = max(erreurequi);
  erreurtcheby = abs(func(x)-polyval(pntcheby, x));
  normestcheby(k) = max(erreurtcheby);
  % Ajouter des labels et une légende
  xlabel('x');
  ylabel('y');
  legend('f(x)', 'pn(x)');
  title(['n=', num2str(n(k))]);
end

figure(2)
plot(log10(n), log10(normesequi));
hold on;
plot(log10(n), log10(normestcheby));
hold off;
xlabel('x');
ylabel('y');
legend('log(err,equi)','log(err,tcheby)');
title("log(err) en fonction de log(n)");