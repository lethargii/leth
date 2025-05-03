% Test Gauss

% On charge la petite matrice
load matlab_little;

% On fait la premi�re �tape du pivot de Gauss
[B, c] = gaussStep1(A,b);
disp(B)
disp(c)

% On fait la deuxi�me �tape du pivot de Gauss
x = gaussStep2(B,c);
disp(x)