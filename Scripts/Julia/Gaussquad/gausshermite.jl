#!/usr/bin/env julia
# File: gausshermite.jl
# Name: D.Saravanan
# Date: 08/03/2022

""" Script to calculate nodes and weights of Gauss-Hermite quadrature """

using SciPy
using FastGaussQuadrature, LinearAlgebra

# exact value of the integral
f = x -> x^4 * exp(-x^2)
exact = SciPy.integrate.quad(f, -Inf, Inf)[1]

# nodes and weights calculations
x, w = gausshermite(10)

# integration
integral = w' * x.^4

# error calculation
error = abs(integral - exact)

println(exact, ' ', integral, ' ', error)
