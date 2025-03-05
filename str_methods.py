Escape Sequences
\n - makes new line
\t - makes tab space
\\ - write one \ in the line

1. raw_string = r"C:\new_folder\file.txt"
2. print("Raw String:", raw_string)
# here we used ‘r’ before the string and that’s why it will be raw string and escape sequences won’t work and actual backslash (\) will be printed


Some strings methods:
A = “I am the best”
1. A.upper()
2. A.replace(‘a’, ‘b’)
3. A.find(‘a’)
4. A.split()
5. A.group()

pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)
