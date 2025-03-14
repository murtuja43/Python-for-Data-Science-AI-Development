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
