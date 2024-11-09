package main

import "fmt"

func isPrime(n int) bool {
  if n < 2 {
    return false
  }
  if n == 2 {
    return true
  }
  if n % 2 == 0 {
    return false
  }
  for i := 3; i < n / 2; i += 2 {
    if n % i == 0 {
      return false
    }
  }
  return true
}

func getPrimes(n int) []int {
  if n < 1 {
    return []int{}
  } else if n == 1 {
    return []int{2}
  }

  primes := []int{2}
  curr := 3

  for len(primes) < n {
    if isPrime(curr) {
      primes = append(primes, curr)
    }
    curr += 2
  }

  return primes
}

func main() {
  const n = 10001
  primes := getPrimes(n)
  fmt.Printf("The %d prime number is %d.\n", n, primes[len(primes)-1])
}
