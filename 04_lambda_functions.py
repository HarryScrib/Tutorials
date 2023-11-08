# typical function
def add(x, y):
    return x + y
# return 9
print(add(4, 5))

# lambda version of the function
lambda x,y: x+y

# example of using lambda as a variable - don't do this
add2 = lambda x, y: x + y
print(add2(4, 5))

# using print with lambda parenthesis
print((lambda x, y: x + y)(4, 5))

# example of higher order function with lambda involvement
# rebuilding python's built in map function
def my_map(my_func, my_iterable):
    #initialise our result that we want to return as empty list 
    result = []
    # iterate through each item of my iterable and apply my_func to each item
    for item in my_iterable: 
        # give us a new item
        new_item = my_func(item)
        # append item to result list
        result.append(new_item)
    
    return(result)

nums = [3, 4, 5, 6, 7]

# cube each of the items in list nums
# have to input a function and an iterable as inputs
cubed = my_map(lambda x: x ** 3, nums)

print(cubed)

# i included 2 of my own examples as an exercise

# example 1
# multiplying by 2

# define a higher-order function that takes a function as an argument
def apply_function(func, value):
    # call the function and return the result
    result = func(value)
    return result

# define a value we want to process
number = 5

# pass the lambda function that doubles the input to the higher-order function and store the result
result = apply_function(lambda x: x * 2, number)

# Print the result
print(f'Result: {result}')

# my example 2
# calculating total price of shopping list

# define a higher-order function that calculates the total cost of items in a shopping cart
def calculate_total_cost(cart, price_function):
    total = 0
    for item in cart:
        total += price_function(item)
    return total

# define a list representing a shopping cart with items and quantities
shopping_cart = [
    {"item": "Shirt", "quantity": 2},
    {"item": "Shoes", "quantity": 1},
    {"item": "Jeans", "quantity": 6},
]

# define lambda functions to calculate the price of each item based on quantity
price_lambda = lambda item: item["quantity"] * (10 if item["item"] == "Shirt" else 50)

# calculate the total cost using the lambda function and the shopping cart
total_cost = calculate_total_cost(shopping_cart, price_lambda)

# print the total cost
print(f"Total cost of items in the shopping cart: ${total_cost}")

# lambda function as an output:

# define a function that returns a lambda function
def multiplier(factor):
    # define and return a lambda function
    return lambda x: x * factor

# create a lambda function that multiplies by 2
double = multiplier(2)

# use the lambda function to double a number
result = double(5)

# print the result
print(f"Result: {result}")