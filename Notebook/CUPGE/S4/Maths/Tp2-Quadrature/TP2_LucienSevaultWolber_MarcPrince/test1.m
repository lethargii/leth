a=0;
b=1;
n=[2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16392, 32784];
f=@(x)(1./(x.^2+1));
methode1=@(x)intRectG(f,a,b,x);
methode2=@(x)intRectD(f,a,b,x);
methode3=@(x)intPointsM(f,a,b,x);
methode4=@(x)intTrap(f,a,b,x);
methode5=@(x)intSimson(f,a,b,x);
methodes={methode1,methode2,methode3,methode4,methode5};
erreur=zeros(5,length(n));
for i=1:length(n)
    for j=1:5
        methodesj=methodes{j};
        erreur(j,i)=log10(abs(pi/4-methodesj(n(i))));
    end
end
disp(erreur);

h=zeros(length(n),1);
for i=1:length(n)
    h(i,1)=(b-a)/n(i);
end
erreur=erreur';
hold on;
grid on;
for i=1:5
    plot(log10(h),erreur(:,i),'-x');
end
xlabel('log10(h)');
ylabel('log10(erreur)');
title('Erreur en fonction de log10(h) pour differentes methodes');
legend('Methode Rectangle gauche', 'Methode Rectangle droit', 'Methode Points Milieu', 'Methode Trapeze', 'Methode Simpson');
grid on;
hold off;