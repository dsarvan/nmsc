#!/usr/bin/env julia
# File: problem.jl
# Name: D.Saravanan
# Date: 24/03/2022

""" Script to solve the differential equation with ODEProblem """

using DifferentialEquations
using Plots

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")
using LaTeXStrings

f(y, p, t) = -0.5*y

# initial condition
y0 = 1

# time points
t = (0, 25)

# solve ODE
y = ODEProblem(f, y0, t)

# exact solution
exact = exp.(-0.5*(0:0.5:25))

#plot(solve(y), linewidth=2,
#     title="Solution to the linear ODE",
#     xaxis="Time (t)", yaxis="y(t)",
#     label="dy/dt = - 0.5 * y")
#
#plot!(solve(y).t, t -> exp(-0.5*t), 
#      ls=:dash, label="Exact solution")
#
#savefig("problem.png")

fig, ax = plt.subplots()
ax.plot(solve(y), "r--", label=L"$\displaystyle \frac{dy}{dt} = - 0.5 * y$")
ax.plot(0:0.5:25, exact, "k.", label=raw"exact solution")
ax.set(xlabel=raw"t", ylabel=raw"y(t)")
ax.set_title(raw"Solution to the linear ODE")
ax.grid(true); ax.legend()
plt.savefig("problem.png")
