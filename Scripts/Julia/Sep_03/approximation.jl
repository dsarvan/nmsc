#!/usr/bin/env julia
# File: approximation.jl
# Name: D.Saravanan
# Date: 03/09/2021

""" Program to compare the convergence """

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")
using LaTeXStrings
using LinearAlgebra

function interpolate(fnodes, xnodes, x)
    
    m, n = length(x), length(xnodes)
    p = zeros(m)

    for i in 1:n
        p = p + fnodes[i] * lagrange(xnodes, x, i)
    end

    return p 
end

function lagrange(xnodes, x, i)
    
    m, n = length(x), length(xnodes)
    l = ones(m)

    for j in 1:n

        if i == j
            continue
        end

        l = l .* (x .- xnodes[j]) / (xnodes[i] - xnodes[j])
    end

    return l
end

function fact(x)
    factorial(big(x))
end

# degree of the polynomial
n = 10

# data is given at N+1 points
N = 1000

# true function calculated with equi-spaced nodes
x = LinRange(-1, 1, N+1)
f = x -> 1 ./(1 .+ 25 .* x.^2)

""" polynomial interpolation using Chebyshev nodes of first kind """
m = n-1  # polynomial of degree m
xnodes = cos.((2*LinRange(0,m-1,m) .+ 1)/(2*m + 2) * pi)
fnodes = 1 ./(1 .+ 25 .* xnodes.^2)
fintpt = interpolate(fnodes, xnodes, x)

""" polynomial approximation using Bernstein polynomials """
bern = sum(map(k -> fact(n)/(fact(n-k)*fact(k)) .*
                 ((x .+ 1)./2).^k .* ((1 .- x)./2).^(n-k) .* f(2*k/n-1), 0:n))

""" computing Least-Squares approximation """
# desired matrix of size (N+1, n+1)
X = ones(N+1, n+1)

for k in 1:n
    X[:, k+1] = x.^k
end

# condition number of the matrix X
const cond_X = cond(X)

# condition number of transpose of X with X
const cond_XX = cond(X'*X)

# QR decomposition of the matrix X
Q, R = qr(X)
Q = Base.ReshapedArray(Q,(N+1,n+1),())

# condition number of the matrix R (same as the condition number of the matrix X)
const cond_R = cond(R)

# solution to the equation: R a = Q' f
a = R\Q'*f(x)

# computing the least-squares
ls = X*a

fig, ax = plt.subplots()
ax.plot(xnodes, fnodes, "k.", label=L"$n = 10$")
ax.plot(x, f(x), c="#005249", ls="dotted", label=L"$\displaystyle\frac{1}{1+25 x^{2}}$")
ax.plot(x, ls, c="#fdb915", ls="dotted", label=L"$Least-Squares$")
ax.plot(x, fintpt, c="#f5054f", ls="dotted", label=L"$Interpolation$")
ax.plot(x, bern, c="#952e8f", ls="dotted", label=L"$Bernstein$")
ax.set(xlim=(-1, 1), ylim=(0, 1.1))
ax.set(xlabel=L"$x$", ylabel=L"$\displaystyle\frac{1}{1+25 x^{2}}$")
ax.set_title(raw"Interpolation and Approximation")
ax.grid(true); ax.legend()
plt.savefig("approximation.pdf")
