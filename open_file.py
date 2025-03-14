with open("file1.txt", "r") as file1:
    read_file = file1.read()
    print(read_file)

# -------------------

with open("file1.txt", "r") as file1:
    read_file = file1.readline()
    print(read_file)
    read_file = file1.readline()
    print(read_file)
    read_file = file1.readline()
    print(read_file)


# ---------------------
with open("file1.txt", "r") as file1:

    read_line1 = file1.readline()

    read_line2 = file1.readline()

    read_line3 = file1.readline()

    
print(read_line1)
print(read_line2)
print(read_line3)
