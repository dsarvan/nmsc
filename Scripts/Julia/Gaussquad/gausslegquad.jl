#!/usr/bin/env julia
# File: gausslegquad.jl
# Name: D.Saravanan
# Date: 08/03/2022

""" Script to evaluate integral exp(-x^2) from -1 to +1 """

using SciPy
using FastGaussQuadrature, LinearAlgebra

# exact value of the integral
f = x -> exp(-x^2)
exact = SciPy.integrate.quad(f, -1, 1)[1]

n = []

for k in [2, 5, 10, 20, 50, 100]

    n.append(k)
    
    # nodes and weights calculations
    x, w = gausslegendre(k)

    # integration
    integral = (w' * f.(x))

    # error calculation
    error = abs(integral - exact)
