# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
# get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# Answer:
# 233168

sum = 0

# range is exclusive of the lsat number
for x in range(0,1000):
  if(x % 3 == 0):
    sum += x
  elif(x % 5 == 0):
    sum += x

print sum
