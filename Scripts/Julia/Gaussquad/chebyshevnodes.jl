#!/usr/bin/env julia
# File: chebyshevnodes.jl
# Name: D.Saravanan
# Date: 08/03/2022

""" Script to compute the nodes and weights of the Chebyshev polynomial of the first kind of degree n """

using SciPy
using FastGaussQuadrature, LinearAlgebra
    
println("degree: ")
n = readline()
n = parse(Int64, n) 

println("lower limit: ")
a = readline()
a = parse(Int64, a)

println("upper limit: ")
b = readline()
b = parse(Int64, b)

x = zeros(n+1)
w = zeros(n+1)

xn, wn = gausschebyshev(n)
println("nodes computed: ", xn)
println("weights: ", wn) 

for k in 1:n
    x[k] = 0.5*(b - a) * cos(((2*k-1)/(2*n))*pi) + 0.5*(b + a)
    w[k] = pi/(n)
    println(k, x[k])
    println(k, w[k])