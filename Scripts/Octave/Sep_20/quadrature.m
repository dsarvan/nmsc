#!/usr/bin/env octave
# File: program.m
# Name: D.Saravanan
# Date: 20/09/2021

""" Script to implement the different quadrature and see how the error behaves """

# end points of interval
a = 0; b = 1;

# function to be integrated
f = @(x) exp(-x.^2);

# derivative of the function
g = @(x) -2*x*exp(-x.^2);

# exact value of the integral
exact = 0.746824132812427025399;

# number of different set of grids
Ngrids = 10;

h = zeros(Ngrids,1);        # different grid spacings

rect = zeros(Ngrids,1);     # rectangular rule
trap = zeros(Ngrids,1);     # trapezoidal rule
simp = zeros(Ngrids,1);     # simpson rule
rend = zeros(Ngrids,1);     # rectangular rule with end-point correction
tend = zeros(Ngrids,1);     # trapezoidal rule with end-point correction

for k = 1:Ngrids
    N = 10*2^(k+1);                 # number of grid points
    h(k) = (b - a)/(N - 1);         # grid spacing
    x = linspace(a, b, N);          # grid points
    y = 0.5*(x(1:N-1) + x(2:N));    # mid-points of each panel

    rect(k) = h(k)*sum(f(y));                       # rectangular rule
    trap(k) = h(k)*(sum(f(x)) - (f(a) + f(b))/2);   # trapezoidal rule
    simp(k) = (2*rect(k) + trap(k))/3;              # simpson rule
    rend(k) = rect(k) + h(k)^2 / 24*(g(b) - g(a));  # rectangular rule with end-point correction
    tend(k) = trap(k) - h(k)^2 / 12*(g(b) - g(a));  # trapezoidal rule with end-point correction
end

# error calculations
rect_err = abs(double(rect - exact));
trap_err = abs(double(trap - exact));
simp_err = abs(double(simp - exact));
rend_err = abs(double(rend - exact));
tend_err = abs(double(tend - exact));

figure;  loglog(h, rect_err, 'r+--');
hold on; loglog(h, trap_err, 'b+--');
hold on; loglog(h, simp_err, 'k+--');
hold on; loglog(h, rend_err, 'r*--');
hold on; loglog(h, tend_err, 'b*--');
xlabel('grid size'); ylabel('error in quadrature');
legend('rectangular', 'trapezoidal', 'simpsonrule', 'rectendpont', 'trapendpont');
set(legend, 'location', 'northwest');
set(gca, 'title', text('string', 'Quadrature convergence'));
grid on; print('quadrature.pdf', '-dpdf')
