#!/usr/bin/env julia
# File: hermite.py
# Name: D.Saravanan
# Date: 31/08/2021

""" Script to calculate and plot Hermite polynomials """

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

for n in 0:3
    
    Hn = convert(Polynomial, basis(Hermite, n))

    x = LinRange(-2, 2, 1000)
    y = map(x -> Hn(x), x)

    ax.plot(x, y, label=L"H_{n}(x)")
end

ax.set(xlabel=raw"$x$", ylabel=raw"$H_{n}(x)$", ylim=(-10,10))
ax.set_title(raw"Hermite polynomials")
ax.grid(true); ax.legend()
plt.savefig("hermite.png")
