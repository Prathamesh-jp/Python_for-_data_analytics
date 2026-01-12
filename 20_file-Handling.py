a = "harry is good"

# file = open("harry.txt","w")
# file.write(a)

# file = open("harry.txt","r")
# content = file.read()
# print(content)

# file.close()


# append file

a = "\n Rohan is also good"

# file = open("harry.txt", "a")
# file.write(a)
# file.close()


# with file

with open ("harry.txt", "a") as f: # if we use this function then we do not need to use file.close it can automatically close the file
    f.write(a)