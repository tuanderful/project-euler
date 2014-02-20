# Summation of primes
# Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# Answer:
# 142913828922

# Note: dict is faster than array for the sieve algorithm


# return an array of all prime numbers up to m
def sieve(m):
  SIEVE = {}
  PRIMES = []
  i = 2

  while i < m:
    # i is multiple of an earlier prime;
    if i in SIEVE:
      i += 1
      
    # i has not been marked false, must be Prime
    else:
      # Technically, we dont even need to update the sieve for True values
      #SIEVE[i] = True
      PRIMES.append(i)

      for j in range(2*i, m, i):
        SIEVE[j] = False
      i += 1

  return PRIMES


# ------------------------------------------------------------------------------
def problem_010():
  print sum(sieve(2000000))


# ------------------------------------------------------------------------------
# Execute standalone
problem_010()


