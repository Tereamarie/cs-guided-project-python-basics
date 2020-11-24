"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
print(sort_by_length(["a", "ccc", "dddd", "bb"])) # ➞ ["a", "bb", "ccc", "dddd"]
print(sort_by_length(["apple", "pie", "shortcake"])) # ➞ ["pie", "apple", "shortcake"]
print(sort_by_length(["may", "april", "september", "august"])) # ➞ ["may", "april", "august", "september"]
print(sort_by_length([])) # ➞ []
"""
def sort_by_length(lst):
    # Your code here
    #lst.sort(key=len)
    #return lst
    return sorted(lst, key=len)
   
print(sort_by_length(["a", "ccc", "dddd", "bb"])) # ➞ ["a", "bb", "ccc", "dddd"]
print(sort_by_length(["apple", "pie", "shortcake"])) # ➞ ["pie", "apple", "shortcake"]
print(sort_by_length(["may", "april", "september", "august"])) # ➞ ["may", "april", "august", "september"]
print(sort_by_length([])) # ➞ []