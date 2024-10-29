# =================================================================
# =================================================================
# vs code shortcuts

# cmd + c = copy
# cmd + v = paste
# cmd + n = new file
# cmd + n = open file
# cmd + s = save
# cmd + / = comment and undo comment

# cmd + f = replace
# option + up/down = move whole line.
# option + cursor = multiple cursors.
# shift + option + down = copy line down
# =================================================================
# =======================================================================================
# ************************LIST Methods Built-In*** see lines around 420-440*************

# append()	Adds an element at the end of the list

# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value

# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position

# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list

# sort()	Sorts the list

# ***********************************SET Methods****************************************

# add()	               -> Adds an element to the set
# clear()	           -> Removes all the elements from the set
# copy()	           -> Returns a copy of the set
# difference()	       -> Returns set containing difference between two or more sets
# difference_update()  -> Removes items in set that are also included in another, specified set
# discard()	           -> Remove the specified item
# intersection()	   -> Returns set, that is the intersection of two other sets
# intersection_update()-> Removes the items in set that are not present in other, specified set(s)
# isdisjoint()	       -> Returns whether two sets have a intersection or not
# issubset()	       -> Returns whether another set contains this set or not
# issuperset()	       -> Returns whether this set contains another set or not
# pop()	               -> Removes an element from the set
# remove()	           -> Removes the specified element
# symmetric_difference()	    Returns set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	            -> Return set containing the union of sets
# update()	            -> Update the set with the union of this set and others

# *******************************Tuple Methods****************************************

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches tuple for specified value, returns the position where it was found

# ****************************Dictionary Methods**************************************

# clear()   	-->Removes all the elements from the dictionary
# copy()	    -->Returns a copy of the dictionary
# fromkeys()	-->Returns dictionary with the specified keys and value
# get()	        -->Returns the value of the specified key
# items()	    -->Returns list containing a tuple for each key value pair
# keys()	    -->Returns a list containing the dictionary's keys
# pop()	        -->Removes the element with the specified key
# popitem()	    -->Removes the last inserted key-value pair
# setdefault()	-->Returns value of the specified key. If key does not exist:
#                       insert the key, with specified value
# update()	    -->Updates the dictionary with the specified key-value pairs
# values()	    -->Returns a list of all the values in the dictionary

# ======================================================================================
# ----------------------------------------
# ***COLOR ASCII CODE***

# print("\033[91m red\033[0m")
# print("\033[92m green\033[0m")
# print("\033[95m pink \033[0m")
# print("\033[94m blue\033[0m")
# print("\033[93m yellow \033[0m")
# print("\033[91m blue\033[0m")
# ----------------------------------------
# ******SOME BUILT-IN FUNCTIONS*********

# print(sum([2,4,6,8])) # => 20
# print(len([2,4,6,8])) # => 4
# print(max([2,4,6,8])) # => 8
# print(min([2,4,6,8])) # => 2

# x = frozenset  ({"apple", "banana", "cherry"})
# a frozen set cannot be modified after it is created.
# print(x)
# ------------------------------------------------------
# name = 'ali'

# print((len(name)))              #----> 3
# print((name.find("l")))         #----> 1
# print((name.upper()))           #----> ALI
# print((name.capitalize()))      #----> Ali
# print((name.lower()))           #----> ali
# print((name.isdigit()))         #----> False
# print((name.isalpha()))         #----> True
# print((name.count("a")))        #----> 1
# print((name.replace("i","y")))  #----> aly
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# SOME MORE BUILT-IN FUNCTIONS

# name = 'micheal jackson'

# print(name.title())          #---> Micheal Jackson
# print(name.startswith("l"))  #---> False
# print(name.endswith("n"))    #---> True
# print(name.split(" "))       #---> ['micheal', 'jackson']
# print(name.count("a"))       #---> 2
# print(name.index("o"))       #---> 13
# print(name.find("i"))        #---> 1
# To append elements from another list to the current list, use the extend() method.
# ----------------------------------------------------------
# ==============================================================================
# ******PYTHON ARITHMETIC OPERATORS*********

# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y
# %	Modulus	x % y
# **	Exponentiation	x ** y
# //	Floor division	x // y
# --------------------------------------
# ******COMPARISON OPERATORS*********

# ==	Equal	      x == y
# !=	Not equal	  x != y
# >	    Greater than  x > y
# <	    Less than	  x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	    x <= y
# --------------------------------------
# ******LOGICAL OPERATORS*********

# and -> true if both are true else false
# or  -> onr or the other has to be true else false
# not -> reverse the result true >> false and false >> true.

# --------------------------------------------------
# ******MEMBERSHIP OPERATORS*********

# in       x in y     - if yes then true else false
# not in   x not in y - if yes then true else false

# -------------------------------------------------
# ******PYTHON BITWISE OPERATORS*********

