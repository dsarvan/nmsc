#!/usr/bin/env octave

M = 10;
N = 1000;

x = linspace(-1, 1, N+1);

X = ones(N+1, M+1);

for k = 1:M
    X(:, k+1) = x.^k;
end

cond(X)
cond(X'*X)

[Q,R] = qr(X);
cond(R)

f = 1./(1 + 25 * x.^2);

a = R\(Q'.*f);
#disp(a)

f_LS = X.*a;
#disp(f_LS)

figure;
plot(x, f, 'r-');
hold on;
plot(x, f_LS, 'k-');
hold on;
legend('Function', 'Least Square');
grid on;
print('leastsquare.png', '-dpng')
