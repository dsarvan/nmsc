#!/usr/bin/env julia
# File: finitedifference.jl
# Name: D.Saravanan
# Date: 13/09/2021

""" Program to compute derivative of a function using finite-difference """

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")
using LaTeXStrings

f = x -> sin(x)/x^3
g = x -> cos(x)/x^3 - 3*sin(x)/x^4

x = 4

# N different grid spacing
N = 30

h = map(k -> 1 ./(2 .^k), 1:N)
forward = map(k -> (f(x .+ h[k]) .- f(x))./h[k], 1:N)
backwrd = map(k -> (f(x) .- f(x .- h[k]))./h[k], 1:N)
central = map(k -> (f(x .+ h[k]) .- f(x .- h[k]))./(2*h[k]), 1:N)
fourthd = map(k -> (-f(x .+ 2*h[k]) .+ 8*f(x .+ h[k]) .- 8*f(x .- h[k]) .+ f(x .- 2*h[k]))./(12*h[k]), 1:N)

fig, ax = plt.subplots()
ax.loglog(h, abs.(forward .- g(x)), label=raw"forward")
ax.loglog(h, abs.(backwrd .- g(x)), label=raw"backwrd")
ax.loglog(h, abs.(central .- g(x)), label=raw"central")
ax.loglog(h, abs.(fourthd .- g(x)), label=raw"fourthd")
ax.grid(true); ax.legend()

plt.savefig("finite.png")
