package main

import (
  "fmt"
  "os"
  "path/filepath"
  "runtime"
  "strings"
  "strconv"
)

func getFilePath(filename string) (string, error) {
  _, scriptPath, _, ok := runtime.Caller(0)
  if !ok {
    return "", fmt.Errorf("failed to get script path")
  }
  return filepath.Join(filepath.Dir(scriptPath), filename), nil
}

func getNumbers(filename string) (string, error) {
  filePath, err := getFilePath(filename)
  if err != nil {
    return "", err
  }

  content, err := os.ReadFile(filePath)
  if err != nil {
    return "", err
  }

  numbers := strings.ReplaceAll(string(content), "\n", "")
  numbers = strings.ReplaceAll(numbers, " ", "")
  return numbers, nil
}

func multiplyDigitString(digits string) (int, []int, error) {
  mult := 1
  numbers := make([]int, len(digits))

  for i, char := range digits {
    num, err := strconv.Atoi(string(char))
    if err != nil {
      return 0, nil, fmt.Errorf("invalid digit at position %d: %c", i, char)
    }
    numbers[i] = num
    mult *= num
  }
  
  return mult, numbers, nil
}

func main() {
  numbersString, err := getNumbers("numbers.txt")
  if err != nil {
    fmt.Printf("Error getting numbers: %v\n:", err)
  }
  fmt.Printf("Numbers: %s\n", numbersString)

  const sequenceLength = 13

  largestMult := 0
  largestSequence := make([]int, sequenceLength)

  start := 0
  end := sequenceLength - 1

  for end < len(numbersString) {
    mult, numbers, err := multiplyDigitString(numbersString[start:end+1])
    if err != nil {
      fmt.Errorf("Error summing digits in string: %s", err)
      return
    }

    if mult > largestMult {
      largestMult = mult
      largestSequence = numbers
    }

    start += 1
    end += 1
  }

  fmt.Printf("Largest sequence: %v\n", largestSequence)
  fmt.Printf("Largest multiple: %d\n", largestMult)
}
