# name = "Tony Stark"
# age = 51
# isGenius = True

# print(name, age, isGenius)

# def person():
#     name = "Tony Stark"
#     age = 51
#     isGenius = True
#     # return(name , age , isGenius)
#     print(name, age, isGenius)

# person()

# def secretName():
#     secret = input("What is ur secret name: ")
#     print(secret)

# secretName()

# def oldAge():
#     old_age = int(input("Enter Your age: "))
#     new_age = old_age + 2
#     print(new_age)

# oldAge()

# def addition():
#     first = int(input("Enter your 1st no. : "))
#     second = int(input("Enter Your 2nd no. : "))
#     sum = first + second
#     print("The sum is ", sum)

# addition()

# def Comp_operator():
#     print(3 > 4 or 4 > 3)   
#     print(3 > 2 and 4 < 3)
#     print(not 2 > 3)

# Comp_operator()

# day = input("Enter the time of day(sun or Moon)")

# def guess():
#     if(day == "Sun" or day == "sun"):
#         print("It's Light")
#     elif(day == "Moon" or day == "moon"):
#         print("It's Night")
#     else:
#         print("It's Invalid")

# guess()

a = input("Enter 1st Number")
b = input("Enter 2nd Number")
choose = (["+", "-", "*", "/"])
print(choose)
input("Enter Choice")

def Calculator():
    if(choose == "+"):
        print(a + b)
    elif(choose == "-"):
        print(a - b)
    elif(choose == "*"):
        print(a * b)
    elif(choose == "/"):
        print(a / b)
    else:
        print("Invalid Choosed Option")

Calculator()