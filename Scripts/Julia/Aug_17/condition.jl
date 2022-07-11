#!/usr/bin/env julia
# File: condition.jl
# Name: D.Saravanan
# Date: 17/08/2021

""" Script to compute condition number of a matrix """

using LinearAlgebra

N = 20

eye(n) = 1.0*Matrix(I,n,n)
A = eye(N) - 10 * diagm(ones(N)) + 9 * diagm(ones(N))
