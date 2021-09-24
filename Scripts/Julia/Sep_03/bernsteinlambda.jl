#!/usr/bin/env julia
# File: bernsteinlambda.jl
# Name: D.Saravanan
# Date: 03/09/2021

""" Program to compute Bernstein polynomial using lambda function """

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")
using LaTeXStrings

function fact(n)
    factorial(big(n))
end

const M = 1001
x = LinRange(-1,1,M)
f = x -> 1 ./(1 .+ 25 .* x.^2)

const N = 5
Bern = sum(map(k -> fact(N)/(fact(N-k)*fact(k)) .*
                 ((x .+ 1)./2).^k .* ((1 .- x)./2).^(N-k) .* f(2*k/N-1), 0:N))

fig, ax = plt.subplots()
ax.plot(x, f(x), c="olive", ls="dotted", label=L"$\displaystyle\frac{1}{1+25 x^{2}}$")
ax.plot(x, Bern, c="teal", label=L"$Bernstein$")
ax.set(xlim=(-1, 1), ylim=(0, 1.1))
ax.set(xlabel=L"$x$", ylabel=L"$\displaystyle\frac{1}{1+25 x^{2}}$")
ax.set_title(raw"Bernstein polynomial")
ax.grid(true); ax.legend()
plt.savefig("bernsteinlambda.pdf")
