#!/usr/bin/env julia
# File: chebyshevnodes.jl
# Name: D.Saravanan
# Date: 08/03/2022

""" Script to compute the nodes and weights of the Chebyshev polynomial of the first kind of degree n """

using SciPy
using FastGaussQuadrature, LinearAlgebra
    
print("degree: ")
n = parse(Int64, readline()) 

print("lower limit: ")
a = parse(Int64, readline())

print("upper limit: ")
b = parse(Int64, readline())

x = zeros(n+1)
w = zeros(n+1)

xn, wn = gausschebyshev(n)
println("nodes computed: $xn\n")
println("weights: $wn\n") 

for k in 1:n
    x[k] = 0.5*(b - a) * cos(((2*k-1)/(2*n))*pi) + 0.5*(b + a)
    w[k] = pi/(n)
    println("x[$k] =  ", x[k])
    println("w[$k] =  ", w[k])
end
