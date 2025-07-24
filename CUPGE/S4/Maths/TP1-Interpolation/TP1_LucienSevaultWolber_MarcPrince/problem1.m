% Problème 1

n = [5 15 25 35];
a = -20;
b = 20;

fig = figure('Name','Graphique de sin(x) et pn(x)','NumberTitle','off');

for k=1:length(n)
    xi = tchebyPoints(a, b, n(k));
    yi = xi;
    for i=1:n(k)+1
        yi(i) = sin(xi(i));
    end
    Li = polyLagrange(xi, yi)
    x = linspace(a, b, 100);
    subplot(2,2,k);
    plot(x, polyval(Li, x));
    hold on;
    plot(x, sin(x));
    hold off;
    xlabel('x');
    ylabel('y');
    title(['n=', num2str(n(k))]);
end