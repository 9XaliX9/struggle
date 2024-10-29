
"""
#2     variables ✘
#3     multiple assignment 🔠
#4     string methods 〰️
#5     type cast 💱
#6     user input ⌨️
#7     math functions 🧮
#8     string slicing ✂️
#9     if statements 🤔
#10    logical operators 🔣
#11    while loops 🔄
#12    for loops ➰
#13    nested loops ➿
#14    reak continue pass ⛔
#15    lists 🧾
#16    2D lists 📜
#17    tuples 📄
#18    sets 🍴
#19    dictionaries 📖
#20    indexing 📑
#21    functions 📞
#22    return statement 🔙
#23    eyword arguments 🔑
#24    nested function calls 🖇️
#25    variable scope 🔬
#26    *args 📦
#27    **kwargs 🎁
#28    string format 💬
#29    random numbers 🎲
#30    exception handling ⚠️
#31    file detection 📁
#32    read,write,copy,move,delete a file 🔍
#37    modules 💌
#38    rock, paper, scissors game 🗿
#39    quiz game 💯
#40    Object Oriented Programming (OOP) 🐍
#41    class variables 🚗
#42    inheritance 👪
#43    multilevel inheritance 👴
#44    multiple inheritance 👨‍👩‍👧‍👦
#45    method overriding 🙅
#46    method chaining ⛓️
#47    super function 🦸
#48    abstract classes 👻
#49    objects as arguments 🏍️
#50    duck typing 🦆
#51    walrus operator 🦦
#52    functions to variables 📛
#53    higher order functions 👑
#54    lambda λ
#55    sort 🗄️
#56    map 🗺️
#57    filter 🍺
#58    reduce ♻️
#59    list comprehensions 📰
#60    dictionary comprehensions 🕮
#61    zip function 🤐
#62    if name == '__main__' ❓
#63    time module ⌚
#64    threading 🧵
#65    daemon threads 😈
#66    multiprocessing ⚡
#67    GUI windows 🖼️
#68    labels 🏷️
#72    radio buttons 🔘
#73    scale 🌡️
#74    listbox 📋
#75    messagebox 💭
#76    colorchooser 🎨
#77    text area 📒
#78    open a file (file dialog) 📁
#79    save a file (file dialog) 💾
#80    menubar 🧾
#81    frames ⚰️
#82    new windows 🗔
#83    window tabs 📑
#84    grid 🏢
#85    progress bar 📊
#86    canvas 🖍️
#87    keyboard events ⌨️
#88    mouse events 🖱️
#89    drag & drop 👈
#90    move images w/ keys 🏎️
#91    animations 🛸
#92    multiple animations 🎞️
#93    clock program 🕒
#94    send an email 📧
#95    run with command prompt 👨‍💻
#96    pip 🏗️
#97    py to exe 🏃
#98    calculator program 🖩
#99    text editor program ✏️
#100   tic tac toe game 
#101   snake game 🐍

#============================================================================================

# (print statemnts)==========================================================================
print("\n------------------------------")
print("i love pizza")
print("it's good")
print("------------------------------\n")
# (variables)=================================================================================
print("\n------------------------------")
name = "Ali " 
age = (str)(input("enter your age\n"))
print("hello "+name)
print("you are "+str(age) +" years old.")
print("------------------------------\n")
# (boolean)=================================================================================
print("\n------------------------------")
human = False
print(type(human))
print("------------------------------\n")
# (multiple assignments)====================================================================
print("\n------------------------------")
person = name,age,attractive = "ali",21,True
print(attractive)
print("------------------------------\n")
# (multiple assignments)=====================================================================
print("\n------------------------------")
name = "ali"
#print(len(name))
#print(name.find("l"))
#print(name.upper())
#print(name.capitalize())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("a"))
#print(name.replace("i","y"))
print("------------------------------\n")
# (type casting)============================================================================
print("\n------------------------------")
x = 5
y = 3.43
z = "3"
x = float(x)
y = float(y)
z = float(z)
print(x)
print(y)
print(z*3)
print("------------------------------\n")
# (inputs)=================================================================================
print("\n------------------------------")
name = input("what is your name?  ")
age = input("how old are you?: ")
height_inch = float(input("what is your height in inch?:"))
age = int(age) + 1
height_foot = height_inch/12
print("Hello " + name.capitalize())
print("You will be " + str(age) + " next year")
print("Your height is "+ str(height_inch) +" in inches and "+str(round(height_foot,3))+" in feets")
print("------------------------------\n")
# (maths)=================================================================================
import math
print("\n------------------------------")

pi = 3.213

print (round(pi))
print (math.ceil(pi))
print (math.floor(pi))
print (abs(pi))
print (round(pow(pi,3),3))
print (math.sqrt(pi))
x=3
y=69
z=20
print(max(x,y,z))
print(min(x,y,z))
print("------------------------------\n")
# (slicing strings)================================================================================
print("\n------------------------------")

full_name = "codinerr iss good "

first_name = full_name[:-11]
mid_name = full_name[9:-6]
last_name = full_name[13:-1]

reversed_name = full_name[-2::-1]

print(first_name)
print(mid_name)
print(last_name)
print(reversed_name)
print("------------------------------\n")

website = "http://www.google.com"
slice = slice(11,-4)
print(website[slice])
# ()================================================================================
print("\n------------------------------")
age = int(input("how old are you?"))

if age>18:
    print("you are of legal age.")
elif age == 65:
    print("you are retired")
elif age<18:
    print("not legal age for drinking")
else:
    print("enter number only")
print("------------------------------\n")
# ()================================================================================

print("\n------------------------------")
temp = int(input("what is the temp outside:\n"))

if temp >= 0 and temp <= 30:
    print("it is good outside")
#elif temp<=0 or temp>=30:
 #   print("it is extreme outside")
elif not (temp >= 0 and temp <= 30):
    print("bad")
print("------------------------------\n")

# (loops)================================================================================

import time
print("\n------------------------------")
#while

#name = ""
#while len(name) == 0:
#    name = input("ENTER YOUR NAME: \n")
#    print("Hello "+name.capitalize())
#forloop

#for i in range(10):
#    print(i)# code here includes 0 excludes last index
#for i in range(50,101,5):

#    print(i)# code here includes 0 excludes last index

#for i in "Ali is good":
#    print(i)

#for seconds in range(10,0,-1):
#    print(seconds)
#    time.sleep(1)
#print("happy new year.")

#nested loops
rows = int(input("how many rows:"))
columns = int(input("how many columns:"))
symbol = input("enter a symbol to use:")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print("")
print("------------------------------\n")
# (loop comntrol staemnets)================================================================
# break    = Used to eliminate the loop entirely
# continue = Skips to the next iteration of the loop
# pass     = Does nothing,acts as a placeholder

#while True:
#    name = input ("enter your name: ")
#    if name != "":
#        break
#keeps asking util something is enteres
phone_num = "453-545-4593 "

#for i in phone_num:
#    if i == "-":
#        continue
#    print(i,end="")
#    skip the thing you dont want

#print("\n------------------------------")
#for i in range(1,21):
#
#   if i == 13:
#    pass
#   else:
#    print (i,end="," if i<20 else".")
#
#print("\n------------------------------\n")
# (lists )================================================================================

print("\n------------------------------")

food = ["pizza","burger","rice","juice"]
food[0] = "raita"
#print(food[3].capitalize(),end=".")

#food.append ("ice cream")
#food.remove("rice")
#food.pop()
#food.insert(0,"banana")
#food.sort()
#food.clear()

for x in food:
    print(x.capitalize())# code here includes 0 excludes last index
                                        
print("------------------------------\n")
print("\n------------------------------")

question = input("would you like to do calculations press any key. \n")
while question == "p":
    option = input("What would you like to do a) add s) substract d) divide m) multiply \n")
    while option != "q":

        num1 = int(input("enter num1:"))
        num2 = int(input("enter num2:"))

        def add(num1, num2):
            return num1 + num2
        def substract(num1, num2):
            return num1 - num2
        def multiply(num1, num2):
            return num1 * num2
        def divide(num1, num2):
            return num1 / num2
        def quit(quit):
            return quit()

        if option == "a":
            print("Result:", add(num1, num2))
            continue
        elif option == "s":
            print("Result:", substract(num1, num2))
            continue
        elif option == "m":
            print("Result:", multiply(num1, num2))
            continue
        elif option == "d":
            print("Result:", divide(num1, num2))
            continue
    continue
    quit("Quited...")
print("------------------------------\n")

print("\n------------------------------")
#sets = unodered and no duplicate values faster than a list
utnesils = {"fork","spoon","knifes","candles"}
car = {"tesla","toyota","bmw"}

utnesils.add("pencil")
utnesils.remove("spoon")
#utnesils.clear()
utnesils.update(car)
for x in utnesils:
    print(x)                               
print("------------------------------\n")

#dictionary = A changeable, unoredered collection of unique key:value pairs
#fast becuase they use hash8ing, allow us to access a value quickly
print("\n------------------------------")

capitals =  {
            'usa':'washington',
            'pakistan':'islamabad',
            'china':'beijing'
            }  
capitals.update({'germany':'berlin'})
capitals.update({'usa':'texas'})
capitals.pop('germany')
#capitals.clear()
 
#print(capitals['germany'])#dont use this use below one.
#print(capitals.get('india'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key,value in capitals.items():
    print(key,value)
                                     
print("------------------------------\n")

print("\n------------------------------")
#index operator [] = gives aceess to a sequence;s element (str,list,tuples)   

name = "alex blake"
#if(name[0].islower()):
#    name = name.capitalize()
#print(name)

first_name = name[0:8].upper()
last_name = name[9:].lower()

print(first_name) 
print(last_name) 
                                      
print("------------------------------\n")

#function = a block of code which is executed only when it is called.
print("\n------------------------------")
def hello(first_name, last_name):
    print("Hello "+first_name.capitalize())
    print("how r u "+last_name)
    
hello("bro","ali")                            
print("------------------------------\n")

print("\n------------------------------")
#retrun statements = function send pyhton calues/object back to the caller
#                    these values/object are known as the funtion's retrun value.
def multiply(num1, num2):
    return num1 *num2

x = multiply(6,5)
print(x)                                   
print("------------------------------\n")

print("\n------------------------------")
#keyword arguments = arguments preceded by a identifier when we pass them to a function
#                    the order of the arguments dosen't matter, unlike positional arguments 
#                     knows the names of the argument that our funtion recieves.
def hello(first,mid,last):
    print("hello "+first+" "+mid+" "+last)

hello(last="ahsan",first="m",mid="ali")
                                        
print("------------------------------\n")

print("\n------------------------------")
#nested function calls = function calls inside other function calls
#                        innermost function calls are resolved first returned 
#                        value is used as argument for the next outer function

#num = input("enter a positive number: ")
#num=float(num)
#num=abs(num)
#num = round(num)
#print(num)
print(round(round(abs(float(input("enter a whole number"))))))                                  
print("------------------------------\n")

print("\n------------------------------")
# *args = parameter that eill pack all arguments into a tuple
#         useful so that a function can accept a varyiyng amount of arguments.
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum   
print(add(3,43,4,234,32,4,34))                
print("------------------------------\n")
print("\n------------------------------")
#kwargs = parameter that will pack all arguments into a dictionary
#         useful so that a function can accept a varying amount of keyboard arguments.
def hello(**names):
    #print("hello "+kwargs['first']+" "+kwargs['last'])
    print("hello",end=" ")
    for key,value in names.items():
        print(value,end=" ")
    
hello(title = "mr.",first="bro", mid="ali",last="good")

print("\n------------------------------")
#str.format = optional method that gives users moe controls when displaying output.

animal = "cow"
item = "moon"
#print("the "+animal+" jumped over the "+item)

#print("the {} jupmed over the {}".format("cow","moon"))#same
#print("the {} jupmed over the {}".format(animal, item))#same
#print("the {0} jupmed over the {1}".format(animal, item))#same
#print("the {animal} jupmed over the {item}".format(animal="cow", item="moon"))#same

#text = "the {} jumped over the {}"
#print(text.format(animal,item))

#name ="ali"
#print("hello, my name is {:10}. nice".format(name))
#print("hello, my name is {}".format(name))
#print("hello, my name is {:<10}. nice".format(name))
#print("hello, my name is {:>10}. nice".format(name))
#print("hello, my name is {:^10}. nice".format(name))

number1 = 3.14524342
number2 = 10000

#print("the num pi is {:.3f}".format(number2))#is does round the num
#print("the num pi is {:,}".format(number2))#is does round the num
#print("the num pi is {:b}".format(number2))#binary
#print("the num pi is {:o}".format(number2))#oct
#print("the num pi is {:x}".format(number2))#hexadecimal
#print("the num pi is {:.2E}".format(number2))#scientific notation
                                  
print("------------------------------\n")

# random module
import random
print("\n------------------------------")

x = random.randint(1, 10)
y = random.random()

my_List = ["rock", "paper", "scissor"]
z = random.choice(my_List)
print(z)

cards = [1,2,3,4,5,6,7,8,9,"a","j","k"]
random.shuffle(cards)
print(cards)
print("------------------------------\n")

print("\n------------------------------")
try:
    numerator = int(input("enter a number to divide:"))
    denominator = int(input("enter a number to divide by:"))
    result = numerator/denominator
    
except ZeroDivisionError as e:
    print(e)
    print("you can't divide by 0.")
except ValueError as e:
    print(e)
    print("enter only numbers") 
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print("result: {:.2}".format(result))
    
finally:
    print("this line will always execute.")

print("------------------------------\n")
#files
import os
print("\n------------------------------")

path = "/Users/ali/Desktop/Essay answers updated.pdf"

if os.path.exists(path):
    print("exists")
    if os.path.isfile(path):
        print("is file")
else:
    print("dose not")         
print("------------------------------\n")
# rock ,paper , scissor.
print("\n------------------------------")
import random

choices = ["rock", "paper", "scissor"]

while choices:
    computer = random.choice(choices)
    player = input("rock , paper or scissor?:")

    print("computer: ", computer)
    print("player: ", player)

    if computer == player:
        print("draw.")

    elif computer == "scissor" and player == "rock":
        print("player wins")

    elif computer == "scissor" and player == "paper":
        print("computer wins")

    elif computer == "paper" and player == "rock":
        print("computer wins")

    elif player == "scissor" and computer == "rock":
        print("computer wins")

    elif player == "scissor" and computer == "paper":
        print("player wins")

    elif player == "paper" and computer == "rock":
        print("players wins")

    else:
        print("try again")

    play_again = input("want to play again, yes(y) ot no(n): ").lower()
    if play_again != "y":
        break
print("end. bye")
print("------------------------------\n")
#oop
print("\n------------------------------")
class Car:

    def __init__ (self,make, model, color):
        self.make = str(make)
        self.model = str(model)
        self.color = str(color)
    
    def drive(self):
        print("The "+self.make+" is driving. ")
    def stop(self):
        print("The "+self.make+" has stoped. \n")

car_1 = Car("tesla", 2023, "blue")
print("Make:   "+car_1.make)
print("Model:  "+car_1.model)
print("Colour: "+car_1.color)
car_1.drive()
car_1.stop()
#---------------------------------------
car_2 = Car("mercedes", 2014, "black")
print("Make:   "+car_2.make)
print("Model:  "+car_2.model)
print("Colour: "+car_2.color)
car_2.drive()
car_2.stop()
                                  
print("------------------------------\n")
# super class: function used to give access to the methods of a methods of a parent class.
#              return a temporary object of  a parent class when used.
print("\n------------------------------")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width

class Cube(Square):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height

square = Square(3,5)
cube = Cube(3,5,8)

print(square.area())
print(cube.volume())

print("------------------------------\n")"""