#  & 	AND	Sets each bit to 1 if both bits are 1	            x & y
#  |	OR	Sets each bit to 1 if one of two bits is 1	        x | y
#  ^	XOR	Sets each bit to 1 if only one of two bits is 1.	x ^ y
#  ~	NOT	Inverts all the bits                                 ~x
#  <<	Zero fill left shift. Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2
#  >>	Signed right shift.Shift right by pushing copies of the leftmost bit
#             in from the left, and let the rightmost bits fall off	x >> 2

# -------------------------------------------------
# ******PYTHON OPERATORS PRECEDENCE ORDER*********

# |  ()	Parentheses
# |  **	Exponentiation
# |  +x  -x  ~x	Unary plus, unary minus, and bitwise NOT
# |  *  /  //  %	Multiplication, division, floor division, and modulus
# |  +  -	Addition and subtraction
# |  <<  >>	Bitwise left and right shifts
# |  &	Bitwise AND
# |  ^	Bitwise XOR
# |  |	Bitwise OR
# |  ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators
# |  not	Logical NOT
# |  and	AND
# |  or	OR

# -------------------------------------------------
# Customize Sort Function

# Sort the list based on how close the number is to 50:
# def func(n):
#   return abs(n - 50)

# list = [100, 50, 65, 82, 23]
# list.sort(key = func)
# print(list)

# =========================
# Keyword-Only Arguments
# def my_function(*, x):

# Positional-Only Arguments
# def my_function(x, /):

# =========================
# =============================
# Escape Characters

# |  \'	   Single Quote
# |  \\	   Backslash
# |  \n	   New Line
# |  \r	   Carriage Return
# |  \t	   Tab
# |  \b	   Backspace
# |  \f	   Form Feed
# |  \ooo   Octal value
# |  \xhh   Hex value
# =============================
# ==================================================
# | ****************Built-in Data Types*************

# | Variables can store data of different types,
# |   and different types can do different things.
# | Python has the following data types built-in:

# | Text Type:	    str
# | Numeric Types:	int, float, complex
# | Sequence Types:	list, tuple, range
# | Mapping Type:	dict
# | Set Types:	    set, frozenset
# | Boolean Type:	bool
# | Binary Types:	bytes, bytearray, memoryview
# | None Type:	    NoneType
# ==================================================
# ******************RULES***************************

# |VARIABLES:
# | Variable names are case-sensitive.((age, Age and AGE are three different)
# | A variable name must start with a letter or the underscore character
# | A variable name cannot start with a number
# | A variable name cannot be any of the Python keywords.
# |
# | Camel Case:>>> myVariableName = "John"
# | Each word, except the first, starts with a capital letter:
# |
# | Pascal Case>>> MyVariableName = "John"
# | Each word starts with a capital letter:
# |
# | *Snake Case:>>> my_variable_name = "John"
# | Each word is separated by an underscore character:

# ===========================================================================================================================
# ***Python String Methods Built-In ***

# capitalize()	  --> Converts first character to upper case
# casefold()	  --> Converts string into lower case
# center()	      --> Returns centered string
# count()	      --> Returns the number of times a specified value occurs in string

# encode()	      --> Returns an encoded version of the string
# endswith()	  --> Returns true if string ends with the specified value
# expandtabs()	  --> Sets the tab size of the string

# find()	      --> Searches string for specified value, returns the position of where it was found
# format()	      --> Formats specified values in a string
# format_map()	  --> Formats specified values in a string

# index()	      --> Searches the string for a specified value, returns the position of where it was found
# isalnum()	      --> Returns True if all characters in the string are ->alphanumeric
# isalpha()	      --> Returns True if all characters in the string are ->in the alphabet
# isascii()	      --> Returns True if all characters in the string are ->ascii characters
# isdecimal()	  --> Returns True if all characters in the string are ->decimals
# isdigit()	      --> Returns True if all characters in the string are digits
# isidentifier()  --> Returns True if the string is an identifier
# islower()	      --> Returns True if all characters in the string are lower case
# isnumeric()	  --> Returns True if all characters in the string are numeric
# isprintable()	  --> Returns True if all characters in the string are printable
# isspace()	      --> Returns True if all characters in the string are whitespaces
# istitle()	      --> Returns True if the string follows the rules of a title
# isupper()	      --> Returns True if all characters in the string are upper case

# join()	      --> Converts the elements of an iterable into a string

# ljust()	      --> Returns a left justified version of the string
# lower()	      --> Converts string into lower case
# lstrip()	      --> Returns a left trim version of the string

# maketrans()	  --> Returns a translation table to be used in translations
# partition()	  --> Returns a tuple where the string is parted into three parts

# replace()	      --> Returns a string where specified value is replaced with a specified value
# rfind()	      --> Searches the string for a specified value and returns the last position of where it was found
# rindex()	      --> Searches the string for a specified value and returns the last position of where it was found
# rjust()	      --> Returns a right justified version of the string
# rpartition()	  --> Returns a tuple where the string is parted into three parts
# rsplit()	      --> Splits the string at the specified separator, and returns a list
# rstrip()	      --> Returns a right trim version of the string

