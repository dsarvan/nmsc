#!/usr/bin/env julia
# File: quadrature.jl
# Name: D.Saravanan
# Date: 20/09/2021

""" Program to implement the different quadrature and see how the error behaves """

a, b = 0, 1

# function to be integrated
f = x -> exp(-x^2)

# derivative of the function
g = x -> -2*x*exp(-x^2)
