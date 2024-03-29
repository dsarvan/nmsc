#!/usr/bin/env julia
# File: laguerre.jl
# Name: D.Saravanan
# Date: 31/08/2021

""" Script to calculate and plot Laguerre polynomials """

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

    Ln = convert(Polynomial, basis(Laguerre{0}, n))

    x = LinRange(-4, 7, 1000)
    y = map(x -> Ln(x), x)

    ax.plot(x, y, label=L"L_{n}(x)")
end

ax.set(xlabel=raw"$x$", ylabel=raw"$L_{n}(x)$", xlim=(-2,5), ylim=(-4,4))
ax.set_title(raw"Laguerre polynomials")
ax.grid(true); ax.legend()
plt.savefig("laguerre.png")
