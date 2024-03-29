#!/usr/bin/env julia
# File: eulermethod.jl
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to implement the Euler explicit & implicit scheme for y' = -0.5*y with y(0) = 1 """

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")
using LaTeXStrings

t_ = 25                 # time period
dt = 0.5                # time step
N = Int64(t_/dt)        # number of steps
t = zeros(N+1)          # time vector
y1 = ones(N+1)          # solution vector of euler explicit
y2 = ones(N+1)          # solution vector of euler implicit

for k in 1:N
    t[k+1] = t[k] + dt
    y1[k+1] = y1[k]*(1 - 0.5*dt)
    y2[k+1] = y2[k]/(1 + 0.5*dt)
end

exact = exp.(-0.5*t)     # exact solution

fig, ax = plt.subplots()
ax.plot(t, y1, "r.", label=raw"euler explicit")
ax.plot(t, y2, "b.", label=raw"euler implicit")
ax.plot(t, exact, "k-", label=raw"exact solution")
ax.set(xlim=(0, 25), xticks=0:5:25)
ax.set(ylim=(0, 1), yticks=0:0.2:1)
ax.tick_params(direction="in")
ax.set(xlabel=raw"t", ylabel=raw"y(t)")
ax.set_title(raw"Euler explicit \& implicit scheme")
ax.grid(true); ax.legend()
plt.savefig("eulermethod.png")
