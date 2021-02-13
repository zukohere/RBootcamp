# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    num_items = len(numbers)
    sum_items = sum(numbers)
    return sum_items/num_items
  


# Test your function with the following:
print(average([1, 5, 9]))

#print(average(range(11)))