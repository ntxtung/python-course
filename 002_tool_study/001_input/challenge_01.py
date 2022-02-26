"""
Input a sequence of float in to a variable named "my_list"
"""
data = input('please input: ')
# list comprehension
my_list = [float(x) for x in data.split(' ')]
print(my_list)
