#!/usr/bin/env octave
% File: guasselm.m
% Name: D.Saravanan
% Date: 18/08/2021
% Script of gaussian elimination algorithm for solving systems of linear equations

% A is a matrix  and b is a vector
% A is a square matrix and inv(A) exists

function x = gaussian(A, b)

    n = length(b);

    % forward elimination phase
    for i = 1:n-1

        for j = i+1:n

            A(j, i+1:end) = A(j, i+1:end) - A(j, i)/A(i, i) * A(i, i+1:end);

            b(j) = b(j) - A(j, i)/A(i, i) * b(i);

        end

        A(i+1:end, 1) = 0;

    end

    % backward substitution phase
    for i = n:-1:1
        b(i) = (b(i) - A(i, i+1:end) * b(i+1:end))/A(i,i);
    end

    x = b;

endfunction
