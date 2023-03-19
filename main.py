# 1
def name_age():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print("Hello", name + ". Your age is:", age)
    return name + age

name_age()

# 2
def swap_integers(num1, num2):
    print("Before swap:")
    print("X =", num1)
    print("Y =", num2)

    temp = num1
    num1 = num2
    num2 = temp

    print("After swap:")
    print("X =", num1)
    print("Y =", num2)

    return str(num1) + str(num2)

# Example
swap_integers(10, 20)

# 3
def check_numbers(num1, num2):
    div_by_6 = (num1 % 6 == 0) or (num2 % 6 == 0)
    div_by_10 = (num1 % 10 == 0) and (num2 % 10 == 0)

    if div_by_6 and div_by_10:
        return True
    else:
        return False

# Example
print(check_numbers(6, 10)) # False
print(check_numbers(60, 120)) # True

# 4
def sum_up(num1, num2):
    if num1 > num2 or num1 <= 0 or num2 <= 0:
        return 0
    else:
        total_sum = 0
        for i in range(num1, num2 + 1):
            total_sum += i
        return total_sum

# Example
print(sum_up(3, 9))
print(sum_up(9, 3))
print(sum_up(-2, 9))
print(sum_up(3, -9))
print(sum_up(0, 9))

# 5
def circle_area(r1, r2, r3):
    pi = 3.14
    area1 = pi * r1 ** 2
    area2 = pi * r2 ** 2
    area3 = pi * r3 ** 2
    return area1 + area2 + area3

# Example
print(circle_area(3, 4, 5))

# 6
def check_string(text):
    return text.lower().startswith('a') or text.lower().endswith('a')

# Example
print(check_string('Apple')) # Output: True
print(check_string('banana')) # Output: True
print(check_string('orange')) # Output: False

# 7
def triangle(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()

# Example
triangle(4)
