#!/usr/bin/env julia
# File: quadrature.jl
# Name: D.Saravanan
# Date: 20/09/2021

""" Program to implement the different quadrature and see how the error behaves """

import PyPlot
const plt = PyPlot
plt.rc("pgf", texsystem="pdflatex")
plt.rc("font", family="serif", weight="normal", size=8)
plt.rc("axes", labelsize=10, titlesize=10)
plt.rc("figure", titlesize=10)
plt.rc("text", usetex="True")
using LaTeXStrings

# end points of interval
a, b = 0, 1

# function to be integrated
f = x -> exp.(-x.^2)

# derivative of the function
g = x -> -2*x*exp.(-x.^2)

# exact value of the integral
exact = 0.746824132812427025399

# number of different set of grids
Ngrids = 10

h = zeros(Ngrids)       # different grid spacings

rect = zeros(Ngrids)    # rectangular rule
trap = zeros(Ngrids)    # trapezoidal rule
simp = zeros(Ngrids)    # simpson rule
rend = zeros(Ngrids)    # rectangular rule with end-point correction
tend = zeros(Ngrids)    # trapezoidal rule with end-point correction

for k in 1:Ngrids
    N = 10*2^(k+1)              # number of grid points
    h[k] = (b - a)/(N - 1)      # grid spacing
    x = LinRange(a,b,N)         # grid points
    y = 0.5*(x[1:N-1] + x[2:N]) # mid-points of each panel

    rect[k] = h[k]*sum(f(y))                        # rectangular rule
    trap[k] = h[k]*(sum(f(x)) - (f(a) + f(b))/2)    # trapezoidal rule
    simp[k] = (2*rect[k] + trap[k])/3               # simpson rule
    rend[k] = rect[k] + h[k]^2 / 24*(g(b) - g(a))   # rectangular rule with end-point correction
    tend[k] = trap[k] - h[k]^2 / 12*(g(b) - g(a))   # trapezoidal rule with end-point correction
end

# error calculations
rect_err = abs.(Float64.(rect .- exact))    # error in rectangular rule
trap_err = abs.(Float64.(trap .- exact))    # error in trapezoidal rule
simp_err = abs.(Float64.(simp .- exact))    # error in simpson rule
rend_err = abs.(Float64.(rend .- exact))    # error in rectangular rule with end-point correction
tend_err = abs.(Float64.(tend .- exact))    # error in trapezoidal rule with end-point correction

fig, ax = plt.subplots()
ax.loglog(h, rect_err, "r.--", label=raw"rectangular")
ax.loglog(h, trap_err, "b.--", label=raw"trapezoidal")
ax.loglog(h, simp_err, "k.--", label=raw"simpsonrule")
ax.loglog(h, rend_err, "r+--", label=raw"rectendpont")
ax.loglog(h, tend_err, "b+--", label=raw"trapendpont")
ax.set(xlabel=raw"grid size", ylabel=raw"error in quadrature")
ax.set_title(raw"Quadrature convergence")
ax.grid(true); ax.legend()
plt.savefig("quadrature.pdf")
