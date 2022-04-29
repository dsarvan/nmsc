#!/usr/bin/env julia
# File: gausslag.jl
# Name: D.Saravanan
# Date: 08/03/2022

""" Script to calculate nodes and weights of Gauss-Laguerre quadrature """

using SciPy
using FastGaussQuadrature, LinearAlgebra

# exact value of the integral
f = x -> exp(-x)*sin(x^2)
exact = SciPy.integrate.quad(f, 0, Inf)[1]

# nodes and weights calculations
x, w = gausslaguerre(140)

# integration
integral = w' * sin.(x.^2) 

# error calculation
error = abs(integral - exact)

println(exact, ' ', integral, ' ', error)
