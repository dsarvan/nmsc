#!/usr/bin/env octave
% File: vandermonde.m
% Name: D.Saravanan
% Date: 24/08/2021
% Scirpt to compute the condition number of Vandermonde matrix

C = [];

for N = 5:2:35
    x = linspace(-1,1,N);
    V = vander(x);
    C = [C, cond(V)]
end

semilogy(C);
set(gca, "ylabel", text("string", "cond(V)", "fontsize", 10));
set(gca, "title", text("string", "condition number of Vandermonde matrix for N in [5,35]"));
grid on;
print('graph.png', '-dpng');
