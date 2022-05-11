!#/usr/bin/env julia
# File: eulerexplicit.jl
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
N = int(t_/dt)          # number of steps
t = zeros(N)            # time vector
y = zeros(N)           # solution vector of euler explicit

for k in 1:N
    t[k+1] = t[k] + dt
    y[k+1] = y[k]*(1 - 0.5*dt)
end

exact = exp(-0.5*t)     # exact solution

fig, ax = plt.subplots()
ax.plot(t, y, "r.", label=raw"euler explicit")
ax.plot(t, exact, "k-", label=raw"exact solution")
ax.set(xlabel=raw"t", ylabel=raw"y(t)")
ax.set_title(raw"Euler explicit scheme")
ax.grid(true); ax.legend()
plt.savefig("eulerexplicit.pdf")
