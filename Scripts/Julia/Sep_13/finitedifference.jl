#!/usr/bin/env julia
# File: finitedifference.jl
# Name: D.Saravanan
# Date: 13/09/2021

""" Program to compute derivative of sin(x)/x^3 at x = 4 using finite-difference """

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
N = 10

# different grid spacing
h = map(k -> 1 ./(2 .^k), 1:N)

forward = map(k -> (f(x .+ h[k]) .- f(x))./h[k], 1:N)              # forward difference
backwrd = map(k -> (f(x) .- f(x .- h[k]))./h[k], 1:N)              # backward difference 
central = map(k -> (f(x .+ h[k]) .- f(x .- h[k]))./(2*h[k]), 1:N)  # central difference
fourthd = map(k -> (-f(x .+ 2*h[k]) .+ 8*f(x .+ h[k]) .-           # fourth order difference
               8*f(x .- h[k]) .+ f(x .- 2*h[k]))./(12*h[k]), 1:N)

fig, ax = plt.subplots()
ax.loglog(h, abs.(forward .- g(x)), "r.--", label=raw"forward")
ax.loglog(h, abs.(backwrd .- g(x)), "r.--", label=raw"backwrd")
ax.loglog(h, abs.(central .- g(x)), "b.--", label=raw"central")
ax.loglog(h, abs.(fourthd .- g(x)), "k.--", label=raw"fourthd")
ax.set(xlabel=raw"grid size", ylabel=raw"error in derivative") 
ax.set_title(raw"Finite-difference convergence")
ax.grid(true); ax.legend()
plt.savefig("convergence.pdf")
