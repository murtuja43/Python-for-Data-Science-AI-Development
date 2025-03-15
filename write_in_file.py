with open("new_file2.txt", "w") as Write_file:
    New_line_add1 = Write_file.write("This is line 1")
    New_line_add2 = Write_file.write("This is line 2")
    New_line_add3= Write_file.write("This is line 3")





with open("new_file2.txt", "r") as File2:
    open_file_2 = File2.read()

print(open_file_2)