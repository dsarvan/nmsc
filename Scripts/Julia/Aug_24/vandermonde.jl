#!/usr/bin/env julia
# File: vandermonde.jl
# Name: D.Saravanan
# Date: 24/08/2021

""" Script to compute the condition number of Vandermonde matrix """

for (i, N) in enumerate(range(5,35,10))
    x = range(-1, 1, Int32(N))
    V = vander(x)
end
