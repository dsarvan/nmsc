#!/usr/bin/env julia
# File: problem.jl
# Name: D.Saravanan
# Date: 24/03/2022

""" Script to solve the differential equation """

using DifferentialEquations

f(y, p, t) = -0.5y

# initial condition
y0 = 1

# time points
t = (0, 25)

# solve ODE
y = ODEProblem(f, y0, t)
