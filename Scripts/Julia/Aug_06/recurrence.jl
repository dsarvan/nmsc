#!/usr/bin/env julia
# File: recurrence.jl
# Name: D.Saravanan
# Date: 06/08/2021

""" Script for fibonacci recurrence series """

function fibonacci(n)
    """
    returns fibonacci number:
        fibonacci(3) = 2
    """

    f = zeros(n)
    f[1], f[2] = 1, 1

    for i in 2:n-1
        f[i+1] = f[i] + f[i-1]
    end
    
    return f[n]
end

N = 20

# exact values
e = zeros(N)
e[1] = 2.95
e[2] = 2.95

# values
a = zeros(N)
a[1] = 2.95
a[2] = 2.95

# relative error terms
err = zeros(N)

for n in 2:N-1
    a[n+1] = a[n] + a[n-1]
    e[n+1] = 2.95 * fibonacci(n+1)
end

for n in 1:N
    err[n] = abs((a[n]-e[n])/(e[n]))
end

# print relative error terms
println(err)
