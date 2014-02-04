# Even Fibonacci numbers
# Problem 2
# Each new term in the Fibonacci sequence is generated by adding the previous 
# two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed 
# four million, find the sum of the even-valued terms.


# Answer:
# 4613732

FIB_MEMO = [1, 1]

# 0 => 0
# 1 => 1
# 2 => 2
# 3 => 3
# 4 => 5
# 5 => 8
def fibonnaci(n):
  if(n == 0):
    return 1
  elif(n == 1):
    return 1
  return fibonnaci(n-1) + fibonnaci(n-2)


# Leverages memoization, but assumes that you would never skip.
def fibonnaci_2(n):
  # faulty check
  if n < len(FIB_MEMO):
    return FIB_MEMO[n]
  else:
    newValue = FIB_MEMO[n-1] + FIB_MEMO[n-2]
    FIB_MEMO.insert(n, newValue)
    return newValue


# Recursive
def fibonnaci_3(n):
  if n < len(FIB_MEMO):
    return FIB_MEMO[n]
  else:
    newValue = fibonnaci_3(n-1) + fibonnaci_3(n-2)
    FIB_MEMO.insert(n, newValue)
    return newValue

def problem_002():
  # Alternative to passing in 3rd step param in range() is list comprehension:
  # evens = [x for x in range(100) if x%2 == 0]
  sum, i, term = 0, 0, 0

  while term < 4000000:
    if (term % 2 == 0):
      sum += term
    i += 1                             # no i++ :(
    term = fibonnaci_3(i)

  # `backtick` also works like repr(), when adding str to int
  print "Sum: " + str(sum)



# Execute standalone
problem_002()

# Benchmark
# if __name__ == '__main__':
#   import timeit
#   print(timeit.timeit("problem_002(100)", setup="from __main__ import problem_002", number=100))