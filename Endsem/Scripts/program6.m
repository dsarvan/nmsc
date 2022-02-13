#!/usr/bin/env octave
# File: program6.m
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to implement quadrature methods and see how the eroor behaves """

f = @(x) exp(-x^2)

exact = 1.49364826562485405080

N = [2, 5, 10, 20, 50, 100]

Ngrids = length(N)

gleg = zeros(Ngrids);

for N = [2, 5, 10, 20, 50, 100]
    [xnode, wnode] = GaussLegendre(N);
    gleg = sum(wnode.*f(xnode));
end

glegerr = gleg - exact
fprintf(glegerr)
