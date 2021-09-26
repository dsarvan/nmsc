// File: polynomial.go
// Name: D.Saravanan
// Date: 27/08/2021
// Program to construct the polynomial interpolation
// using Lagrange polynomial

package main

import (
    "fmt"
    "math"
    "gonum"
)

func interpolate(fnodes, xnodes [9]float64, x [1000]float64) [1000]float64 {

    var res [len(x)]float64

    for i := 0; i <= len(xnodes); i++ {
        res = res + fnodes[i] * lagrange(xnodes, x, i)
    }

    return res
}

func lagrange(xnodes [9]float64, x [1000]float64, i int)  [1000]float64 {

    var val [len(x)]float64

    for j := 0; j <= len(xnodes); j++ {
        
        if (i == j) {
            continue
        }

        val = val * (x - xnodes[j]) / (xnodes[i] - xnodes[j])
    }

    return val
}

func main() {

    const N = 9

    var xnodes [N]float64 
    var fnodes [N]float64
    var x [1000]float64 
    var f [1000]float64 
    var fintp [1000]float64
    
    var c = 0

    var n flaot64

    for n = -1; n <= 1; n += 0.25 {
        xnodes[c] = n
        fnodes[c] = math.Sin(math.Pi * xnodes[c])
        c += 1
    }

    for n = -1; n <= 1; n += 0.002002 {
        x[c] = n
        f[c] = math.Sin(math.Pi * x[c])
        c += 1
    }

    fintp = interpolate(fnodes, xnodes, x)

    error := math.Max(math.Abs(f - fintp)/math.Abs(f))
    fmt.Printf("%f\n", error)

}
