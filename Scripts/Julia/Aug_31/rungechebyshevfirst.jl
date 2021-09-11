#!/usr/bin/env julia
# File: rungechebyshevfirst.jl
# Name: D.Saravanan
# Date: 31/08/2021
# Program to construct the polynomial interpolation
# for Runge Function using Chebyshev nodes of First kind

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


N = 21

xnodes = cos.((2*LinRange(0,N-1,N) .+ 1)/(2*N + 2) * pi)
fnodes = 1 ./(1 .+ 25 .* xnodes.^2)

# true function calculated with equi-spaced nodes
x = LinRange(-1,1,1000)
f = 1 ./(1 .+ 25 .* x.^2)

fintp = interpolate(fnodes, xnodes, x)

error = maximum(abs.(f .- fintp) ./abs.(f))
println(error)

fig, ax = plt.subplots()
ax.plot(x, f, "r", label=L"$N = 21$")
ax.plot(x, fintp, "g", label=L"$N = 21$")
ax.plot(xnodes, fnodes, "b*")
ax.set(xlim=(-1, 1), ylim=(0, 1.1))
ax.set(xlabel=L"$x$", ylabel=L"$\cos\left(\frac{(2x+1) \pi}{2N+2}\right)$")
ax.set_title(raw"Runge Function with Chebyshev nodes of First kind")
ax.grid(true); ax.legend()
plt.savefig("rungechebyshevfirst.pdf")
