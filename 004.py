# Largest palindrome product
# Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# Answer:
# 906609

# ___3 Approaches_________________________
# 0. i from 999 to 100, j from 999 to 100. Multiply i*j, find a palindrome.
#    This has 800k pairs (900^2).
# 1. Find largest palindromes (iterate 999 down, generate palindrome), then
#    check if you can find two 3-digit divisors with different combinations of
#    their prime factors.
#    This has 900 candidates to check, but I haven't gotten around to determining
#    the complexity of vetting each palindrome.
# 2. i from 999 to 100, j from 999 to i. The second iterator doesn't need to go
#    past i; unnecessarily low calculations. This has 500k pairs (triangle(999))


# ==============================================================================
# Approach 1: Start from a palindrome, determine factors

# 1. Generate all the prime factors ----------------------------------------
def getPrimeFactors(n):
  # loop from 2 to n/2 (i)
  # if n % i == 0, then set n to n/i
  i = 2
  factors = []

  while i <= n:
    # if i is a factor, it must be prime, since we've checked (and divided out) all factors less than i
    if (n % i == 0):
      n = n / i
      factors.append(i)
    else:
      # Can we optimize this by incrementing by 2?
      i += 1

  print factors

  return factors


# 2. Find largest factor ---------------------------------------------------
# - We simply cannot multiply from the bottom up: 
#   3 * 3 * 5 * 7 * 37 would incorrectly yield 315 * 37, but 
# - We look for the largest first: look at last factor, multiple against the
#   head of the array until it exceeds 100. Then fold the remaining prime 
#   factors but this is also faulty logic, since the remaining prime factors 
#   can exceed 3 digits
# - Go through the permutations of factors. For each permutation, slide a pivot
#   and reduce left/right to find two factors. Check if they're both three digits
def _twoLargeThreeDigitFactors(factors):
  x = 1
  y = 1

  # x = factors.pop()

  # while (x < 100):
  #   x *= factors.pop(0)

  # # reduce(function, iterable [, initializer])
  # # here, function is:
  # #   lambda x, y: x * y
  # # iterable is factors
  # y = reduce(lambda x, y: x*y, factors)

  return [x, y]


# --------------------------------------------------------------------------
def approach_1():

# 100, 1000
  for i in reversed(range(900,1000)):
    # This is extended slice syntax. It works by doing [begin:end:step]
    # by leaving begin and end off and specifying a step of -1, it reverses a string.
    palindrome = `i` + `i`[::-1]

    print palindrome
    largeFactors = _twoLargeThreeDigitFactors(getPrimeFactors(int(palindrome)));

    if(largeFactors[0] > 100 and largeFactors[0] < 1000 and largeFactors[1] > 100 and largeFactors[1] < 1000):
      print `palindrome` + " has prime factors of " + `largeFactors[0]` + " and " + `largeFactors[1]`
      break



# ==============================================================================
# Approach 2: Multiply two three-digit numbers and determine if its a palindrome

def isPalindrome(n):
  return str(n) == str(n)[::-1]


def approach_2():
  validPalindromes = []

  # 100, 1000 - start at 999 and iterate down
  for i in reversed(range(100,1000)):

    #multiply i by all numbers larger than i
    for j in reversed(range(i, 1000)):
      c = i * j

      if (isPalindrome(c)):
        print `c` + ": " + `i` + " * " + `j`
        validPalindromes.append(c)
        break  # only breaks out of the inner loop
               # since we are iterating j down, looping further would only yield smaller products

  # sorts, smallest to large
  validPalindromes.sort()

  # print the largest one
  print validPalindromes.pop()


# ==============================================================================
def problem_004():

  approach_2()


# ------------------------------------------------------------------------------
# Execute standalone
problem_004()


