a = 10 / 0
print(a)       # this is ZeroDivisionError


a = 5 + "cat"
print(a)       # this is TypeError



a = [3, 5, 2, 7, 3]
print(a[10])   # this is IndexError


# let's observe an example (how to use try except):
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    k = a / b
    print(k)
except:
    print("Encountered an error")
    # here if we take 0 as value of b we will get the except code running ignoring the code in try.


# another example:
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")


# using else:
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)


# using 'finally' to inform the process is complete
a = 5

try:
    c = int(input("Enter a number: "))
    b = a / c
except ZeroDivisionError:
    print("Can't divide by 0")
except ValueError:
    print("Enter a number only: ")
else:
    print("Success, c = ", c)
finally:
    print("Processing Complete")



# another one
def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Can't divide by 0")
        return None

numerator = int(input("Enter numerator number: "))
denominator = int(input("Enter denominator number: "))
print(safe_divide(numerator,denominator))
