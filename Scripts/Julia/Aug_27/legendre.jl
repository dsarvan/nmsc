#!/usr/bin/env julia
# File: legendre.jl
# Name: D.Saravanan
# Date: 27/08/2021

""" Script to calculate and plot Legendre polynomials """

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")
using LaTeXStrings

function Legendre(x, n)
    # recurrence relation of Legendre polynomials
    # P_0 = 1, P_1 = x
    # (n+1)  P_(n+1) = (2n+1) x P_(n) - n P_(n-1)
    n == 0 && return 1
    n == 1 && return x
    ((2(n-1) + 1)*x*Legendre(x, n-1) - (n-1)*Legendre(x, n-2))/n
end

fig, ax = plt.subplots()

for n in 0:4
    
    # interval [-1, 1]
    x = LinRange(-1, 1, 1000)
    y = map(x -> Legendre(x, n), x)

    ax.plot(x, y, label=L"P_{n}(x)")
end

ax.set(xlabel=raw"$x$", ylabel=raw"$P_{n}(x)$")
ax.set_title(raw"Legendre polynomials")
ax.grid(true); ax.legend()
plt.savefig("legendre.png")
