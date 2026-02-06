#1. Write a Program to input 2 numbers & print their sum.
first = int(input("enter first : ")) 
second = int(input("enter second : "))

print("sum =", first + second)


#2. WAP to input side of a square & print its area
side = float(input("enter square side : ")) 

# print("area =", side * side)
print("area =", side ** 2)

#3. WAP to input 2 floating point numbers & print their average.
a = float(input("enter first : ")) 
b = float(input("enter second : "))

print("avg =", (a+b)/2)

#4. WAP to input 2 int numbers, a and b. Print True if a is greater than or equal to b. If not print False (a>=b True or False)
a = int(input("enter first : ")) 
b = int(input("enter second : "))

print(a >= b)