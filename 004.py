# Largest palindrome product
# Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# Answer:
# 906609




# ==============================================================================
# Start from a palindrome, determine factors
def approach_1():

# 100, 1000
  for i in reversed(range(900,1000)):
    # This is extended slice syntax. It works by doing [begin:end:step]
    # by leaving begin and end off and specifying a step of -1, it reverses a string.
    palindrome = `i` + `i`[::-1]
    print palindrome


# ------------------------------------------------------------------------------
# Multiply two three-digit numbers and determine if its a palindrome
#def isPalindrome(n):

# ------------------------------------------------------------------------------


def problem_004():

  approach_1()


# ------------------------------------------------------------------------------
# Execute standalone
problem_004()


