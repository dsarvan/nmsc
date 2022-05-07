#!/usr/bin/env julia
# File: eulerscheme.jl
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to implement the Euler explicit, implicit and Trapezoidal scheme for y' = -0.5*y with y(0) = 1 """

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
N = int(t_/dt)          # number of steps
t = zeros(N)            # time vector
y1 = zeros(N)           # solution vector of euler explicit
y2 = zeros(N)           # solution vector of euler implicit
y4 = zeros(N)           # solution vector of trapezoidal rule

for k in 1:N
    t[k+1] = t[k] + dt
    y1[k+1] = y1[k]*(1 - 0.5*dt)
    y2[k+1] = y2[k]/(1 + 0.5*dt)
    y3[k+1] = y3[k]*(1 - 0.5*dt/2)/(1 + 0.5*dt/2)
end

exact = exp(-0.5*t)     # exact solution

fig, ax = plt.subplots()
ax.plot(t, y1, "r.", label=raw"euler explicit")
ax.plot(t, y2, "b.", label=raw"euler implicit")
ax.plot(t, y3, "g.", label=raw"trapezoidal rule")
ax.plot(t, exact, "k-", label=raw"exact solution")
ax.set(xlabel=raw"t", ylabel=raw"y(t)")
ax.set_title(raw"Euler explicit, implicit \& Trapezoidal scheme")
ax.grid(true); ax.legend()
plt.savefig("eulerscheme.pdf")
