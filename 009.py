# Large sum
# Problem 13

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Answer:
# 31875000


def isPythagoreanTriplet(a, b, c):
  return a**2 + b**2 == c**2

# ------------------------------------------------------------------------------
def problem_009():

  # a + b + c = 1000
  # a < b < c 
  # c = [3, 997], b = [2, c-1], a = [1, b-1]
  # since a + b + c = 100, 
  #   - c cannot be less than 335. anything less and we won't add up to 1,000
  #   - b cannot exceed 499. any more and we add up past 1,000
  #   - a cannot exceed 332. any more and we add up past 1,000
  # c = [335, 997], b = [2, c-1], a = [1, b-1]

  # Off this information, b has 660+ possible values, b has 500, a has 332.
  # Loop through possible values of a (1, 332)
  for a in range(1, 333):
    for b in range(a, 499):
      c = 1000 - a - b
      # print "(" + `a` + ", " + `b` + ", " + `c` + ")"
      if isPythagoreanTriplet(a, b, c):
        print "Found! Product is " + `a*b*c`
        #break


# ------------------------------------------------------------------------------
# Execute standalone
problem_009()
