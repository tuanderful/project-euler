# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


# Answer:
# 6857

def isPrime(n):
  nHalf = n / 2   # is this accurate?

  print "Is " + `n` + " a prime number??"

  if (n == 2):
    return True

  if (n % 2 == 0):
    #print "No, its even."
    return False

  for i in range(3, nHalf, 2):
    if (n % i == 0):
      return False

  return True

def largestPrimeFactor(n):
  # loop from 2 to n/2 (i)
  # if n % i == 0, then i is LPF, then set n to n/i
  i = 2
  lpf = 1

  while i < n/2:
    if (n % i == 0):
      n = n / i
      lpf = i
    else:
      i += 1
  return lpf



# ------------------------------------------------------------------------------
def problem_003():

  #lpf = largestPrimeFactor(13195)

  # `backtick` also works like repr(), when adding str to int
  #print "Largest Prime Factor: " + str(lpf)

  for i in range(1, 20):
    if (isPrime(i)):
      print i


# ------------------------------------------------------------------------------
# Execute standalone
problem_003()