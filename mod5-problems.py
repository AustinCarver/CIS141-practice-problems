#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.
n = int(input("Give me a positive integer."))
countup = 1
final = 0
while n >= countup:
    final += countup
    countup += 1
print(final)
#2. Define a string variable (e.g., my_string = "Olympic College"). Use a for loop to print each character on its own line. Convert each character to uppercase before printing.
the_string = ("Yurlok of Scorch Thrash")
for char in the_string:
    print(char.upper())
#3. Use a for loop and the range() function to print all even numbers from 2 to 20.
for int in range(2, 21, 2):
    print(int)
#4. Use nested for loops to create a simple multiplication table for numbers 1 through 5. Format your output so that each row corresponds to multiplying by a specific number.
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:2}" + " ", end='')
    print()
#5. Write a program that continuously asks the user to input a number. If the user enters 0, immediately stop asking for more numbers. Otherwise, print the number they entered.
num = 1
while num != 0:
    num = int(input("Give me a number and please don't make it 0. "))
    if num == 0:
        print("0? Seriously? I'm done with this.")
    if num != 0:
        print(f"Oh, cool your number is {num}. Again?")
