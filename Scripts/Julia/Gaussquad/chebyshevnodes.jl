#!/usr/bin/env julia
# File: chebyshevnodes.jl
# Name: D.Saravanan
# Date: 08/03/2022

""" Script to compute the nodes and weights of the Chebyshev polynomial of the first kind of degree n """

using SciPy
using FastGaussQuadrature, LinearAlgebra

for k in 1:n
    x[k] = 0.5*(b - a) * cos(((2*k-1)/(2*n))*pi) + 0.5*(b + a)
    w[k] = pi/(n)
    println(k, x[k])
    println(k, w[k])
