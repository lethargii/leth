% Test 2
% On crée la fonction 1/(1+25x^2)
func=@(x)1./(1+25*x.^2);
% On teste pour n = 5, 10, 15, 20
n = [2 3 5 10 15 20 25 30];
normes = zeros(1, length(n));
figure('Name','Graphique de f(x) et pn(x)','NumberTitle','off');
for k=1:length(n)
  % On prend i + 1 points d'interpolation entre -1 et 1
  xi=linspace(-1,1,n(k)+1);
  yi=func(xi);
  pn=polyLagrange(xi,yi);
  
  

  % Créer le graphique
  subplot(3,3,k);
  x=linspace(-1,1,100);
  plot(x, func(x), 'r');  % Trace func(x) en rouge
  hold on;                         % Garde le graphique actuel
  plot(x, polyval(pn,x), 'b');  % Trace polyLg(x) en bleu
  hold off;                        % Libère le graphique pour les autres tracés
  
  % On calcule la norme infinie de l'erreur
  erreur = abs(func(x)-polyval(pn, x));
  normes(k) = max(erreur);

  % Ajouter des labels et une légende
  xlabel('x');
  ylabel('y');
  legend('fn(x)', 'pn');
  title(['n=', num2str(n(k))]);
end

figure(2)
plot(log10(n), log10(normes));
xlabel('x');
ylabel('y');
legend('log(err)');
title("log(err) en fonction de log(n)");