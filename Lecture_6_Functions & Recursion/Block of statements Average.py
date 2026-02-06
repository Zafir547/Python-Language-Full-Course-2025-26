# average of 3 numbers

# def calc_avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg

# calc_avg(1,5,4) 

def calc_avg(a,b,c):
    if a == 0:
        total = a+b+c
        avg = total/3
        print("a is zero. Average:",avg)
        return avg
    elif a < 0:
        print("Warning: a is negative. Cannot calculate average.")
        return None
    else:
        total = a + b + c
        avg = total / 3
        print("a is positve. Average:", avg)
        return avg

calc_avg(0, 5, 4)   # a == 0
calc_avg(-1, 5, 4)  # a < 0
calc_avg(2, 5, 4)   # a > 0    