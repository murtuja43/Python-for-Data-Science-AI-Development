with open("file1.txt", "r") as file1:
    read_line1 = file1.readline()
    read_line2 = file1.readline()
    read_line3 = file1.readline()

print(read_line1)
print(read_line2)
print(read_line3)

if "This is the" in read_line1:
    print("Correct line")
else:
    print("This is not in line")


# -----------
with open("file1.txt","r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1


# --------------

