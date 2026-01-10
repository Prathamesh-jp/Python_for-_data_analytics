# def greet(name):
#     print("Good Morning !",name)
#     print("How are You" , name)
#     print("Thank You !", name)

# greet("harry")    

def add(a,b):
    print(a+b)

c = add(4,6)

print(c) 


# give the default value to parameter

def greet(name = "user", city ="Delhi"):
    print("Hello", name, city)

greet()
greet("Rohan")

greet(city = "Alwar", name = "Aakash")

# lambada functions

add = lambda a, b : a + b;

print(add(5,7))