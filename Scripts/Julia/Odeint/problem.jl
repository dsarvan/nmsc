#!/usr/bin/env julia
# File: problem.jl
# Name: D.Saravanan
# Date: 24/03/2022

""" Script to solve the differential equation """

using DifferentialEquations
using Plots

f(y, p, t) = -0.5y

# initial condition
y0 = 1

# time points
t = (0, 25)

# solve ODE
y = ODEProblem(f, y0, t)

plot(solve(y), linewidth=2,
     title="Solution to the linear ODE",
     xaxis="Time (t)", yaxis="y(t)",
     label="dy/dt = - 0.5 * y")

savefig("problem.png")
