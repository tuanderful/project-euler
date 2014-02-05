# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


# Answer:
# 104743


import math


def isPrime(n):
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
def problem_007():
  return 0

# ------------------------------------------------------------------------------
# Execute standalone
problem_007()