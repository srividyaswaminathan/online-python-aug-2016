# Assignment: Average List
# Create a program that prints the average of the values in the list:

# Check it out! We're pulling in some functionality we already created!
import sum_list

a = [1, 2, 5, 10, 255, 3]

def print_avg(arr):
    return sum_list.sum_list(arr) / len(arr)

print print_avg(a)
