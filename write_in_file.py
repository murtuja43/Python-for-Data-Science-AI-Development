lines = ["This is line 1", "This is line 2", "This is line 3"]
with open("new_file2.txt", "w") as Write_file:
    for line in lines:
        Write_file.write(line + "\n")



new_data = "This is line 3.1"
with open("new_file2.txt", "a") as Write_file2:   #use "a" to add (append) new data in the write file.
    Write_file2.write(new_data + "\n")

with open("new_file2.txt", "r") as File2:
    open_file_2 = File2.read()

print(open_file_2)




# ------------------
with open("file1.txt", "r") as Read_file: #copying from one file to another
    with open("new_file3.txt", "w") as Write_file:
        for i in Read_file:
            Write_file.write(i)


new_data2 = "This is line 7"
new_data3 = "This is line 8"
with open("new_file3.txt", "a") as append_file:
    append_file.write(new_data2 + "\n" + new_data3 + "\n")



with open("new_file3.txt", "r") as Check_file: #reading the file 
    check1 = Check_file.read()
print(check1)
