#!/usr/bin/env octave
# File: program6.m
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to implement quadrature methods and see how the eroor behaves """

# function to be integrated
f = @(x) exp(-x^2)

# exact value of the integral
exact = 1.49364826562485405080

# number of grid points
N = [2, 5, 10, 20, 50, 100]

# number of different set of grids
Ngrids = length(N)

gleg = zeros(Ngrids);   # gauss-legendre quadrature rule 

for N = [2, 5, 10, 20, 50, 100]
    [xnode, wnode] = GaussLegendre(N);
    gleg = sum(wnode.*f(xnode));
end

# error calculations
gleg_err = abs(gleg - exact)
fprintf(glegerr)
