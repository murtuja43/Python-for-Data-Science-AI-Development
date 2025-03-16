# copy files from file 2 to 1:

list = ["This is 1", "This is 2", "This is 3"]
with open("prac2_txt_file2.txt", "w") as File2:
    for item in list:
        File2.write(item + "\n")


with open("prac2_txt_file1.txt", "w") as File1:
    File1.write("This is the heading \n")


with open("prac2_txt_file2.txt", "r") as Copy_file:
    with open("prac2_txt_file1.txt", "a") as Paste_file:
        for file in Copy_file:
            Check_paste_file = Paste_file.write(file)



# with open("prac2_txt_file2.txt", "r") as Read_file:
#     check_file = Read_file.read()

# print(check_file)


with open("prac2_txt_file1.txt", "r") as Read_file:
    check_file = Read_file.read()

print(check_file)
