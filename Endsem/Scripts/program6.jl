#!/usr/bin/env julia
# File: program6.jl
# Name: D.Saravanan
# Date: 02/12/2021

""" Program to implement the different quadrature and see how the error behaves """

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")
using LaTeXStrings
using LinearAlgebra
using FastGaussQuadrature

# end points of interval
a, b = -1, 1

# function to be integrated
f = x -> exp.(-x.^2)

# first derivative of the function
g = x -> -2*x*exp(-x.^2)

# third derivative of the function
s = x -> 4*x*(3 - 2*x.^2)*exp(-x.^2)

# exact value of the integral
exact = 1.49364826562485405080

# number of grid points
N = [2, 5, 10, 20, 50, 100]

# number of different set of grids
Ngrids = length(N)

h = zeros(Ngrids)

trap = zeros(Ngrids)    # trapezoidal rule
tend = zeros(Ngrids)    # trapezoidal rule using first derivative
tent = zeros(Ngrids)    # trapezoidal rule using first and third derivative
gleg = zeros(Ngrids)    # gauss-legendre quadrature rule

for (k, N) in enumerate(N)
    h[k] = (b - a)/(N - 1)
    x = LinRange(a, b, N)

    # nodes and weights calculation of gauss-legendre
    xnode, wnode = gausslegendre(N)

    trap[k] = h[k]*(sum(f(x)) - (f(a) + f(b))/2)
    tend[k] = trap[k] - (h[k]^2 / 12) * (g(b) - g(a))
    tent[k] = tend[k] + (h[k]^4 / 720) * (s(b) - s(a))
    gleg[k] = dot(wnode, f(xnode))
end

# error calculations
trap_err = abs.(Float64.(trap .- exact))
tend_err = abs.(Float64.(tend .- exact))
tent_err = abs.(Float64.(tent .- exact))
gleg_err = abs.(Float64.(gleg .- exact))

println(gleg_err)

fig, ax = plt.subplots()
ax.loglog(h, trap_err, "b.--", label=raw"trapezoidal rule")
ax.loglog(h, tend_err, "r.--", label=raw"trapezoidal rule using 1st derivative")
ax.loglog(h, tent_err, "m.--", label=raw"trapezoidal rule using 1st and 3rd derivative")
ax.loglog(h, gleg_err, "g.--", label=raw"gauss-legendre quadrature rule")
ax.set(xlabel=raw"grid size", ylabel=raw"error in quadrature")
ax.set_title(raw"Quadrature convergence")
ax.grid(true); ax.legend()
plt.savefig("program6.png")
