#!/usr/bin/env julia
# File: gausscheby1.jl
# Name: D.Saravanan
# Date: 08/03/2022

""" Script to calculate nodes and weights of Gauss-Chebyshev quadrature of the 1st kind """

using SciPy
using FastGaussQuadrature, LinearAlgebra

# exact value of the integral
f = x -> (x^4)/sqrt(1 - x^2)
exact = SciPy.integrate.quad(f, -1, 1)[1]

# nodes and weights calculations
x, w = gausschebyshev(10)

# integration
integral = w' * x.^4

# error calculation
error = abs(integral - exact)

println(exact, ' ', integral, ' ', error)
