#!/usr/bin/env julia
# File: legendre.jl
# Name: D.Saravanan
# Date: 31/08/2021

""" Script to calculate and plot Legendre polynomials """

using Polynomials
using SpecialPolynomials
using LaTeXStrings

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")

fig, ax = plt.subplots()

for n in 0:4
    
    Pn = convert(Polynomial, basis(Legendre, n))

    x = LinRange(-1, 1, 1000)
    y = map(x -> Pn(x), x)

    ax.plot(x, y, label=L"P_{n}(x)")
end

ax.set(xlabel=raw"$x$", ylabel=raw"$P_{n}(x)$")
ax.set_title(raw"Legendre polynomials")
ax.grid(true); ax.legend()
plt.savefig("legendre.png")
