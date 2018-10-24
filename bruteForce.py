# Define variable to hold sum of multiples of 3 and 5
sumMultiples = 0

# Iterate from 1 to 999
for i in range(1, 1000):
  
  # If i is divisible by 3 or 5, add it to the sum of multiples
  if i % 3 == 0 or i % 5 == 0:
      sumMultiples += i
  
  # Otherwise... don't
  else:
    continue

# Print the result
print(sumMultiples)
