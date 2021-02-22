#!/usr/bin/env octave 
% File: recurrence.m
% Name: D.Saravanan
% Date: 19/02/2021
% Octave script to obtain I_(n) by recurrence relation

N = 15              % Number of terms in the recurrence
I = zeros(N,1)      % initialize vector of N elements
I(1) = 0.63662      % initial condition I0 = 0.31831

for n = 1:N
    I(n+1) = (-1/pi) * 1^(2*n) * cos(pi) + (2*n)/(pi^2) * 1^(2*n - 1) * sin(pi) - ((2*n)*(2*n - 1)/(pi^2)) * I(n)
end
