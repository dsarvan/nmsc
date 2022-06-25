#!/usr/bin/env julia
# File: problem.jl
# Name: D.Saravanan
# Date: 24/03/2022

""" Script to solve the differential equation """

using DifferrentialEquations

function f(y, t)
    return -0.5*y
end

# initial condition
y0 = 1

# time points
t = (0, 25)

# solve ODE
y = ODEProblem(f, y0, t)

# exact solution
exact = exp(-0.5*t)
