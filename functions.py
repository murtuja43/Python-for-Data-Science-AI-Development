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


def greet(name):
    return (f"Hello, {name}")

for _ in range(3):
    print(greet("Alice"))


# ------------------------



# ------------------------Here we used a blank list and two funcitons and letter on we used the functions to add and remove elements from the list

my_list = []

def add_elements(list_name, element):
    list_name.append(element)

def remove_elements(list_name, element):
    if element in list_name:
        list_name.remove(element)
    else:
        print("The element is not in the list")


add_elements(my_list, 43)
add_elements(my_list, 1)
add_elements(my_list, 4)
add_elements(my_list, 41)
remove_elements(my_list, 41)
remove_elements(my_list, 49)

print(my_list)


# ------------------------



# ------------------------

scores = []

def add_scores(scores, addremove_the_score):
    scores.append(addremove_the_score)


def remove_scores(scores, addremove_the_score):
    if addremove_the_score in scores:
        scores.remove(addremove_the_score)
    else:
        print(f"The score {addremove_the_score} that you want to remove is not in the score list")

add_scores(scores, 43)
add_scores(scores, 48)
add_scores(scores, 41)
remove_scores(scores, 40)

print(scores)


# ------------------------


# ------------------------

# using Try- except 
try:
    # Attempting to divide 10 by 0
    result = 10 / 0
except ZeroDivisionError:
    # Handling the ZeroDivisionError and printing an error message
    print("Error: Cannot divide by zero")
# This line will be executed regardless of whether an exception occurred
print("outside of try and except block")


# ------------------------


# ------------------------
