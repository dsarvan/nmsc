#!/usr/bin/env julia
# File: vandermonde.jl
# Name: D.Saravanan
# Date: 24/08/2021

""" Script to compute the condition number of Vandermonde matrix """

using LinearAlgebra

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")
using LaTeXStrings

function vander(t,n)
    m = length(t)
    V = zeros(m,n)
    for i = 1:m
        for j = 1:n
            V[i,j] = t[i]^(j-1)
        end
    end
    return V
end

x1 = Int64[]
x2 = Float64[]

for (i, N) in enumerate(5:2:35)
    x = range(-1,1,N)
    V = vander(x, N)
    push!(x1, i)
    push!(x2, cond(V))
end

fig, ax = plt.subplots()
ax.set_yscale("log")
ax.plot(x1, x2)
ax.set(xlim=(0, 20), ylim=(10^1, 10^27))
ax.set(xlabel="", ylabel="cond(V)")
ax.set_title(raw"condition number of Vandermonde matrix for N $\in [5,35]$", fontsize=10)
ax.grid(true)
plt.savefig("graph.png")
