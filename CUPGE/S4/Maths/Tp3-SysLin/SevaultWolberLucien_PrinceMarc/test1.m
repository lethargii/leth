% test1

% On charge la petite matrice et on teste Jacobi
load matlab_little

x = resJacobi(A, b, 10**-3, 15)

x = resJacobi(A, b, 10**-5, 15)

% On charge la matrice moyenne et on teste Jacobi
load matlab_medium

x = resJacobi(A, b, 10**-5, 30)