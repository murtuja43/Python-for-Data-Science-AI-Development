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
    '''this function says hello to a user after they input their name when asked'''
    greetings = (f"Hello {name}!")
    return greetings

greet_them = greet(input("Your name: "))
print(greet_them)


# ------------------------


def multiply(a, b):
    """
    This function multiplies two numbers.
    Input: a (number), b (number)
    Output: Product of a and b
    """
    print(a * b)
multiply(2,6)               # we don't have to type print to print a defined funciton

# ------------------------


def sum(a, b):
    print(a + b)
    return a + b

sum(4, 2)


# ------------------------


def loop_test(ending):
    for i in range(2, ending+1):
        print(i)

loop_test(8)


# ------------------------


# ------------------------
