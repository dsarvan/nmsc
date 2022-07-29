#!/usr/bin/env julia
# File: rungelegendre.jl
# Name: D.Saravanan
# Date: 31/08/2021

""" Script to construct the polynomial interpolation
for Runge Function using Legendre nodes """

using FastGaussQuadrature
using LaTeXStrings

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")

function interpolate(fnodes, xnodes, x)

    M, N = length(x), length(xnodes)
    res = zeros(M)

    for i in 1:N
        res = res + fnodes[i] * lagrange(xnodes, x, i)
    end
    
    return res
end

function lagrange(xnodes, x, i)

    M, N = length(x), length(xnodes)
    val = ones(M)

    for j in 1:N
        
        if i == j
            continue
        end

        val = val .* (x .- xnodes[j]) / (xnodes[i] - xnodes[j])
    end

    return val
end

N = 21

xnodes, weights = gausslegendre(N)
fnodes = 1 ./(1 .+ 25 .* xnodes.^2)

# true function calculated with equi-spaced nodes
x = LinRange(-1,1,1000)
f = 1 ./(1 .+ 25 .* x.^2)

fintp = interpolate(fnodes, xnodes, x)

error = maximum(abs.(f .- fintp) ./abs.(f))
println(error)

fig, ax = plt.subplots()
ax.plot(x, f, c="olive", ls="dotted", label=L"$\displaystyle\frac{1}{1+25 x^{2}}$")
ax.plot(x, fintp, c="teal", label=L"$Interpolation$")
ax.plot(xnodes, fnodes, "m.", label=L"$N = 21$")
ax.set(xlim=(-1, 1), ylim=(0, 1.1))
ax.set(xlabel=L"$x$", ylabel=L"$\displaystyle\frac{1}{1+25 x^{2}}$")
ax.set_title(raw"Runge Function with Legendre nodes")
ax.grid(true); ax.legend()
plt.savefig("rungelegendre.png")
