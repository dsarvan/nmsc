#!/usr/bin/env julia
# File: eulerscheme.jl
# Name: D.Saravanan
# Date: 02/12/2021

""" Script to implement the Euler explicit, implicit and Trapezoidal scheme for y' = -0.5*y with y(0) = 1 """

t_ = 25                 # time period
dt = 0.5                # time step
N = int(t_/dt)          # number of steps
t = zeros(N)            # time vector
y1 = zeros(N)           # solution vector of euler explicit
y2 = zeros(N)           # solution vector of euler implicit
y4 = zeros(N)           # solution vector of trapezoidal rule
