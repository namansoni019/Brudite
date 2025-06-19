"""If a number is divisible by 3 it should print “SKILLBREW”
as a string
If a number is divisible by 5 it should print “BRUDITE” as a
string
If a number is divisible by both 3 and 5 it should print
“BRUDITE - NIRVANA” as a string."""
print("question no. 1:")
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("BRUDITE - NIRVANA")
elif num % 3 == 0:
    print("SKILLBREW")
elif num % 5 == 0:
    print("BRUDITE")
else:
    print("Not divisible by 3 or 5")

"""Write a program that accepts a string as input from
the user and calculates the number of digits and
letters.
Input: Hello123
Output: Alphabets: 5 & Number : 3"""
print("question no. 2:")
alpha =0
num=0
for i in list("Hello123"):
    if i.isalpha():
      alpha +=1
    elif i.isnumeric():
       num +=1
num +=1
print(f"total alphabets:{alpha}")
print(f"total nums:{num}")

"""Write a Python program to input marks for five
subjects Physics, Chemistry, Biology, Mathematics,
and Computer. Calculate the percentage and grade
according to the following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% :  Grade F"""
print("question no. 3:")
physics = float(input("Enter marks in Physics: "))
chemistry = float(input("Enter marks in Chemistry: "))
biology = float(input("Enter marks in Biology: "))
mathematics = float(input("Enter marks in Mathematics: "))
computer = float(input("Enter marks in Computer: "))

total_marks = physics + chemistry + biology + mathematics + computer
percentage = (total_marks / 500) * 100

print(f"Percentage: {percentage:.2f}%")

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
elif percentage >= 40:
    grade = 'E'
else:
    grade = 'F'

print(f"Grade: {grade}")

"""Write a Python program to find the sum of all odd
numbers between two given numbers.
Start = 1, stop = 10
Sum of odd numbers: 25"""
print("question no. 4:")
start = int(input("Enter the start number: "))
stop = int(input("Enter the stop number: "))

odd_sum = 0

for i in range(start, stop + 1):
    if i % 2 != 0:
        odd_sum += i

print("Sum of odd numbers:", odd_sum)

"""Write a Python program to find the factorial of a
number using a for loop."""
print("question no. 5:")
num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")

"""Write a Python program to check if a given number
is a perfect number.
A Perfect number is a positive integer that is equal to the
sum of its proper divisors. For instance, 6 has divisors 1, 2,
and 3, and 1 + 2 + 3 = 6, so 6 is a perfect number.
Input: 5
Output: No """
print("question no.6: ")
num = int(input("Enter a number: "))
sum_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_divisors += i

if sum_divisors == num:
    print("Yes, it's a Perfect Number")
else:
    print("No, it's not a Perfect Number")

"""Write a Python program to check if a string is an
anagram of another string.
string1 = "listen", string2 = "silent"
Output: True """
print("question no.7: ")
str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()

if sorted(str1) == sorted(str2):
    print("True (Anagram)")
else:
    print("False (Not an Anagram)")

"""Write a Python program to calculate the LCM (Least
Common Multiple) of two numbers.
number1 = 12, number2 = 18
LCM of 12 and 18 are: 36"""
print("question no. 8: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    greater = num1
else:
    greater = num2

while True:
    if (greater % num1 == 0) and (greater % num2 == 0):
        lcm = greater
        break
    greater += 1

print(f"LCM of {num1} and {num2} is: {lcm}")

""" Write a Python program to count the frequency of
each element in a list.
Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}"""
print("question no. 9: ")
input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
frequency = {}

for item in input_list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Frequency count:", frequency)

"""Write a Python program to reverse the order of
words in a given sentence.
Input_sentence = “Hello, World! Welcome to Python
programming.”
Output after reverse = “programming. Python to Welcome
World! Hello,”"""
print("question no. 10:")
input_sentence = "Hello, World! Welcome to Python programming."
words = input_sentence.split() 
reversed_words = words[::-1]   
output = " ".join(reversed_words)  
print("Output after reverse:", output)

"""Write a Python program to calculate the sum of
digits of a given number until the sum becomes a
single-digit number.
Sample Input: num = 987
Sample Output: Sum_of_digits = 24,
Again compute the sum of digits so that it can be reduced
to
on single digit.
Final Output: 6"""
print("question no. 11: ")
num = int(input("Enter a number: "))

def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10  
        n = n // 10  
    return s

while num >= 10:
    num = digit_sum(num)
    print("Intermediate Sum:", num)

print("Final Output:", num)

"""Write a Python program to reverse a number using
a while loop.
Sample Input: num = 12345
Sample Output: revnum = 54321"""
print("question no. 12:")
num = int(input("Enter a number: "))
revnum = 0

while num > 0:
    digit = num % 10 
    revnum = revnum * 10 + digit 
    num = num // 10            

print("Reversed number:", revnum)

