#!/usr/bin/env julia
# File: numerical.jl
# Name: D.Saravanan
# Date: 10/03/2022

""" Script to compute the integral f(x) = cos(20*pi*x) exp(-x**2) on the interval [-1, 1] """

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
f = x -> cos(20*pi*x) * exp(-x^2)
exact = SciPy.integrate.quad(f, -1, 1)[1]

x = range(-1, 1, 1000)

N = range(1, 80)
n = Array(N)

Ngrids = length(N)

gleg = zeros(Ngrids)

for (k, N) in enumerate(N)
    
    # nodes and weights calculation of gauss-legendre
    xnode, wnode = gausslegendre(N)

    gleg[k] = (wnode' * f.(xnode))

end

# error calculations
gleg_err = abs.(gleg .- exact)

fig, ax = plt.subplots(1, 2, figsize=(10,4))
ax[1].plot(x, f.(x))
ax[1].set(xlim=(-1, 1), xticks=-1.0:0.5:1.5)
ax[1].set(ylim=(-1, 1), yticks=-1.0:0.2:1.0)
ax[1].set(xlabel=raw"x", ylabel=raw"f(x)")
ax[1].tick_params(direction="in")
ax[2].semilogy(n, gleg_err)
ax[2].set(xlim=(0, 80), xticks=0:10:90)
ax[2].set(ylim=(10^-17, 10))
ax[2].set(xlabel=raw"number of points", ylabel=raw"quadrature error")
ax[2].tick_params(direction="in")
fig.tight_layout()
plt.savefig("numerical.png")
