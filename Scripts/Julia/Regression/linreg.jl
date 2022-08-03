#!/usr/bin/env julia
# File: linreg.jl
# Name: D.Saravanan
# Date: 16/11/2020 

""" Script to implement linear regression """

using Statistics

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")
using LaTeXStrings

function slope(x, y, n)
    """ estimating the slope """
    sum((x .- mean(x)) .* (y .- mean(y))) / sum((x .- mean(x)).^2)
end

function intercept(x, y, m)
    """ estimating the intercept """
    mean(y) .- m * mean(x)
end

height = [151, 174, 138, 186, 128, 136, 179, 163, 152, 131]
weight = [63, 81, 56, 91, 47, 57, 76, 72, 62, 48]

n = length(height)
m = slope(height, weight, n)
c = intercept(height, weight, m)

# predicted weight with values m and c
predicted_y = [m*x + c for x in height]
residuals = [x1 .- x2 for (x1, x2) in zip(predicted_y, weight)]
println(sum(residuals))

function rmse(p, y, n)
    """ error estimation (Root Mean Squared Error) """
    sqrt(sum((p .- y).^2)/n)
end

err = rmse(predicted_y, weight, n)
println(err)

fig, ax = plt.subplots()
ax.plot(height, weight, "b.", label="data points")
ax.plot(height, predicted_y, "r", label="predicted data")
ax.set(xlabel="height", ylabel="weight")
ax.set_title("Linear regression")
ax.grid(true); ax.legend()
plt.savefig("linreg.png")
