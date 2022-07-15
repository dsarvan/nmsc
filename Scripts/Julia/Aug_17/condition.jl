#!/usr/bin/env julia
# File: condition.jl
# Name: D.Saravanan
# Date: 17/08/2021

""" Script to compute condition number of a matrix """

using LinearAlgebra

N = 20

eye(n) = 1.0*Matrix(I,n,n)
A = eye(N) - 10 * diagm(-1 => fill(1, N-1)) + 9 * diagm(-2 => fill(1, N-2))
A[2,1] = 0

cond_A = cond(A)

println("Condition number of matrix A: $cond_A")

B = eye(N) - 1 * diagm(-1 => fill(1, N-1)) - 1 * diagm(-2 => fill(1, N-2))
B[2,1] = 0

cond_B = cond(B)

println("Condition number of matrix B: $cond_B")
