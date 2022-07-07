#!/usr/bin/env julia
# File: gausslegquad.jl
# Name: D.Saravanan
# Date: 08/03/2022

""" Script to evaluate integral exp(-x^2) from -1 to +1 """

using SciPy
using FastGaussQuadrature, LinearAlgebra

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")
using LaTeXStrings

# exact value of the integral
f = x -> exp(-x^2)
exact = SciPy.integrate.quad(f, -1, 1)[1]

n = []

for k in [2, 5, 10, 20, 50, 100]

    n.append(k)
    
    # nodes and weights calculations
    x, w = gausslegendre(k)

    # integration
    integral = (w' * f.(x))

    # error calculation
    error = abs(integral - exact)

end

fig, ax = plt.subplots()
ax.loglog(n, error, "r.--", label=raw"Gauss-Legendre")
ax.set_title(raw"Error plot of Gauss-Legendre quadrature")
ax.set(xlabel=raw"n", ylabel=raw"error in quadrature")
ax.grid(true); ax.legend()
plt.savefig("gausslegquad.png")
