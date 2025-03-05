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
