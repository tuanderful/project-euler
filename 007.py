# 10001st prime
# Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.

# What is the 10 001st prime number?

# Answer:
# 104743

# Time: 10.2s  with enumerate
#        8.2s  without enumerate
#        4.0s  without print statements
#        4.2s  cut upper bound of checks in half
#        2.4s  cut upper bound of checks in half (bitwise shift)
#        0.2s  use sqrt(n) as upper-bound for checks
#              incrememt by 2 (check only odd numbers duh)


import math

PRIMES_MEMO = [2, 3]


# ------------------------------------------------------------------------------
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


# Check if n is prime by seeing if it is divisible by any known primes.
# Assumes that ALL primes less than n have been found.
def isPrime_2(n):
  sqrtN  = math.sqrt(n);
  for p in PRIMES_MEMO:
    if (n % p == 0):
      return False
    # possible performance optimization
    if (p > sqrtN):
      break


  # If n is not divisble by any primes less than itself, then add n to PRIMES
  PRIMES_MEMO.append(n)
  return True


# ------------------------------------------------------------------------------
def problem_007():

  # Cannot start at 1
  i = 5
  while len(PRIMES_MEMO) < 10001:
    # Check if its a prime, add it to memo if it is
    isPrime_2(i)
    i += 2

  print PRIMES_MEMO[10000]


# ------------------------------------------------------------------------------
# Execute standalone
problem_007()