# split()	      --> Splits the string at the specified separator, and returns a list
# splitlines()	  --> Splits the string at line breaks and returns a list
# startswith()	  --> Returns true if the string starts with the specified value
# strip()	      --> Returns a trimmed version of the string
# swapcase()	  --> Swaps cases, lower case becomes upper case and vice versa

# title()	      --> Converts the first character of each word to upper case
# translate()	  --> Returns a translated string
# upper()	      --> Converts a string into upper case
# zfill()	      --> Fills the string with specified number of 0 values at the beginning
# ===========================================================================================================================


"""
###===========================START==============================###
print("\n------------------------------")
name = 'ali'
age = 34
print(name)
print(age)

#better way is less lines of code.
name, age = "ali", 32
print(name +"\n"+ str(age))

your_name =input("please enter your name: ")
print("hi "+your_name)

num1,num2 = input("enter num1:"), input("enter num2:")
sum = int(num1) + int(num2)
print(sum)
print("------------------------------\n")
#calculator mine
print("\n------------------------------")

options = None
result = None

while True:
    options = input("Enter what u want add subtract divide or multiply. or q to quit. ")
   
    try:
       num1,num2 = int(input("Enter num1: ")), int(input("Enter num2: "))
       
    except ValueError:
       print("Please enter numeric value.")
       continue
    
    if options == "a":
      result = num1 + num2
      break

    elif options == "s":
      result =  num1 - num2
      break
    
    elif options == "d":
        if num2 != 0:
            result =  num1 / num2
        else:
            print("result cannot be divided.")
        break
    
    elif options == "m":
       result =  num1 * num2
       break
    else:
        print("Invalid operation. Please enter 'a', 's', 'd', 'm', or 'q'.")
        continue

print("result: "+str(("{:.3f}".format(result))))

print("------------------------------\n")

print("\n------------------------------")

#print(135//23) #divide rounding down
#print(2**3) # expo
#print(67%6) #gives remainder

food_amount = float(input("Enter food amount: "))           
tip_percentage = float(input("Enter tip percentage: "))
tip_percentage = tip_percentage/100

tip_amount = food_amount * tip_percentage
total_amount = tip_amount + food_amount

print("Tip: "+str("{:.2f}".format(tip_amount))+"$")
print("Amount: "+str(food_amount)+"$")
print("Total with tip: "+str("{:.2f}".format(total_amount))+"$")

print("------------------------------\n")
#print("\n------------------------------")

# # weather = input("how's the weather today?: ")

# # if weather == "rain":
# #     print("Umbrella")
# # elif weather == 'cloudy':
# #     print("cloud")
# # elif weather == 'thunder':
# #     print("lighting ")
# # else:
# #     print("Sunglasses.")

# print(type(45))        == int
# print(type('fef'))     == str
# print(type(45.34))     == float
# print(type(True))      == bool

print("\n------------------------------")

print("------------------------------\n")
def score(marks):

    if 90<=marks<101:
        return ("Wow! You got an A.\n")
    elif 80<=marks<90:
        return (" You got an B.\n")
    elif 70<=marks<80:
        return ("You got an C.\n")
    elif 60<=marks<70:
        return ("You got an D.\n")
    elif 50<=marks<60:
        return ("You got an E.\n")
    elif 0<=marks<50:
        return ("Sorry. you failed.\n")
    else:
        return ("Please enter valid marks out of 100.\n")

def run():
    while True:y

       try:
           marks = int(input("Please enter your marks: "))
           print(score(marks))
       except ValueError:
          User_input = input("please enter a numeric value \n unless u want to quit press 'q'.\n")
          if User_input.lower() == 'q':
            break
          else:
            continue
run()
print("------------------------------\n")

print("\n------------------------------")

# def sum(num1, num2: int) -> int:
#     return num1+num2
# print(sum(1,3))
# sum2= lambda a, b:a+b
# print(sum2(4,5))
# greet = lambda greet,name:f"{greet},{name}"
# print(greet('hii','ali'))

while True:
    def Bigger_Guy(num1: int,num2: int) -> int:

        if num1>num2:
           return num1 
        else:
           return num2
   
    print(Bigger_Guy(num1 = int(input("enter num1: ")), num2 = int(input("enter num1: "))))

#***  above code can be written in these two lines below more effective. use lambda.
#Bigger_guy = lambda num1,num2: num1 if num1>num2 else num2
#print(Bigger_guy(num1 = int(input("enter num1: ")), num2 = int(input("enter num1: "))))

#this code below is a shorter version of the code above.
# while True:
#     try:
#         Bigger_guy = lambda num1,num2: num1 if num1>num2 else num2
#         result = print(Bigger_guy(num1 = int(input("enter num1: ")), num2 = int(input("enter num1: "))))
#     except ValueError:
#         print("enter numerics")
#         user = input("or enter 'q to quit")
#         if user == 'q':
#             break

print("------------------------------\n")
# assert testing code
print("\n------------------------------")

sum = lambda a, b: a + b
# print(sum(1,2))

assert sum(1, 2) == 3, "\033[91m sum(1,2) does not return 3 like it should."
assert sum(1, -4) == -3, "\033[91m sum(1,-4) does not return -3 like it should."
assert sum(1, 24) == 25, "\033[91m sum(1,24) does not return 25 like it should."
print("\033[92m Sum function: all test passed (3/3).\033[0m")

print("------------------------------\n")

print("\n------------------------------")
#calculator using lambda
def sum():
    sum = lambda num1, num2: num1+num2
    print(sum(num1=int(input("enter num1:")), num2=int(input("enter num1:"))))

def subtract():
    subtract = lambda num1, num2: num1 - num2
    print(subtract(num1=int(input("enter num1:")), num2=int(input("enter num1:"))))

def multiply():
    multiply = lambda num1, num2: num1 * num2
    print(multiply(num1=int(input("enter num1:")), num2=int(input("enter num1:"))))

def divide():
    divide = lambda num1, num2: num1 / num2 if num2 > 0 else "try again"
    print(divide(num1=int(input("enter num1:")), num2=int(input("enter num1:"))))

while True:
    
    choices = input("enter what you want to do? a)add s)subtract m)multiply or d)divide.")

    if choices == 'a':
        sum()
    elif choices == 's':
        subtract()
    elif choices == 'm':
        multiply()
    elif choices == 'd':
        divide()
    else:
        print("please enter valid choices values")
#=========================
# def operations(add_f,sub_f):

#     def add(num1,num2):
#         return num1+num2

#     def sub(num1,num2):
#         return num1-num2
   #line above can be written as line below.     
#      add = lambda num1,num2 : num1+num2
#      sub = lambda num1,num2 : num1-num2

#     print(add(1,8))
#     print(sub(20,5))

# operations(0,0)
#=========================
print("------------------------------\n")

print("\n------------------------------")
# list = []
# set = {}
# tuple = ()
# DICTIONARIES {}

#------------------------------------------------------------------------------------
# There are four collection data types in the Python programming language:

# List is collection which is ordered and changeable. Allows duplicate members.
# Tuple is collection which is ordered and unchangeable. Allows duplicate members.
# Set is collection which is unordered, unchangeable*, and un indexed. No duplicate members.
# Dictionary is collection which is ordered** and changeable. No duplicate members.
#   list and sets are opposite 
#
#------------------------------------------------------------------------------------
#**********************
tuple = ("apple",)
print(type(tuple))

#NOT a tuple
tuple = ("apple")
print(type(tuple))
#**********************

# .append(element)
# .pop(index)
# .remove(element)
# .insert(index, element)

# list_name[-index] gives the index of element
# del list_name [index]
# number = [1,2,3,4,5,6,7,8,9,0]
# number.append(20)
# number.remove(1)
# print(number[-3])
# `del number[2]` is deleting the element at index 2 in the list `number`.
# number.pop(8)
# number.insert(0,34)

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# # slicing
# # print(number[0:9])
# # print(len(number))  # gives the length of the array

# name = "micheal jackson"

# print(len(name))
# print(len(name[0:15:2])) #it ::x this skips the elements and prints the rest.
# reversing
# print(name[::-2]) #it reverses and also skips 2 steps

# name_num = [1,2,3,4,'micheal',3.4]

# # print(name_num)
# integers = [ ]
# floats = [ ]
# strings = [ ]
# #separates different types
# for element in name_num:
#     if isinstance(element, int):
#         integers.append(element)
#     elif isinstance(element, float):
#         floats.append(element)
#     elif isinstance(element, str):
#         strings.append(element)

# print("integers: ",integers)
# print("float: ",floats)
# print("strings: ",strings)

print("\n------------------------------")

# dictionaries: and lists are ordered in py 3.8 or later
# # key value pairs
# person = {"name": "ali"}
# print(person["name"])

# print("your name is {name} and you are {age} years old with {car}".format_map(details))


# person = {
#     "name": "ali",
#     "age": "10",
#     "laptop": "apple"
#     }
# print("Value for key 'laptop':", person["laptop"])

# def intro():
#     person = {
#     "name": "Ali",
#     "shirts": "Black",
#     "laptop": "Apple"
#     }

#     print(f"\033[96mHi my name is \033[3m{person['name']} ,I am wearing {person['shirts']} shirt,\nand the laptop i have is {person['laptop']}.\033[0m")

# intro()
#function
# def Net_worth():
#     person  = {
#      'name': 'ali',
#      'asset': 500,
#      'debt': 2000,
#      'net_worth': lambda: person['asset'] - person['debt']
#     }
person['name'] = 'ali' #you can assign or update dictionary
#     print(f"\033[94mHii. My name is {person['name']} and my net Net_worth is ${person['net_worth']()}. \033[0m")
# Net_worth()

# print(list(person.values())) # will print all values
# print(list(person.keys()))   # will print all keys

#  x=this_dict.keys() #this will get all the keys.
#  x=this_dict.values() #this will get all the values.
#  print(x)

print("------------------------------\n")
print("\n------------------------------")
#tuples(): are unchangeable or cannot be updated

number = (1,3)
print(number)
print(type(number))
 
print("------------------------------\n")
print("\n------------------------------")
#set: how to convert list=>set so u don't get duplicate elements or get unique items

# programming_lang1 = ['python','c','ruby','java']
# programming_lang2 = ['python','js','c','C++']

# #unique languages aka no duplicates
# programming_language = set(programming_lang1+programming_lang2)

# print(programming_language)

#my example below but can be written as fewer lines of code.

# def unique():

#     programming_list = ['python','js','c','C++','python','js','c','C++']

#     programming_list = set(programming_list)
#     programming_list = list(programming_list)

#     print(programming_list)

# unique()
#========================================
#This both functions does the exact same thing as above one but is written in fewer lines of code.
def unique(languages): return list(set(languages))
print(unique(['python','js','c','C++','python','js','c','C++']))

unique = lambda languages: list(set(languages))
print(unique(['python','js','c','C++','python','js','c','C++']))

print("------------------------------\n")
print("------------------------------\n")
# loops: for loops and while loops
# enumerate() = takes a collection (eg a tuple) and returns it as an enumerate object.
# the enumerate() function adds a counter as the key of the enumerate object.(Basically adds a counter.)

# This code snippet is using a for loop with the `enumerate()` function to iterate over a list of
# programming languages.

languages = ["python", "js", "c", "C++", "python", "js", "c", "C++"]

languages.append("go")
languages.append("maple")
languages += ["oye"] * 3  # this is how you print line 5 times. and append at the same time

for index, i in enumerate(languages):
    
    print(index, "->", i)
print("length of array:", len(languages))

#apple = ["apple"]

# for _ in range(10):
#     print(apple)
#     apple.append("apple")

# ali = 'standing'
# while ali != 'sitting':
#     print("ali if standing")
#     break

# counter = 0
# while counter<=10:
#     print(counter)
#     counter += 1

print("------------------------------\n")
print("\n------------------------------")
# exercises:1================================================

# num = [53, 34, 6, 6, 4, 7, 46, 34]
# result = []

# def double(num):
#     for i in num:
#         result.append(i * 2)
#     return result

# print(double(num))
# exercises:2================================================

sum_list = [3, 3, 4, 4, 23, 42]

def sum(sum_list):
    counter = 0
    for i in sum_list:
        counter += i
    return counter

sum_all = sum(sum_list)
print("\033[95mSum of list: ", sum_all, "\033[0m")

print("------------------------------\n")
# exercise 3========================================
# print("\n------------------------------")

# num = [1, 4, 6, 9, 23, 443, 34, 34, 3, 4]

# def max_num(num):
#     new_max = num[0]
#     for i in num:
#         if i > new_max:
#             new_max = i
#     print(new_max)
#print(max([1, 4, 6, 9, 23, 443, 34, 34, 3, 4])) this line of code is same as above except that it is a built in function
# max_num(num)
#return min ==================================
print("\n------------------------------")
num = [ 9,4, 6, 5,345,346,4,64,5,1,4]

def min_num(num):
    new_min = num[0]
    for i in num:
        if new_min > i:
            new_min = i
    print(new_min)
min_num(num)
                                        
print("------------------------------\n")
# dictionaries practice
# print("\n------------------------------")
# phrase = "I am Spiderman because Spiderman is a hero because he is good."

# def freq(phrase):
#     result = {}
#     words = phrase.split(" ")
#     for i in words: # 'I', 'am'
#         if i not in result:
#             result[i] = 1
#         else:
#             result[i] += 1
#     return result
# print(freq(phrase))
                                    
#comments
#  to count words from given phrase
# make convert the phrase or string to a list like['word', 'phrase'] by using the split(' ') function that is used when u need to skip an element
# create an empty dictionary name it result = {} 
#  make a loop that check the element in list ,if it already exist in result which should be at least one 
# if words exist in result then result = result +1
# return result
# call the  function def whatever.
# print("------------------------------\n")
print("\n------------------------------")
#High order function: map and filter

#1 filter(): the filter method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
numL = [1, 2, 3, 4, 5, 6, 5, 4, 457, 6, 7, 6, 2]

print("even:",list(filter(lambda even: even % 2 == 0, numL)))
print([num for num in num if num%2==0])#same as above

print("odd:",list(filter(lambda odd: odd % 2 == 1, numL)))
print([num for num in num if num%2==1])#same as above

print(list(map(lambda num:num*2,[1,3,5]))) #this is just one line of code doing the exact same thing as code lines below

#2============================================
# def double_num(num):
#     return num*2

# print(list(map(double_num,[1,3,5])))
#3=============================================
#exercise 1 above on line:425
# num = [53, 34, 6, 6, 4, 7, 46, 34]
# result = []

# def double(num):
#     for i in num:
#         result.append(i * 2)
#     return result

# print(double(num))
#======================================
print("\n------------------------------")

# num = (5,6,9,3,4,324,32,4,3,4,23)
# list1 = []

# for i in num:
#     square = lambda num: i*i
#     list1.append(square(num))

# print(list1)
# import math
# print(list(map(lambda num:num*num,[5,6,4,23])))                   # squares the nums provided -|
print(list(map(lambda num:num**2,[5,6,4,23])))                      # squares the nums provided -|
# print(list(map(lambda num: math.sqrt(num),[16,36,81,25,144])))    # under root of nums provided

print("------------------------------\n")
print("------------------------------\n")
#calculator one more time

while True:
    try:
        num1 = input("\033[0m enter num1:")
        print(num1)

        num2 = input("enter num2:")
        print(num2)
    except:
        print("please enter a Numeric value.")

    option = input(
        "<Q>Now what do u want to do \n\033[94m<>press (a) for addition  \n\033[95m<>press (s) for subtraction \n\033[96m<>press (m) for multiplication \n\033[93m<>press (d) for division.\n\033[0m \n:? "
    )
    try:
        if option == "a":
            print(
                "add:\033[92m ",
                list(map(lambda num1, num2: num1 + num2, [int(num1)], [int(num2)])),
            )
        elif option == "s":
            print(
                "subtract:\033[92m",
                list(map(lambda num1, num2: num1 - num2, [int(num1)], [int(num2)])),
            )
        elif option == "m":
            print(
                "multiply:\033[92m",
                list(map(lambda num1, num2: num1 * num2, [int(num1)], [int(num2)])),
            )
        elif option == "d":
            try:
                print(
                    "divide:\033[92m",
                    list(map(lambda num1, num2: num1 / num2, [int(num1)], [int(num2)])),
                )
            except:
                print("\033[91mPlease enter number greater than 0.\033[0")
        else:
            break

    except:
        print("\033[91mPlease enter a numeric value.\033[0m")
print("------------------------------\n")
print("\n------------------------------")
# list comprehensions.***
# num = [1,2,3,4,5,6,7,8,9,0]
# print([num for num in num if num%2==1])


double = [1,2,3,4,5,6,7,8,9,0]
print([all * 2 for all in double if all > 0])               #prints all nums 
print([even * 2 for even in double if even % 2 == 0])       #print all even numbers after multiply by 2
print([odd * 2 for odd in double if odd % 2 == 1])          #print all odd numbers after multiply by 2
print([even*even*even for even in double if even >0])       #print all even numbers after getting their cube **3 
print([even**3 for even in double if even >0])              #same thing as above

#          ========        ***Using list comprehension is generally easier than using .map() and filter() methods.*** =======

print("------------------------------\n")
# print("\n------------------------------")
# #**  walrus operator :=  **

# foods = list()
# while True:
#     food = input("What food do you like?:")
#     if food == "quit":
#             break
#     foods.append(food)
# #below one is more effective.
    
# foods = list()
# while food := input("What food do you like?: ") != "quit":
#       foods.append(food)

# # Without walrus operator
# data = [1, 2, 3, 4, 5]
# squared_numbers = []
# for item in data:
#     squared = item ** 2
#     squared_numbers.append(squared)
# print(squared_numbers)

# # With walrus operator
# data = [1, 2, 3, 4, 6]
# squared_numbers = print([squared for item in data if (squared := item ** 2)])

#no walrus used see below
# num= (1,2,3,4,5,6,7,8,9,0)
# result =[]
# def double(num):
#     for i in num:
#         j = i*2
#         result.append(j)
#     return result    
# print(double(num))

# num= (1,2,3,4,5,6,7,8,9,0)
# result = print([i*2 for i in num])
#examples:
#num= (1,2,3,4,5,6,7,8,9,0)
#result = print([num for i in num if (num := i*2)])
#
##examples:
#even= (1,2,3,4,5,6,7,8,9,0)
#result = print([i for i in even if (even := i%2==0)])
##examples:
#odd= (1,2,3,4,5,6,7,8,9,0)
#result = print([i for i in odd if (odd := i%2==1)])
                                        
#print("------------------------------\n")
#---------------------------------- 
phone_num = "453-545-4593 "

for i in phone_num:
    if i == "-":
        continue
    print(i,end="")
#----------------------------------  
phone_num = "453-545-4594"
numbers = []
for i in phone_num:
    numbers.append(i)
just_numbers = [i for i in numbers if i != "-"]

combined = "".join(just_numbers)
result = int(combined)

print(result)

#print(type(i))        #<class 'str'>
#print(type(result))   #<class 'int'>
#---------------------------------- 
print("\n------------------------------")

# r = int(input("enter num of rows:"))

# for i in range(0,n):
#     for j in range(0,i+1):
#         print("\033[95m*",end="")
#     print("\r")
# =========same both up and down
# my_List =[]
# for i in range(1,n+1):
#     my_List.append("*"*i)
#print("\n".join(my_List))

print("------------------------------\n")

print("\n------------------------------")
#*** Recursion -> It means that a function calls itself ***

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

print("------------------------------\n")

print("\n------------------------------")
# **** Python Classes and Objects ****important

# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like a "blueprint" for creating objects.

# # creating an class
# class My_class:
#     students = 30

# #now we can create an object

# school = My_class()
# print(school.students)

# The __init__() Function
# Examples above are classes and objects in simplest form.not useful in that form.
# To understand class -> the built-in __init__() function.
# All classes have a function __init__(), which is always executed when class is initiated.
# Use the __init__() function to assign values to object properties, or other operations
#    that are necessary to do when the object is being created:
    
class Person:
    def __init__(self, name,age ):
        self.name = name
        self.age = age
    
p1 = Person("hamza",23)
p2 = Person("ahmed",3)
p3 = Person("ali",20)
p4 = Person("jake",29)
p5 = Person("sheikh",43)

print(f"{p1.name}:{p1.age}")
print(f"{p2.name}:{p1.age}")
print(f"{p3.name}:{p1.age}")
print(f"{p4.name}:{p1.age}")
print(f"{p5.name}:{p1.age}")
#-----------------------------------------------
    #*** __str__() *** 

# The __str__() function controls what should be returned
#            when the class object is represented as a string.
# If the __str__() function is not set, the string 
#                 representation of the object is returned:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 32)
print(f"{p1.name}:{p1.age}")
#-----------------------------------

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"name = {self.name}: age = {self.age}"

p1 = Person("John", 32)
print(p1)
                                       
print("------------------------------\n")

print("\n------------------------------")

#OBJECTS Methods:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def func(self):
    print("Hello my name is " + self.name)
    print(f"and i'm {self.age} years old")

p1 = Person("ali",20)
p1.func()
print("\n------------------------------")

print("\n------------------------------")
#*** Inheritance *** important
#--------------------------------------------
#do this important
# Accessing attributes using __dict__
# attributes = x.__dict__

# # Printing attributes
# print("Attributes of x:", attributes)
#---------------------------------------------

# Inheritance allows us to define a class that 
#       inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.
# Child class is class that inherits from another class, also called derived class.

class Person:
    def __init__(self, fname,lname):
        self.firstname  = fname #these are the attributes i.e first name
        self.lastname  = lname
    def print_name(info):
        print(info.firstname,info.lastname)

x = Person("M","Ali ")
x.print_name()


class Student(Person):
    def __init__(self, fname ,lname ,year):
        super().__init__( fname,lname)
        self.graduation_year = year
       
    def print_info(info):
        print(info.firstname,info.lastname,info.graduation_year)

x = Student("m","ali",2024)

print(x.graduation_year)
print(x.firstname)
x.print_info()

print("\n********Attributes************")
attributes = x.__dict__
for key, value in attributes.items():
    print("\033[95m" + key + "\033[0m")
print("******************************\n")

print("\n------------------------------")

#***PRACTICE:***
print("------------------------------\n")

class Animal:

    def __init__(self, alive=True, legs=4, tail=1, sounds="moye moye"):
        self.alive = alive
        self.legs = legs
        self.tail = tail
        self.sounds = sounds
# ---------------------------------------------------------
class Lion(Animal):
    def __init__(self, alive, legs, tail, sounds):
        super().__init__(alive, legs, tail, sounds)


pet_lion = Animal(True, 4, 1, "roar")

print(
    f'\033[92mThis animal is the know as the king of the jungle, yes the "lion". \nIt was found {pet_lion.alive}',
    f'it has {pet_lion.legs} legs and {pet_lion.tail} tail and makes sounds like these "{pet_lion.sounds}." ',
)
# ---------------------------------------------------------
class dog(Animal):
    def __init__(self, alive, legs, tail, sounds):
        super.__init__(alive, legs, tail, sounds)

pet_dog = Animal(False, 3, 1, "bhao bhao")

print(
    f"\n\033[93mThis animal is known as dog, the sound it makes is called {pet_dog.sounds} ",
    f"\nalso has same {pet_dog.legs} legs and is {pet_dog.alive}",
    f"\nand also has {pet_dog.tail} tail."
)
# ---------------------------------------------------------
class cat(Animal):
    def __init__(self, alive, legs, tail, sounds):
        super.__init__(alive, legs, tail, sounds)


pet_cat = Animal(True, 4, 1, "meow meow")

print(
    f"\n\033[95mThis animal is known as cat, the sound it makes is called {pet_cat.sounds} ",
    f"\nand has same {pet_cat.legs} legs and is {pet_cat.alive}",
    f"\nand also has {pet_cat.tail} tail."
)
# ---------------------------------------------------------
class kangaroo(Animal):
    def __init__(self, alive, legs, tail, sounds=None, herbivore=""):

        super().__init__(alive, legs, tail, sounds)
        self.herbivore = herbivore

pet_kangaroo = kangaroo(True, 2, 1, "no sounds🤐")

print(
    f"\n\033[91mThis animal is known as kangaroo, it dose not make a sound {pet_kangaroo.sounds} ",
    f"\nand has same {pet_kangaroo.legs} legs and is {pet_kangaroo.alive}",
    f"\nand also is a{pet_kangaroo.herbivore} herbivore.\033[0m"
)

print("------------------------------\n")

print("\n------------------------------")

import datetime

x = datetime.datetime.now()

print(x)
print(x.strftime("%A"))
print(f"{x.day}/{x.month}/{x.year} ")
print(x.date())
print(x.astimezone())#**important
print(f"{x.hour}:{x.minute}:{x.second}")

x = datetime.datetime(2018, 2, 1)
print(x.strftime("%B"))


#| %a	Weekday, short version	Wed	
#| %A	Weekday, full version	Wednesday	
#| %w	Weekday as a number 0-6, 0 is Sunday
#| %d	Day of month 01-31	31	
#| %b	Month name, short version	Dec	
#| %B	Month name, full version	December	
#| %m	Month as a number 01-12	12	
#| %y	Year, short version, without century
#| %Y	Year, full version	2018	
#| %H	Hour 00-23	17	
#| %I	Hour 00-12	05	
#| %p	AM/PM	PM	
#| %M	Minute 00-59	41	
#| %S	Second 00-59	08	
#| %f	Microsecond 000000-999999	548513	
#| %z	UTC offset	+0100	
#| %Z	Timezone	CST	
#| %j	Day number of year 001-366	365	
#| %U	Week number of year, Sunday as the first day of week, 00-53	52	
#| %W	Week number of year, Monday as the first day of week, 00-53	52	
#| %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
#| %C	Century	20	
#| %x	Local version of date	12/31/18	
#| %X	Local version of time	17:41:00	
#| %%	A % character	%	
#| %G	ISO 8601 year	2018	
#| %u	ISO 8601 weekday (1-7)	1	
#| %V	ISO 8601 week number (01-53)

print("------------------------------\n")

print("\n------------------------------")
#********** Python JSON*********

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

import json

# If you have a JSON string, you can parse 
# it by using the json.loads() method.
#-----------------------------------------------
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#-----------------------------------------------

# a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)

# You can convert Python objects of the following types 6, into JSON strings:

# dict     #int
# list     #float
# tuple    #True anf false
# string   #None

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))
#-----------------------------------------------
print("------------------------------\n")

print("\n------------------------------")

# ************************ File Handling *******************************************

# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.

# "r" - Read - Default value. Opens file for reading, error if file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# f = open("/Users/ali/PYTHON/demo file.txt","a")
# f.write("now the file has more content!\n")
# f.close()

# f = open("/Users/ali/PYTHON/demo file.txt","r")
# print(f.read())

# To delete a file, you must import the OS module,
# and run its os.remove() function:

# import os
# os.remove("demo file.txt")


# To delete an entire folder, use the os.rmdir() method:

# Remove the folder "folder":

# import os
# os.rmdir("folder")

print("------------------------------\n")"""

# ************************will continue end till now all basic are covered.*****************


# ********************* QUOTES ************************
# Create a dictionary, using the List items as keys.
# This will automatically remove any duplicates because
# dictionaries cannot have duplicate keys.(use/make a function)

































print("\033[95m\n------------------------------")


def binary(num_sorted,target_value):

    left =0
    right = len(num_sorted) -1

    while left<=right:
        mid = (left+right)//2

        if num_sorted[mid] ==target_value:
            return mid
        if num_sorted[mid] <target_value:
            left = mid +1
        else :
            right =mid-1

    return -1
target_value =67

num = [23,4,23,5,6,57,6,7,67,3,45,23,4,23,53,4,67]

num_sorted = sorted(num)
num_sorted_set = sorted(set(num))

result = binary(num_sorted,target_value)
result_set = binary(num_sorted_set,target_value)


print("target value:",target_value)
print(num_sorted)

if result != -1:
    print("found at index:",result)
else:
    print("not found.")


print(num_sorted_set)

if result_set != -1:
    print("found at index:",result_set)
else:
    print("not found.")

print("found at:",num_sorted.index(67))








print("\n------------------------------\n\033[0m")


























# hope this works
# hope this works
# hope this works
