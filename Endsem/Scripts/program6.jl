#!/usr/bin/env julia

# Program to implement the different quadrature and see how the error behaves


import PyPlot
const plt = PyPlot


using LaTeXStrings
using FastGaussQuadrature

# end points of interval
a, b = -1, 1

# function to be integrated
f = x -> exp.(-x.^2)

# derivative of the function
g = x -> -2*x*exp(-x.^2)

# exact value of the integral
exact = 1.49364826562485405080

# number of grid points
N = [2, 5, 10, 20, 50, 100]

# number of different set of grids
Ngrids = length(N)

h = zeros(Ngrids)

trap = zeros(Ngrids)
tend = zeros(Ngrids)
tent = zeros(Ngrids)
gleg = zeros(Ngrids)

for (k, N) in enumerate(N)
    h[k] = (b - a)/(N - 1)
    x = LinRange(a, b, N)

    # nodes and weights calculation of gauss-legendre
    xnode, wnode = gausslegendre(N)

    trap[k] = h[k]*(sum(f(x)) - (f(a) + f(b))/2)
    tend[k] = trap[k] - (h[k]^2 / 12) * (g(b) - g(a))
    tent[k] = tend[k] + (h[k]^4 / 720) * (g(b) - g(a))
    gleg[k] = wnode'.*f(xnode)

end

# error calculations
trap_error = abs(trap - exact)
tend_error = abs(tend - exact)
tent_error = abs(tent - exact)
gleg_error = abs(gleg - exact)
