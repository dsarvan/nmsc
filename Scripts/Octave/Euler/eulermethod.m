#!/usr/bin/env octave
# File: eulermethod.m
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to implement the Euler explicit & implicit scheme for y' = -0.5*y with y(1) = 1 """

t_ = 25;                    # time period
dt = 0.5;                   # time step
N = t_/dt;                  # number of steps
t = zeros(N+1, 1);          # time vector
y1 = ones(N+1, 1);          # solution vector of euler explicit
y2 = ones(N+1, 1);          # solution vector of euler implicit

for k = 1:N
    t(k+1) = t(k) + dt;
    y1(k+1) = y1(k)*(1 - 0.5*dt);
    y2(k+1) = y2(k)/(1 + 0.5*dt);
end

exact = exp(-0.5*t);        # exact solution

figure;  plot(t, y1, 'r*');
hold on; plot(t, y2, 'b*');
hold on; plot(t, exact, 'k-');
xlabel('t'); ylabel('y(t)');
legend('euler explicit', 'euler implicit', 'exact solution');
set(legend, 'location', 'northeast');
set(gca, 'title', text('string', 'Euler explicit and implicit scheme'));
grid on; print('eulermethod.png', '-dpng')
