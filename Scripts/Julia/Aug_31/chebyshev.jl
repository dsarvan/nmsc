#!/usr/bin/env julia
# File: chebyshev.jl
# Name: D.Saravanan
# Date: 31/08/2021

""" Script to calculate and plot Chebyshev polynomials of first kind """

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")
using LaTeXStrings

function Chebyshev(x, n)
    # recurrence relation of Chebyshev polynomials of first kind
    # T_0 = 1, T_1 = x
    # T_(n+1) = 2 x T_(n) - T_(n-1)
    n == 0 && return 1
    n == 1 && return x
    2x*Chebyshev(x, n-1) - Chebyshev(x, n-2)
end

fig, ax = plt.subplots()

for n in 0:4

    # interval [-1, 1]
    x = LinRange(-1, 1, 1000)
    y = map(x -> Chebyshev(x, n), x)

    ax.plot(x, y, label=L"T_{n}(x)")
end

ax.set(xlabel=raw"$x$", ylabel=raw"$T_{n}(x)$")
ax.set_title(raw"Chebyshev polynomials")
ax.grid(true); ax.legend()
plt.savefig("chebyshev.png")
