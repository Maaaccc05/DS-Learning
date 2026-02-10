# ---Basic--- 

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

# ---Calculation---

# def addition():
#     first = int(input("Enter your 1st no. : "))
#     second = int(input("Enter Your 2nd no. : "))
#     sum = first + second
#     print("The sum is ", sum)

# addition()

# ---Comparison Operator---

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

# --- Calculator---

# a = int(input("Enter 1st Number: "))
# b = int(input("Enter 2nd Number: "))
# choose = input("Enter the Operator(+, -, *, / ): ")
# def Calculator():
#     if(choose == "+"):
#         print(a + b)
#     elif(choose == "-"):
#         print(a - b)
#     elif(choose == "*"):
#         print(a * b)
#     elif(choose == "/"):
#         print(a / b)
#     else:
#         print("Option choosed is Invalid")

# Calculator()

# ---While Loop---

# i = 1
# while(i <= 5):
#     print(i)
#     i = i + 1

# i = 1
# while(i <= 5):
#     print(i * "*")
#     i = i + 1
# print("\n")
# i = 5
# while(i >= 0):
#     print(i * "*")
#     i = i - 1


# for loop
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         print(i * i)

# leap year program

# def is_leap(year):
#     leap = False
    
#     if year % 400 == 0:
#         leap = True
#     elif year % 100 == 0:
#         leap = False
#     elif year % 4 == 0:
#         leap = True
#     else:
#         leap = False
#     return leap

# year = int(input())
# print(is_leap(year))

# if __name__ == '__main__':
#     n = int(input())
#     for i in range(1,n + 1):
#         print(i, end="")


# for i in range(5):
#     print(i)


#---Lists---

# marks = [1, 2, 3]
# print(marks[-3])
# for m in marks:
#     print(m)

# marks.append(99)
# marks.insert(0, 99)
# print(2 in marks)

# i = 0
# while i < len(marks):
#     print(marks[i])
#     i = i + 1

# students = ["Mac", "Sak", "Kam", "Bo", "Janhvee"]

# for student in students:
#     if student == "Kam":
#         continue
#     print(student)

#---TUples---

# marks = (1,2,3)
# print(marks(type))

#---Set---

# person = {1,2,3,4,5,5}

# for persons in person:
#     print(persons)

#---Dictionaries---

# marks = {"English" : 98, "Chem" : 99}
# print(marks["Chem"])

# marks["Chem"] = 87
# print(marks)
# marks["Physics"] = 90
# print(marks)

#---Funtions---

# from math import sqrt
# print(dir(math))
# print(sqrt(16))

# a = 1
# b = 2
# def printSum(a, b):
#     print(a + b)

# printSum(1 , 2)