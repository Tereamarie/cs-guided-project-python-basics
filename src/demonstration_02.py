"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

Examples:
-print(convert(5)) ➞ 300
-print(convert(3)) ➞ 180
-print(convert(2)) ➞ 120
"""
# We can times minutes by 60 to get seconds
# def convert(minutes):
#     # set seconds to the value of the expression minutes * 60
#     # Your code here
#     seconds = minutes * 60
#     # return seconds
#     return seconds
def convert(minutes):
    #  return the value of the expression minutes * 60 to caller
    return minutes * 60
    # Your code here
    
    
    

print(convert(5))# ➞ 300
print(convert(3)) #➞ 180
print(convert(2))# ➞ 120