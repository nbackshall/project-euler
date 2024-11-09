package main

import "fmt"

func sumOfSquares(n int) int {
  sum := 0
  for i := 1; i <= n; i++ {
    sum += i * i
  }
  return sum
}

func squareOfSum(n int) int {
  sum := 0
  for i := 1; i <= n; i++ {
    sum += i
  }
  return sum * sum
}

func main() {
  const n = 100
  difference := squareOfSum(n) - sumOfSquares(n)
  fmt.Printf("Difference: %d\n", difference)
}