"""
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text='Hello, Ali!')

if __name__ == '__main__':
    MyApp().run()


# Higer order function = a function that either 
#                   :1 accepts a function as argumetn 
#                                         or
# 2: returns a function in  functions are also treated as functions.#
print("\n------------------------------")

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("hello") 
    print(text)

hello(loud)                               
print("------------------------------\n")

print("\n------------------------------")

options = input("Enter what u want to do? a)add s)substract m)multiply d)divide. \n")

num1= int(input("enter num1: "))
num2= int(input("enter num2: "))

result =0

def add(num1,num2):
    return num1+num2

def substract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

if options == 'a':
    print(add(num1,num2))
    
elif options =='s':
    print(substract(num1,num2))

elif options =='m':
    print(multiply(num1,num2))

elif options =='d':
    print("{:.3f}".format(divide(num1,num2)))

print("------------------------------\n")

print("\n------------------------------")

pairs_of_boots = int(input())
pairs_of_sandals = int(input())

total_pairs = pairs_of_boots +int(5) + pairs_of_sandals +int(5)

print(pairs_of_boots +int(5),'pairs_of_boots')
print(pairs_of_sandals+int(5),'pair_of_sandals')
print(total_pairs,'total')

print("------------------------------\n")

print("\n------------------------------")

pairs_of_boots = int(input())
pairs_of_sandals = int(input())

total_pairs = ((pairs_of_boots +int(5))+ (pairs_of_sandals +int(5) ) ,   (pairs_of_boots+5), (pairs_of_sandals+5))

print(pairs_of_boots ,'pairs_of_boots')
print(pairs_of_sandals,'pair_of_sandals')
print(total_pairs,'total')

print("------------------------------\n")
"""
#=======================================================================================================================
























