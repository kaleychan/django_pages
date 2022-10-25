# w3resource question 24:
word = input("what is the word:")
vowel = 'a,e,i,o,u'
if word in vowel:
    print("this is vowel")
else:
    print("this is not")

# question 25:
data = int(input("what is the number"))
list = [1,5,8,3]
if data in list:
    print("yes")
else:
    print("no")

# question 27:

# question 28:
list = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
for n in list:
    if n == 237:
        print(n)
        break;
    elif n %2 ==0:
        print(n)

# question 30:
h = int(input("what is the height:"))
base = int(input("what is the base:"))

area = (h*base)/2

print(area)

# question 31:
import math
n = int(input("what is the number1:"))
n1 = int(input("what is the number2:"))

n2 = math.gcd(n,n1)

print(n2)

# question 32:
import math
n1 = int(input("what is n1:"))
n2 = int(input("what is n2:"))
n3 = math.lcm(n1,n2)

print(n3)

# question 33:
n1 = int(input("what is the first:"))
n2 = int(input("what is the second:"))
n3 = int(input("what is the third:"))
sum_number = n1+n2+n3
# Only " if " , don't need "def" or "for"
if n1 == n2 or n1 == n3 or n2 == n3:
    print("this is 0")
else:
    print(sum_number)

# question 34:
n1 = int(input("what is the first:"))
n2 = int(input("what is the second:"))
sum_number = n1 + n2

if sum_number >=15 and sum_number<=20:
    print("20")

else:
    print(sum_number)

# question 35:
def number(n1,n2):
    if n1 == n2 or n1 + n2 ==5 or n1 - n2 ==5: # directly put all three tgt
        return("True") # must use return (if use print will have three "None" between answer)
    else:
        return("False")
print(number(3,3))
print(number(2,3))
print(number(5,6))

# question 36:
def object(n1,n2):
    if isinstance(n1,int) and isinstance(n2,int): # isinstance for identify what type of the specific value
        return n1+n2
    else:
        return("It is not")

print(object("hello","hi"))
print(object(5,6))

# question 37:
name = input("what is your name:")
age = input("what is your age:")
address = input("what is your address:")

print("name:",name)
print("Age:",age)
print("Address:",address)

#question 38:

x = 4
y = 3
solved = (x+y)*(x+y)

print("(4+3)^2)=",solved)

# question 40:
import math

p = [4,0]
q = [6,6]

print((math.dist(p,q)))

#question 41:
import os.path # os.path -> for check the operation system
print(os.path.isfile("mypython.py")) # isfile -> check is the file exit or not
print(os.path.isfile("kaley"))

#question 43::
import platform
import os
print("what is the os name:",os.name)
print("what is the platform:",platform.system())
print("what is the release information:",platform.release())

#question 44:
import site  # for get the site-packages
print(site.getsitepackages())

# question 45:
import os # for check all the file
print(os.system('ls -l'))


#question 46:
import os
print(os.getcwd())
