#arithmetic operators
a = 5
b = 2

# sum = a + b
# print(sum)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #remainder
print(a ** b) # a^b


#relational operators
a = 50
b = 20

print(a == b) #False
print(a != b) #True
print(a >= b) #True
print(a > b) #True
print(a <= b) #False
print(a < b) #False


#assignment operators
num = 10
# num = num + 10 #10+10 => 20
num += 10
print("num :", num)


#logical operators
a = 50
b = 30
print(not False)
print(not (a > b))

val1 = False
val2 = False
print("AND operator:", val1 and val2)

# print("OR operator:", val1 or val2)
print("OR operator:", (a == b) or (a > b))


# Type Conversion

a = 2
b = 4.25

sum = a + b # 2.0 + 4.25 => 6.25
print(sum)

# OR

a = "2"
b = 4.25

print(type(a))

# Type Casting 
a, b = 1, "2"
c = int(b)
sum = a + c

# OR

# a = int("2")
a = float("2")
b = 4.25

print(type(a))
print(a + b)

# Any values
a = 3.14
a = str(a)

print(type(a))

# Input in Python
#input() statement is used to accept values(using keyboard) from  user
# input("Enter your name: ")

name = input("Enter your name: ")
print("Welcome ", name)

name = input("Enter your age: ")
print("you entered ", name)

# input() #result for input() is always a str
val = input("enter some value: ")
print(type(val), val) # "25", "99.99"

int("5")
val = int(input("enter some value: "))
print(type(val), val) # "25", "99.99"

int("5")
val = float(input("enter some value: "))
print(type(val), val) # "25", "99.99"


name = input("enter name: ")
age = input("enter age: ")
marks = input("enter marks: ")

print("welcome", name)
print("age =", age)
print("marks =", marks)

name = input("enter name: ")
age = int(input("enter age: "))
marks = float(input("enter marks: "))

print("welcome", name)