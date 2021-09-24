#!/usr/bin/env julia
# File: leastsquares.jl
# Name: D.Saravanan
# Date: 03/09/2021

""" Program to compute Least-squares """

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")
using LaTeXStrings
using LinearAlgebra

# degree of the polynomial
const M = 10

# data is given at N+1 points
const N = 1000

# true function calculated with equi-spaced nodes
x = LinRange(-1, 1, N+1)
f = 1 ./(1 .+ 25 .* x.^2)

# desired matrix of size (N+1, M+1)
X = ones(N+1, M+1)

for k in 1:M
    X[:, k+1] = x.^k
end

# condition number of the matrix X
const cond_X = cond(X)

# condition number of transpose of X with X
const cond_XX = cond(X'*X)

# QR decomposition of the matrix X
Q, R = qr(X)
Q = Base.ReshapedArray(Q,(N+1,M+1),())

# condition number of the matrix R (same as the condition number of the matrix X)
const cond_R = cond(R)

#println(cond_X, ' ', cond_XX, ' ', cond_R) 

# solution to the equation: R a = Q' f
a = R\Q'*f

# computing the least-squares
ls = X*a

fig, ax = plt.subplots()
ax.plot(x, f, c="olive", ls="dotted", label=L"$\displaystyle\frac{1}{1+25 x^{2}}$")
ax.plot(x, ls, c="teal", label=L"$Least-Squares$")
ax.set(xlim=(-1, 1), ylim=(0, 1.1))
ax.set(xlabel=L"$x$", ylabel=L"$\displaystyle\frac{1}{1+25 x^{2}}$")
ax.set_title(raw"Least-Squares approximation")
ax.grid(true); ax.legend()
plt.savefig("leastsquares.pdf")
