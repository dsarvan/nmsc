#!/usr/bin/env julia
# File: chebyshev.jl
# Name: D.Saravanan
# Date: 27/08/2021

""" Script to calculate and plot Chebyshev polynomials of first kind """

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")
using LaTeXStrings

fig, ax = plt.subplots()

for n in 1:5

    # generate the Chebyshev basis for the polynomial of degree 'n'
    #Tn = 

    # interval [-1, 1]
    x = range(-1, 1, 1000)
    #y = Tn(x)
    println(x)

    ax.plot(x, y, label=raw"$T_{}(x)$".format(n))
end

ax.set(xlabel=raw"$x$", ylabel=raw"$T_{n}(x)$")
ax.set_title(raw"Chebyshev polynomials")
ax.grid(); ax.legend()
plt.savefig("chebyshev.png")
