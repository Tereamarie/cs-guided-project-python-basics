"""
1. Create a "numbers" list that contains two different integer values and two different floating point values.

2. Create a "strings" list that contains three different strings.

3. Print the 4th number of your numbers list and the 1st string of your strings list.

4. Iterate through your strings list and print each string.
"""

# YOUR CODE HERE
numbers = []
numbers.append(1)
numbers.append(2.3)
numbers.append(3)
numbers.append(2.0)
print(numbers)

strings = []
strings.append("Lambda")
strings.append("School")
print(strings)

print(numbers[3], strings[0])

sum = 0
for number in numbers:
    sum += number
    print(numbers)
