#!/usr/bin/env octave
# File: eulermethod.m
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to implement the Euler explicit scheme for y' = -10y with y(1) = 1 """

td = 10;                % time period
dt = 0.01;              % time step
N = td/dt;              % number of steps
t = zeros(N+1, 1);      % time step vector
y = zeros(N+1, 1);      % solution vector
t(1) = 0;              
y(1) = 1;               

for k = 1:N
    t(k+1) = t(k) + dt;
    y(k+1) = y(k) + dt * (-10 * y(k));
end

exact = exp(-10*t);     % exact solution

plot(t, y, 'r+');
hold on;
plot(t, exact, 'k-');
print('eulermethod.png', '-dpng')
