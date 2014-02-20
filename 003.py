# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# Answer:
# 6857

import math


def isPrime(n):
  print "  check if " + `n` + " is prime"
  # Altho sqrt calc is expensive, using n/2 is worse
  sqrtN = int(math.ceil(math.sqrt(n)))

  if (n == 2):
    return True

  if (n % 2 == 0):
    return False

  for i in range(3, sqrtN, 2):
    if (n % i == 0):
      return False

  return True


# ------------------------------------------------------------------------------
def largestPrimeFactor(n):
  # loop from 2 to n/2 (i)
  # if n % i == 0, then i is LPF, then set n to n/i
  i = 2
  lpf = 1
  nHalf = n/2

  while i < nHalf:
    # if i is a factor, it must be prime, since we've checked (and divided out)
    # all factors less than i
    if (n % i == 0):
      print `i` + " is a factor."
      # Check if the other divisor is a prime, it'd be the largest prime factor
      if (isPrime(n/i)):
        lpf = n/i
        break

      n = n / i
      lpf = i
    else:
      i += 1

  return lpf


# ------------------------------------------------------------------------------
def problem_003():

  lpf = largestPrimeFactor(600851475143)

  # `backtick` also works like repr(), when adding str to int
  print "Largest Prime Factor: " + str(lpf)


# ------------------------------------------------------------------------------
# Execute standalone
problem_003()

