#!/usr/bin/env julia
# File: polynomial.jl
# Name: D.Saravanan
# Date: 27/08/2021

""" Program to construct the polynomial interpolation
using Lagrange polynomial """

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")
using LaTeXStrings

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


N = 9

xnodes = LinRange(-1,1,N)
fnodes = sin.(pi .* xnodes)

# true function calculated with equi-spaced nodes
x = LinRange(-1,1,1000)
f = sin.(pi .* x)

fintp = interpolate(fnodes, xnodes, x)

error = maximum(abs.(f .- fintp) ./abs.(f))
println(error)

fig, ax = plt.subplots()
ax.plot(x, f, c="olive", ls="dotted", label=L"$\sin(\pi x)$")
ax.plot(x, fintp, c="teal", label=L"$Interpolation$")
ax.plot(xnodes, fnodes, "m.", label=L"$N = 9$")
ax.set(xlim=(-1, 1), ylim=(-1.1, 1.1))
ax.set(xlabel=L"$x$", ylabel=L"$\sin(\pi x)$")
ax.set_title(raw"Lagrange polynomial interpolation")
ax.grid(true); ax.legend()
plt.savefig("polynomial.pdf")
