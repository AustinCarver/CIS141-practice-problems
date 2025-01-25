# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")

# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
x, y = input("Enter a number."), input("Enter a second number.")
print("Addition:", int(x)+int(y))
print("Subtraction:", int(x)-int(y))
print("Multiplication:", int(x)*int(y))
print("Division:", int(x)/int(y))

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
import math
a, b, c = input("Triangle's first side's length?"), input("Triangle's second side's length?"), input("Triangle's third side's length?")
s = 0.5*(int(a)+int(b)+int(c))
A = math.sqrt(float(s)*(float(s)-int(a))*(float(s)-int(b))*(float(s)-int(c)))
print("Triangle Area =", A)

# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).
import math
a, b, c, d, e = input("Enter a number."), input("Enter a second number."), input("Enter a third number."), input("Enter a fourth number."), input("Enter a fifth number.")
f = max(a,b,c,d,e) #Maximum as a variable
g = min(a,b,c,d,e) #Minimum as a variable
h = ((float(a)+float(b)+float(c)+float(d)+float(e))/5) #average calculation
i, j, k, l, m = pow((float(a)-float(h)), 2), pow((float(b)-float(h)), 2), pow((float(c)-float(h)), 2), pow((float(d)-float(h)), 2), pow((float(e)-float(h)), 2) #Deviation from the mean, and square the result
n = (float(i)+float(j)+float(k)+float(l)+float(m))/5 #Average this
o = math.sqrt(n) #Square Root of the averaging of the calculations
print("Total:", (float(a)+float(b)+float(c)+float(d)+float(e)))
print("Average:", float(h))
print("Minimum:", min(a,b,c,d,e))
print("Maximum:", max(a,b,c,d,e))
print("Range:", (float(f)-float(g)))
print("Standard Deviation:", float(o))
