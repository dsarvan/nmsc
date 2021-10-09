#!/usr/bin/env octave
# File: finitedifference.m
# Name: D.Saravanan
# Date: 08/10/2021
# Script to compute derivative of sin(x)/x^3 at x = 4 using finite-difference

f = @(x) sin(x)/x^3;
g = @(x) cos(x)/x^3 - 3*sin(x)/x^4;

x = 4;

# N different grid spacing
N = 10;

h = zeros(N,1);         # different grid spacing

forward = zeros(N,1);   # Forward difference
backwrd = zeros(N,1);   # Backward difference
central = zeros(N,1);   # Central difference
fourthd = zeros(N,1);   # Fourth order difference

for k = 1:N
    h(k) = 1/2^k; # decrease the grid spacing by a factor of 1/2 every single time

    forward(k) = (f(x + h(k)) - f(x))/h(k);
    backwrd(k) = (f(x) - f(x - h(k)))/h(k);
    central(k) = (f(x + h(k)) - f(x - h(k)))/(2*h(k));
    fourthd(k) = (-f(x + 2*h(k)) + 8*f(x + h(k)) - 8*f(x - h(k)) + f(x - 2*h(k)))/(12*h(k));
end

figure;  loglog(h, abs(forward - g(x)), 'r+-');
hold on; loglog(h, abs(backwrd - g(x)), 'r+-');
hold on; loglog(h, abs(central - g(x)), 'b+-');
hold on; loglog(h, abs(fourthd - g(x)), 'k+-');
xlabel('grid size'); ylabel('error in derivative');
legend('forward', 'backwrd', 'central', 'fourthd');
set(legend, 'location', 'northwest');
set(gca, 'title', text('string', 'Finite-difference convergence'));
grid on; print('convergence.pdf', '-dpdf')
