# This is an hello world file
print("Hello, World!")  

age = "25"

print(int(age)+5) #this is the example of type conversion from string to integer

price = 19.99
print(float(price)+10)#this is the example of type conversion from integer to float

num = "123abc"
print(int(num)) #this will raise an error because the string contains non-numeric characters ValueError: invalid literal for int() with base 10: '123abc'