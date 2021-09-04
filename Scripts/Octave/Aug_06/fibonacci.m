#!/usr/bin/env octave
% File: fibonacci.m
% Name: D.Saravanan
% Date: 06/08/2021
% Script that returns fibonacci number for a given n

function f = fibonacci(n)
    % returns fibonacci number:
    % fibonacci(3) = 2

    if (n == 1) || (n == 2)
        f = 1;
    else
        f = fibonacci(n-1) + fibonacci(n-2);
    end
endfunction
