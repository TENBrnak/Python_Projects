#A very simple program that prints out the initals of a name input
name = input("Input your full name. ")
split_name = name.split()
output_initials = ""
for i in split_name:
    for j in i:
        output_initials += j.upper()
        if len(output_initials) < 2:
            output_initials += "."
        break
print(output_initials)
