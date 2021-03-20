#!/usr/bin/env python
# coding: utf-8

# 2. Write a Python program to get the Python version you are using.

# In[2]:


import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# 3. Write a Python program to display the current date and time.

# In[3]:


import datetime
now= datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%y-%m-%d %H:%M:%S"))


# 4. Write a Python program which accepts the radius of a circle from the user and compute the area.

# In[6]:


Radius= 1.1
Area= 3.14 *Radius*Radius
print(Area)


# In[7]:


from math import pi
r= float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: "  + str(pi *r**2))


# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

# In[8]:


fname = input("Input your First Name : ")
lname= input("Input your Last Name")
print ("Hello  " + lname + " " + fname)


# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

# In[9]:


values = input("Input some comma separated numbers : ")
list= values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ', tuple)


# 7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
# Sample filename : abc.java
# Output : java

# In[11]:


filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))


# 8. Write a Python program to display the first and last colors from the following list. Go to the editor
# color_list = ["Red","Green","White" ,"Black"]

# In[12]:


color_list = ["Red", "Green", "White", "Black"]
print( "%s %s"%(color_list[0], color_list[-1]))


# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).

# In[13]:


exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)


# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.

# In[18]:


a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int(  "%s%s" % (a,a) )
n3 = int("%s%s%s" % (a,a,a) )
print (n1+n2+n3)


# 12. Write a Python program to print the calendar of a given month and year.

# In[20]:


import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y,m))


# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

# In[22]:


from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)


# 15. Write a Python program to get the volume of a sphere with radius 6.

# In[26]:


radius = int(input( "Input radius : "))
V = 4/3 * pi * radius**3
print(V)


# 16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

# In[36]:


def difference(n):
    if n <=17:
        return 17 - n
    else:
        return (n-17)*2


# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

# In[32]:


def near_thousand(n):
                    return ((abs(1000 - n) <= 100) or (abs(2000-n) <= 100))
print(near_thousand(1000))


# 18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

# In[34]:


def numbers_same(x,y,z):
    sum = x + y + z 
    
    if x == y == z:
        sum = sum * 3
        return sum


# 19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

# In[35]:


def new_string(str): 
    if len(str) >= 2 and str[:2] == "Is":
        return str
    return "Is" + str
print(new_string("Dancing"))


# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

# In[37]:


def larger_string(str, n):
    result = ""
    for i in range(n):
        result = result + str
        return result 
    
print(larger_string('abc', 2))


# 21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

# In[40]:


number = int(input("Input number : "))
mod = number % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
    


# 22. Write a Python program to count the number 4 in a given list.

# In[41]:


def list_count_4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1
    return count

print(list_count_4([1,4,5,4,9]))


# 24. Write a Python program to test whether a passed letter is a vowel or not.

# In[51]:


def vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels 
print(vowel('e'))


# 25. Write a Python program to check whether a specified value is contained in a group of values.

# In[53]:


def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
        else:
            return False
print(is_group_member([1,5,8,3], 3))


# In[54]:


def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times < 0):
            output += '*'
            times = times - 1
            print(output)
histogram([2,3,6,5])


# In[55]:


def concatenate_list_data(list):
    result = ''
    for element in list:
        result += str(element)
        return result
print(concatenate_list_data([1, 5, 12, 2]))


# 26. Write a Python program to create a histogram from a given list of integers. 

# In[62]:


def histogram( items ):
    for n in items:
        output= ''
        times= n 
        while( times > 0):
            output += '*'
            times = times - 1
        print(output)
        
histogram([2,3,6,5])


# 27. Write a Python program to concatenate all elements in a list into a string and return it

# In[64]:


def concatenate_list_data(list):
    result = ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data([1,5,12,2]))


# 28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.

# In[66]:


list = [
    123, 406, 543, 901, 208, 52, 101, 64
]
def even_numbers(list):
    result = ''
    for element in list:
        if element == 237:
            print(x)
            break;
        elif x % 2 == 0:
            print(x)


# 29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

# In[67]:


color_list_1 = set(["White", "Black", "Red" ])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))


# 30. Write a Python program that will accept the base and height of a triangle and compute the area.

# In[70]:


base = int(input("Input the base : " ))
height = int(input("Input the height : " ))
area = 1/2 * base * height
print(area)


# 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers. 

# In[73]:


def gcd(x,y): 
    gcd = 1
    
    if x % y == 0:
        return y 
    
    for k in range(int(y/2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
        return gcd
    
print(gcd(100, 36))


# 32. Write a Python program to get the least common multiple (LCM) of two positive integers.

# In[75]:


def lcm(x,y):
    if x > y:
        z = x
    else:
        z = y
        
    while(True):
            if((z % x == 0) and (z % y == 0)):
                lcm = z
                break
            z += 1 
    return lcm
print(lcm(4,6))


# 33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

# In[80]:


def sum(x, y, z):
    if x==y or x == z or y == z:
        sum = 0
    else: 
        sum = x + y + z
    return sum

print(sum(1,2,3))


# 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

# In[85]:


def sum(x, y):
    sum = x + y 
    if sum in range(15,20):
        return 20 
    else:
        return sum
print(sum(10,5))


# 35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

# In[87]:


def sum(x,y):
    sum = x + y 
    if x == y or x - y == 5 or y - x == 5 or x + y == 5:
        return True 
    else:
        return False 
print(sum(5,2))


# 36. Write a Python program to add two objects if both objects are an integer type. 

# In[88]:


def add_numbers(a,b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    return a + b 
print(add_numbers(10,20))


# 37. Write a Python program to display your details like name, age, address in three different lines. 

# In[93]:


def display_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
display_details()


# 38. Write a Python program to solve (x + y) * (x + y).

# In[96]:


x, y = 4,3
result = x * x + 2 * x * y + y * y 
print("({} + {}) ^ 2) = {}".format(x,y,result))


# 39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.

# In[97]:


amt = 1000
int = 3.5
years = 7
future_value = amt*((1+(0.01*int)) ** years)
print(round(future_value,2))


# 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

# In[99]:


import math 
p1 = [4,0]
p2 = [6,6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1])**2) )
print(distance)


