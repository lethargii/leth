% Initialisation des parametres
a = 0;
b = 1;
n = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16392, 32784];
f = @(x)(1./(x.^2+1));

% Definition des methodes de quadrature
methode1 = @(x) intRectG(f, a, b, x);  % Rectangle gauche
%cette methode effectue n evaluations

methode2 = @(x) intRectD(f, a, b, x);  % Rectangle droite
%cette methode effectue n evaluations

methode3 = @(x) intPointsM(f, a, b, x); % Point milieu
%cette methode effectue n evaluations (mais si elle était mal optimisée elle pourrais en faire 2n)

methode4 = @(x) intTrap(f, a, b, x);   % Trapeze
%cette methode effectue n evaluations

methode5 = @(x) intSimson(f, a, b, x); % Simpson
%cette methode effectue 3*(n-1) evaluations
methodes = {methode1, methode2, methode3, methode4, methode5};

temps_calcul = zeros(5, length(n));
for i = 1:length(n)
    for j = 1:5
        methodesj = methodes{j};
        % Mesurer le temps de calcul
        tic;
        methodesj(n(i));
        temps_calcul(j, i) = toc;
    end
end

% Tracer les resultats pour le nombre d'evaluations
figure;
hold on;
for i = 1:2
    if i<2
        plot(n, n, '-x', 'LineWidth', 3);
    else
        plot(n, 3*(n-1),'-x', 'LineWidth', 3);
    end
end
xlabel('n');
ylabel('Nombre évaluations de f(x)');
title('Nombre évaluations de f(x) en fonction de n');
legend('Autres méthodes', 'Methode Simpson');
grid on;
hold off;

% Tracer les resultats pour le temps de calcul
figure;
hold on;
for i = 1:5
    plot(n, temps_calcul(i,:),'-x', 'LineWidth', 3);
end
xlabel('n');
ylabel('Temps de calcul (secondes)');
title('Temps de calcul en fonction de n');
legend('Rectangulaire gauche', 'Rectangulaire droite', 'Points milieu', 'Trapèze', 'Simpson');
grid on;
hold off;

