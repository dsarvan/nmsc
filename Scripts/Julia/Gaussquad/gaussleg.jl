#!/usr/bin/env julia
# File: gaussleg.jl
# Name: D.Saravanan
# Date: 08/03/2022

""" Script to calculate nodes and weights of Gauss-Legendre quadrature """

using SciPy
using FastGaussQuadrature, LinearAlgebra

# exact value of the integral
f = x -> sin(x^2)
exact = SciPy.integrate.quad(f, -1, 1)[1]

# nodes and weights calculations
x, w = gausslegendre(10)

# integration
integral = (w' * f.(x)) 

# error calculation
error = abs(integral - exact)

println(exact, ' ', integral, ' ', error)
