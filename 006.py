# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


# Answer:
# 25164150


def sumOfSquares(n):
  sum = 0

  for i in range(1, n+1):
    sum += i*i;

  return sum

def sum(n):
  sum = 0
  for i in range(1, n+1):
    sum += i;
  return sum

# ------------------------------------------------------------------------------
def problem_006():

  sumOfSq = sumOfSquares(100)
  sumOfNum = sum(100)

  squareOfSum = sumOfNum*sumOfNum

  print squareOfSum - sumOfSq




  #print "Largest Prime Factor: " + str(lpf)


# ------------------------------------------------------------------------------
# Execute standalone
problem_006()