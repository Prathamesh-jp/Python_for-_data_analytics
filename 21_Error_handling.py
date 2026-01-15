print("Intializing.........")

a = int (input ("enter a: \n"))
b = int (input ("enter b: \n"))

try:
    print("The Value of a/b is:", a/b)

except Exception as e:
    print("Some Error Occurred ! -",e)

finally:
    print("I will always run")    


print("Thank you....")