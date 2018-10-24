import math

'''
 So.
 (3 + 6 + 9... + limit)
 or
 (5 + 10 + 15... + limit)
 
 is the same as:
 3 * (1 + 2 + 3... + floor(limit / 3)
 or
 5 * (1 + 2 + 3... + floor(limit / 5)

 Formula for calculating a finite arithmetic series is:
  0.5 * n * (a_1 + a_n)
  where:
  n = number of terms being added
  a_1 = first element in sequence
  a_n = last element in sequence

  n = floor(limit / multiple) = n_1

  x = n * (n + 1) * 0.5
'''
### Function to calculate finite arithmetic series
def arithSeries(n):
  return (n * (n + 1)) / 2


### Function to return sum of multiples of a given integer within range (1, limit)

def finiteArithmeticSeries(multiple, limit):
  return multiple * arithSeries(math.floor(limit / multiple))

## Inclusion-exclusion principle:
## multiples of least common multiples will
## be double counted
##
## In case of finding sums of multiples of
## 3 and 5, multiples of 15 will have to be
## subtracted

## Function to return sum of multiples of two numbers within ranges of (1, limit)
def sumOfMultiplesTwoNumbers(n1, n2, limit):
  return (finiteArithmeticSeries(n1, limit) + finiteArithmeticSeries(n2, limit) - finiteArithmeticSeries((n1 * n2), limit))


### Get input from user (2 numbers and a limit)
def sumOfMultiples():

  print("Enter 2 numbers and a limit. Program will return the sum of multiples of given numbers within range (1, limit)")
  
  n1 = int(input("Enter number 1: "))
  n2 = int(input("Enter number 2: "))
  limit = int(input("Enter limit: "))
  
  print(sumOfMultiplesTwoNumbers(n1, n2, limit))
  
  x = input("Enter 'y' to run again, all other commands will exit: \n" )
  if x.lower() == "y":
    sumOfMultiples()
  else:
    exit

sumOfMultiples()
