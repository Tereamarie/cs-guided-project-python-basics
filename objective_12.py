"""
Modify this function to make it return the sum of the arguments a and b.
"""
def sum(a, b):
    # DELETE THE PASS STATEMENT AND WRITE YOUR CODE HERE
    sum = a + b
    return sum
# This should print 7
print(sum(2, 5))


"""
Modify this function to use the sum function above to return
the double of the sum of a and b.
"""
def double_the_sum(a, b):
    # DELETE THE PASS STATEMENT AND WRITE YOUR CODE HERE
    # Store the sum in a local variable
    sum = a + b

  # Double it if a and b are the same
    if a * b:
      sum = sum * 2
      return sum
    

# This should print 14
print(double_the_sum(2, 5))