#!/usr/bin/env julia
# File: eulerexplicit.jl
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to implement the Euler explicit scheme for y' = -10y with y(0) = 1 """

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")
using LaTeXStrings

t_ = 10                 # time period
dt = 0.02               # time step
N = Int64(t_/dt)        # number of steps
t = zeros(N)            # time vector
y = zeros(N)            # solution vector of euler explicit
t[1] = 0
y[1] = 1

for k in 1:N-1
    t[k+1] = t[k] + dt
    y[k+1] = y[k] + dt * (-10*y[k])
end

exact = exp.(-10*t)      # exact solution

fig, ax = plt.subplots()
ax.plot(t, y, "r.", label=raw"euler explicit")
ax.plot(t, exact, "k-", label=raw"exact solution")
ax.set(xlim=(0, 10), xticks=0:2:10)
ax.set(ylim=(0, 1), yticks=0:0.2:1)
ax.tick_params(direction="in")
ax.set(xlabel=raw"t", ylabel=raw"y(t)")
ax.set_title(raw"Euler explicit scheme")
ax.grid(true); ax.legend()
plt.savefig("eulerexplicit.png")
