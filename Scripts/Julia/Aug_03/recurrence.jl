#!/usr/bin/env julia
# File: recurrence.jl
# Name: D.Saravanan
# Date: 03/08/2021

""" Script for solving recurrence relation:
a(n+1) = 10 a(n) - 9 a(n-1), a(0) = 2.95, a(1) = 2.95 """

N = 20
a = zeros(N)
a[1] = 2.95
a[2] = 2.95

for n in 2:N-1
    a[n+1] = 10*a[n] - 9*a[n-1]
end

println(a)
