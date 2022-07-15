#!/usr/bin/env julia
# File: condition.jl
# Name: D.Saravanan
# Date: 17/08/2021

""" Script to compute condition number of a matrix """

using LinearAlgebra

N = 5

eye(n) = 1.0*Matrix(I,n,n)
#A = eye(N) - 10 * diagm(ones(N-1)) + 9 * diagm(ones(N-2))
#A = eye(N) - 10 * diagm(ones(N), 1)
A = diagm(ones(N-1))

println(A)
