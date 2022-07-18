#!/usr/bin/env julia
# File: hermite.jl
# Name: D.Saravanan
# Date: 27/08/2021

""" Script to calculate and plot Hermite polynomials """

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")
using LaTeXStrings

function Hermite(x, n)
    n == 0 && return 1
    n == 1 && return 2*x
    2x*Hermite(x, n-1) - 2(n-1)*Hermite(x, n-2)    
end

fig, ax = plt.subplots()

for n in 0:3
    
    # interval [-2, 2]
    x = LinRange(-2, 2, 1000)
    y = map(x -> Hermite(x, n), x)

    ax.plot(x, y, label=L"H_{n}(x)")
end

ax.set(xlabel=raw"$x$", ylabel=raw"$H_{n}(x)$", ylim=(-10,10))
ax.set_title(raw"Hermite polynomials")
ax.grid(true); ax.legend()
plt.savefig("hermite.png")
