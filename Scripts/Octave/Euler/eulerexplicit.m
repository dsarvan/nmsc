#!/usr/bin/env octave
# File: eulerexplicit.m
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to implement the Euler explicit scheme for y' = -10y with y(1) = 1 """

t_ = 10;                # time period
dt = 0.02;              # time step
N = t_/dt;              # number of steps
t = zeros(N+1, 1);      # time vector
y = zeros(N+1, 1);      # solution vector of euler explicit
t(1) = 0;              
y(1) = 1;               

for k = 1:N
    t(k+1) = t(k) + dt;
    y(k+1) = y(k) + dt * (-10 * y(k));
end

exact = exp(-10*t);     # exact solution

figure;  plot(t, y, 'r+');
hold on; plot(t, exact, 'k-');
xlabel('t'); ylabel('y(t)');
legend('euler explicit', 'exact solution');
set(legend, 'location', 'northeast');
set(gca, 'title', text('string', 'Euler explicit scheme'));
grid on; print('eulerexplicit.png', '-dpng')