# 41. Write a Python program to check whether a file exists.

# In[100]:


import os.path
open('abc.txt', 'w')
print(os.path.isfile('abc.txt'))


# 42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

# In[101]:


import struct
print(struct.calcsize("P") * 8)


# 43. Write a Python program to get OS name, platform and release information.

# In[102]:


import platform
import os
print(os.name)
print(platform.system())
print(platform.release())


# 44. Write a Python program to locate Python site-packages.

# In[103]:


import site;
print(site.getsitepackages())


# 47. Write a Python program to find out the number of CPUs using.

# In[107]:


import multiprocessing
print(multiprocessing.cpu_count())


# 49. Write a Python program to list all files in a directory in Python.

# In[110]:


from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/users/jack')]
print(files_list);


# 50. Write a Python program to print without newline or space.

# In[111]:


for i in range(0,10):
    print('*', end="")
print("\n")


# 51. Write a Python program to determine profiling of Python programs.

# In[112]:


import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')


# 52. Write a Python program to print to stderr. 

# In[113]:


from __future__ import print_function
import sys 

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
eprint("abc", "efg", "xyz", sep="--")


# 53. Write a python program to access environment variables. 

# In[2]:


import os
print('*----------------------*')
print(os.environ)
print(os.environ['PATH'])


# 54. Write a Python program to get the current username

# In[3]:


import getpass
print(getpass.getuser())


# 57. Write a program to get execution time for a Python method.

# In[5]:


import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s= 0 
    for i in range(1, n+1):
        s = s + i
    end_time = time.time()
    return s, end_time - start_time
n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is:",sum_of_n_numbers(n))


# 58. Write a python program to find the sum of the first n positive integers.

# In[6]:


n = int(input("Input a number: "))
sum_num = (n * (n + 1)) /2
print(sum_num)


# 59. Write a Python program to convert height (in feet and inches) to centimeters. 

# In[8]:


print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))
h_inch  += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : %d cm." % h_cm)


# 60. Write a Python program to calculate the hypotenuse of a right angled triangle.

# In[12]:


import math
a= int(input("Input length of one side: "))
b= int(input("Input length of other side: "))
hypotenuse = math.sqrt(a**2 + b**2)
print(hypotenuse)


# 61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.

# In[23]:


distance_ft= int(input("Input distance in feet: "))
distance_inches= distance_ft * 12.000
distance_yards = distance_ft/ 3.000
distance_miles = distance_ft/ 5280.000
print("The distance in inches is %i inches." % distance_inches)
print("The distance in yards is %.2f yards." % distance_yards)
print("The distance in miles is %.2f miles." % distance_miles)


# 62. Write a Python program to convert all units of time into seconds.

# In[24]:


days= int(input("Input the number of days: "))
hours= int(input("Input the number of hours: "))
minutes= int(input("Input the number of minutes: "))
seconds= int(input("Input the number of seconds:"))
mins_sec = minutes * 60
hrs_sec= hours * 60 * 60 
days_sec= days * 24 * 60 * 60
time = seconds + mins_sec + hrs_sec + days_sec 
print("The time in seconds is %i." % time)


# 63. Write a Python program to get an absolute file path.

# In[25]:


def absolute_file_path(path_fname):
    import os
    return os.path.abspath('path_fname')
print("Absolute file path: ", absolute_file_path("test.txt"))


# 65. Write a Python program to convert seconds to day, hour, minutes and seconds.

# In[30]:


time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
minutes = time // 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hours, minutes, seconds))


# 66. Write a Python program to calculate body mass index.

# In[31]:


height = float(input("Input your height in feet: "))
weight = float(input("Input your weight in kilograms: "))
print("Your body mass index is: ", round(weight/ (height*height), 2))


# 67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.

# In[32]:


kpa= float(input("Input pressure in kilopascals> "))
psi = kpa / 6.89475729
mmhg = kpa * 760 /101.325
atm = kpa / 101.325
print("the pressure in pounds per square inch: %.2f psi" % (psi))
print("The pressure in millimeters of mercury: %.2f mmHg" % (mmhg))
print("Atmosphere pressure: %.2f atm." % (atm))


# 68. Write a Python program to calculate the sum of the digits in an integer.

# In[33]:


num = int(input("Input a four digit number: "))
x = num //1000
x1= (num- x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 -x2*10
print("The sum of digits in the number is", x +x1 + x2 + x3)


# 69. Write a Python program to sort three integers without using conditional statements and loops.

# In[34]:


x= int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a1 = min(x,y,z)
a3 = max(x,y,z)
a2= (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)


# 70. Write a Python program to sort files by date. 

# In[35]:


import glob 
import os

files = glob.glob("*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))


# In[ ]:




