'''Christopher Ryan'''
name = input("Enter name: ")
name_length = len(name)
while name_length == 0:
    name = input("Invalid name: ")
for i in range(1, name_length, 2):
    print(name[i])
