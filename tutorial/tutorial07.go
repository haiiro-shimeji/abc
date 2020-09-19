// tutorial07
// https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_c
//
package main

import (
	"fmt"
	"math"
	"os"
)

func readString() string {
	var s string
	fmt.Fscan(os.Stdin, &s)
	return s
}

func readInteger() int {
	var i int
	fmt.Fscan(os.Stdin, &i)
	return i
}

func readStringSet(n int) []string {
	s := make([]string, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(os.Stdin, &s[i])
	}
	return s
}

func readIntegerSet(n int) []int {
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(os.Stdin, &a[i])
	}
	return a
}

func readIntegerMatrix(n int, m int) [][]int {
	a := make([][]int, n)
	for i := 0; i < n; i++ {
		a[i] = make([]int, m)
		for j := 0; j < m; j++ {
			fmt.Fscan(os.Stdin, &a[i][j])
		}
	}
	return a
}

func createModel(M [][]int) [][]int {
	return [][]int{}
}

func inModel(model [][]int, p []float64) bool {
	return true
}

func process(N int, M [][]int) int {
	model := createModel(M)

	bestScore := 0.0

	for i := 0; i < N; i++ {
		for j := i + 1; j < N; j++ {
			score := math.Pow(float64(M[i][0]-M[j][0]), 2.0) +
				math.Pow(float64(M[i][1]-M[j][1]), 2.0)

			if bestScore >= score {
				continue
			}

			p0 := []float64{float64(M[i][0]), float64(M[i][1])}
			p1 := []float64{float64(M[j][0]), float64(M[j][1])}
			p2 := []float64{p1[0] - p0[1] + p1[1], p1[1] + p0[0] - p1[0]}
			p3 := []float64{p2[0] - p1[1] + p2[1], p2[1] + p1[0] - p2[0]}

			if 0 <= p2[0] && 5000 >= p2[0] && inModel(model, p2) &&
				0 <= p3[0] && 5000 >= p3[0] && inModel(model, p3) {
				bestScore = score
			}
		}
	}

	return int(bestScore)
}

func main() {
	_N := readInteger()
	_M := readIntegerMatrix(_N, 3)

	fmt.Fprintln(os.Stdout, process(_N, _M))
}
