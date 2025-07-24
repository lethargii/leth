% Comparaison de méthodes

% Test pour la petite matrice

load matlab_little.mat;

x = [1; 2; -1; 1];

% Méthode de Gauss
tic;
    [B, c] = gaussStep1(A,b);
    res = gaussStep2(B,c);
tempG = toc;
errGauss = sum(abs(res-x));

% Méthode de Cholesky
tic;
    res = resCholesky(A, b);
tempC = toc;
errCholesky = sum(abs(res-x));

% Méthode de Jacobi
tic;
resJacobi(A, b, 10^-5, 10);
tempsJ5 = toc;
errJacobi5 = sum(abs(res-x));
tic;
resJacobi(A, b, 10^-10, 300);
tempsJ10 = toc;
errJacobi10 = sum(abs(res-x));
tic;
resJacobi(A, b, 10^-15, 300);
tempsJ15 = toc;
errJacobi15 = sum(abs(res-x));
tic;
resJacobi(A, b, 10^-20, 300);
tempsJ20 = toc;
errJacobi20 = sum(abs(res-x));


% Comparaison vitesse et erreur
% Tableaux de comparaison des temps d'exécution et des erreurs
tabTempLittle = [tempG, tempC, tempsJ15, tempsJ20];
tabErreurLittle = [errGauss, errCholesky, errJacobi15, errJacobi20];

% Tests pour la matrice moyenne

load matlab_medium.mat;


% Méthode de Gauss
tic;
    [B, c] = gaussStep1(A,b);
    res = gaussStep2(B,c);
tempG = toc;
errGauss = sum(abs(res-ans));

% Méthode de Cholesky
tic;
    res = resCholesky(A, b);
tempC = toc;
errCholesky = sum(abs(res-ans));

% Méthode de Jacobi
tic;
resJacobi(A, b, 10^-5, 10);
tempsJ5 = toc;
errJacobi5 = sum(abs(res-ans));
tic;
resJacobi(A, b, 10^-10, 300);
tempsJ10 = toc;
errJacobi10 = sum(abs(res-ans));
tic;
resJacobi(A, b, 10^-15, 300);
tempsJ15 = toc;
errJacobi15 = sum(abs(res-ans));
tic;
resJacobi(A, b, 10^-20, 300);
tempsJ20 = toc;
errJacobi20 = sum(abs(res-ans));


% Comparaison vitesse et erreur
% Tableaux de comparaison des temps d'exécution et des erreurs
tabTempMedium = [tempG, tempC, tempsJ15, tempsJ20];
tabErreurMedium = [errGauss, errCholesky, errJacobi15, errJacobi20];

disp("temps")
disp(tabTempLittle)
disp(tabTempMedium)
disp("erreur")
disp(tabErreurLittle)
disp(tabErreurMedium)