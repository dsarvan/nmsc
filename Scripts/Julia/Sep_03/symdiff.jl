#!/usr/bin/env julia
# File: symdiff.jl
# Name: D.Saravanan
# Date: 01/10/2021

""" Symbolic differentiation in Julia """

using SymEngine

@vars x
f = x^2 + x/2 - sin(x)/x
println(diff(f,x))
