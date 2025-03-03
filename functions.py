def function_name():
    pass                    #if we don't want to give any condition of functionality in our function we use 'pass'

# ------------------------


def calculate_total(a, b):  # Parameters: a and b
    total = a**2 + b**2           # Task: Addition
    return total            # Output: Sum of a and b

result = calculate_total(5, 7)  # Calling the function with inputs 5 and 7
print(result)  # Output: 12


# ------------------------

def number_addition(first_number, second_number, third_number):
    total = first_number + second_number + third_number
    return total

addnumber = number_addition(34, 4, 2)
print(addnumber)


# ------------------------


a = [2, 45, 23, 623,234, 67, 83, 234, 741]
print(max(a), min(a), sum(a))


# ------------------------

def greet(name):
    greetings = ("Hello " + name)
    return greetings

greet_them = greet(input("Your name: "))
print(greet_them)



