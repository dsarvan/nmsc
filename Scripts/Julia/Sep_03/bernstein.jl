#!/usr/bin/env julia
# File: bernstein.jl
# Name: D.Saravanan
# Date: 03/09/2021

""" Script to compute Bernstein polynomial """

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")
using LaTeXStrings

function fact(x)
    factorial(big(x))
end

function f(x)
    1 ./(1 .+ 25 .* x.^2)
end

function bernstein(x, M, N)

    bern = zeros(M)

    for k in 0:N
        bern = bern + fact(N)/(fact(N - k)*fact(k)) .* 
                ((x .+ ones(M))./2).^k * ((ones(M) .- x)./2).^(N-k) .* f(2*k/N-1)
    end

    return bern
end

M = 1001
x = LinRange(-1,1,M)
y1 = f(x)

N = 5
y2 = bernstein(x, M, N)
  
fig, ax = plt.subplots()
ax.plot(x, y1, c="olive", ls="dotted", label=L"$\displaystyle\frac{1}{1+25 x^{2}}$")
ax.plot(x, y2, c="teal", label=L"$N = 5$")
ax.grid(true); ax.legend()
plt.savefig("bernstein.png")
