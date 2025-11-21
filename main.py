# ////////////////////// function////////////////////////
# def calculate(a, b, sign):
#     print(f"The value of {a} {sign} {b} = {eval(f'{a}{sign}{b}')}")
# calculate(5, 2, '/')
# ////////// asking value from user////////////////////
# # x = input("Enter first digit: ")
# # y = input("Enter first digit: ")
# # print(type(x))
# # print(type(y))
# # print(int(x) +  int(y))
# ////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////// list[starting index, endling index ,  step to skip]///////////////
# name="harry"
# print(name[2:-2])
# ///////////////////////////////////////////////////////////////////////////
# //////////////////////// if else in python/////////////////////////////////
# import time
# currentTime = time.strftime("%H:%M:%S") 
# currentHour = currentTime[0:2]
# print(time.strftime("%H"))
# print(currentTime[0:2])
# if(int(currentHour) >= 6 and int(currentHour) <= 12):
#     print("good morning")
# elif(int(currentHour) >= 13 and int(currentHour) <= 20):
#     print("good evening")
# elif(int(currentHour) <=5  or int(currentHour) >= 21):
#     print("good night")
# else:
    # print("check time")
# /////////////////////////////////////////////////////////////////////////////////////
# ///////////////////// List built in functions in python//////////////////////////////
# l = [3,8,7,1,0,6,9]
# print(f"starting List {l}")
# ///// to add a new value to list , it will be added to end///////////
# l.append(5)
# print(l)
# ///// to sort the list ///////////
# l.sort()
# print(l)
# ///// to sort the list in decending order///////////
# l.sort(reverse=True)
# print(l)
# ///// to reverse the original list ///////////
# l.reverse()
# print(l)
# ///// to get the index of specific item in the list => index function return the index of first occured item ///////////
# print(l.index(7))
# /////////// to count the occurence of specific item in the list ////////
# print(l.count(0))
# ////// to make copy of a list and then edit it //////////////
# m = l.copy()
# m[0] =89
# print(m)
# print(l)
# remeber if you don't use copy() fucntion the on m[0] =89 it will edit l list because m list is a reference of l list
# m = l
# m[0] =89
# print(m)
# print(l)
# ///// to insert a specific item at specific index in the list ///////////
# l.insert(1, 0)
# print(l)
# ///// to add a other list in the list ///////////
# m = [100, 200 , 300]
# l.extend(m)
# print(l)
# you can also do this by making a third list and adding both list in it
# m = [100, 200 , 300]
# k = l + m
# print(k)
# /////////////////// TUPLE IN PYTHON //////////////////////////
# //// REMEMBER TUPLE CAN'T BE CHANGE AS A LIST DO//////////
# ////////// in list we use square bracket [] and in tuple we use rounded brackets () //////////////////
# tup = (2,8,1)
# print(type(tup), tup)
# agar tum tuple ko 1 value do gy tu lazmi comma( , ) add krna huga warna wo int ya string assume krlega like
# tup = (1) # here after 1 comma is must to generate a tuple
# print(type(tup), tup) 
# ///////// you can add different data types item in a single tuple and list in python //////
# tup = (2,5,9,"hi" , True)
# print(type(tup), tup)
# //// to print item of specific index in tuple ///////
# tup = (2,8,1)
# print(tup[1])
# //////// SLICING OF TUPLE IS SAME AS IN LIST ////////
# tup = (8,6,5,2,3,1,4)
# tup2 = tup[2:5]
# print(tup2)
# //////// TO EDIT A TUPLE YOU HAVE TO CHANGE IT TO LIST FIRST AND THEN EDIT AND THEN THEN BACK TO TUPLE///////
# names = ("mack","john", "smith", "nikloa")
# temporaryList = list(names)
# print(temporaryList)
# temporaryList.append("goerge")
# temporaryList.pop(1)
# print(temporaryList)
# names = tuple(temporaryList)
# print(names)
# /////////////////// DAY-27 KON BANEGA KAROR PATI GAME //////////////////
# questionsList = {
#     "What is capital of pakistan": {
#         "options" : ["(a) karachi" ,"(b) lahore","(c) islamabad" , "(d) quetta"],
#         "correctAnswer": "c"
#         },
#     "What is capital of Sindh": {
#         "options" : ["(a) karachi" ,"(b) hyderabad","(c) sukkur" , "(d) tatta"],
#         "correctAnswer": "a"
#         },
#     "What is capital of balochistan": {
#         "options" : ["(a) lasbela" ,"(b) kalat","(c) khuzdar" , "(d) quetta"],
#         "correctAnswer": "d"
#         },
# }
# prize = 0
# def askQuestion(gameContent):
#     global prize
#     print("Choose correct answer by selecting in a , b, c, d")
#     for i in gameContent:
#         user_aswer = input(f"{i}? \nOptions are:\n{", ".join(gameContent[i]["options"])} \nYour answer: ")
#         if(user_aswer == gameContent[i]["correctAnswer"]):
#             prize += 100
#             print("correct answer")
#         else:
#             print("sorry wrong answer")
#     print(f"Game over! \n You get prize of ${prize}")
# askQuestion(questionsList)
# /////////////// RECURSION IN PYTHON //////////////////
# def factorial(n):
#     if(n <= 1):
#         # print(n)
#         return 1
#     else:
#one way of doing this 
        # sub = factorial(n - 1)  
        # print(f"it comes {n} with {n * sub}")
        # # return n * sub
# second way of doing this
#         return (n * factorial(n-1))
# print(factorial(4))
# /////////////// fibonacci IN PYTHON //////////////////
# def fibonacci(n):
#     if(n <= 0):
#         return 0
#     elif(n ==1):
#          return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# for i in range(0,8):
#         print(f"my i is {i}")
#         print(fibonacci(i))
# ///////////////// SETS IN PYTHON //////////////////
# /// sets are unorderd collection of items and it can't have duplicate values ////
# //////// sets are unchangeable, sets uses curly bracket, set does not contain duplicate items ///////
# ///// set me order kabhi bi maintain ni hoga /////
# mySet =  {10, 3, 21, 7, 2}
# print(mySet)
# info = {"name", 20,False, 5.6, "ssssss " , 55}
# print(info)
# emptySet =  {} # this will create a dictionary not a set
# print(type(emptySet))
# to create an empty set you have to use set() function
# emptySet = set()
# print(type(emptySet))
# ///////// for loop in set //////
# mySet =  {10, 3, 21, 7, 2}
# for i in mySet:
#     print(i)
# /////// METHODS IN SET //////
# ////// to add 2 SETS ///////
# S1 = {2,4,1,6,3,8,9}
# S2 = {3,5,4,7,1,8,6}
# S3 = set()
# S3 = S1.union(S2) # it will merge both sets and remove duplicate values
# print(S3)
# S3 = S1.intersection(S2) # it will give only common values in both sets
# print(S3)
# S1.update(S2) # it will add S2 values to S1 and remove duplicate values
# print(S1)
# S1.intersection_update(S2) # it will keep only common values in S1 and remove other values
# print(S1)
# ////// SYEMMETRIC DIFFERENCE ///////
# S3 = S1.symmetric_difference(S2) # it will give values which are not common in both sets
# print(S3)
# S3 = S1.difference(S2) # it will give values which are in S1 but not in S2
# print(S3)
# ////// dISJOINT METHOD ///////
# isdisjoint() — checks if NO common element exists between two sets
# isDisjoint = S1.isdisjoint(S2) # it will return false if both sets have common values otherwise true
# print(isDisjoint)
# ////// ISSUPERSET METHOD ///////
# issuperset() — checks if S1 contains ALL values of S2
# issuperset = S1.issuperset(S2) # it will return true if S1 has all values of S2 otherwise false
# print(issuperset)
# REMOVE/ADD/UPDATE ARE COMMON METHODS IN SET LIKE LIST//////////////// 
# DISCARD OR REMOVE METHOD ITEM KO SET SE HATA DETA HAI FARQ BUS ITNA HAI K DISCARD
# METHOD AGAR ITEM NA HO TU BHI ERROR NI DEGA MAGAR REMOVE METHOD ERROR DEGA
# ///// POP METHOD ///////
# poppedItem = S1.pop() # it will remove random item from set because set is unorderd
# ///// CLEAR METHOD ///////
# S1.clear() # it will CLEAR entire set
# ///// DEL METHOD ///////
# del S1 # it will delete entire set
# /////////////////////// DICTIONARIES IN PYTHON //////////////////////////
# ///// dictionaries are used to store data values in key:value pairs ///////
# ///// dictionaries are ordered changeable and do not allow duplicates ///////
# myDict = {
#     "name": "john",
#     "age": 30,
#     "city": "new york"
# }
# print(myDict)
# print(myDict["name"]) # to access specific value in dictionary by using key
# print(myDict.get("age")) # another way to access specific value in dictionary by using key
# print(myDict.keys()) # to get all keys of dictionary 
# print(myDict.values()) # to get all values of dictionary
# print(myDict.items()) # to get all key:value pairs of dictionary
# # /// to get the key using for loop /////
# for i in myDict.keys():
#     print(i)
# # /// to get the value using for loop /////
# for i in myDict.values():
#     print(i)
# # OR
# for i in myDict.keys():
#     print(myDict[i])
# /////////// METHODS IN DICTIONARY ///////////
# seniorEMPLOYEES = {
#     "ali": 72,
#     "asad": 80,
#     "saeed": 68,
#     "umer": 90,
#     "bilal": 75
# }
# juniorEMPLOYEES = {
#     "hamza": 50,
#     "hassan": 60,
#     "ahmed": 55,
# }
# seniorEMPLOYEES.update(juniorEMPLOYEES) # it will add juniorEMPLOYEES dictionary to seniorEMPLOYEES dictionary
# seniorEMPLOYEE = (...juniorEMPLOYEES)
# print(juniorEMPLOYEES)
# //// to add a dictionary in another dictionary /////
# **seniorEMPLOYEES will add all key:value pairs of seniorEMPLOYEES dictionary to juniorEMPLOYEES dictionary
# ///// to clear entire dictionary /////
# juniorEMPLOYEES.clear()
# ///// to remove a item in dictionary /////
# juniorEMPLOYEES.pop("hamza") # it will remove hamza item from juniorEMPLOYEES dictionary
# ///// to remove last item in dictionary /////
# juniorEMPLOYEES.popitem() # it will remove last item from juniorEMPLOYEES dictionary
# ///// to delete item in dictionary /////
# del juniorEMPLOYEES["hamza"] # it will delete hamza item from juniorEMPLOYEES dictionary 
# print(juniorEMPLOYEES)
# /////////////////////// for loop with else in python //////////////////////////
# main point is agar for loop me controller nhi jaa paya tu else me jaay ga
# or agar for loop me controller jaa paya tu end me else chalega
# for i in range(5):
#     print(i)
# else:
#     print("loop is ended")
# /// break k through else ko ruk sakty hha//////////
# for i in range(5):
#     print(i)
#     if(i == 3):
#         break
# else:
#     print("loop is ended")
# ////////////// ENUMERATE FUNCTION IN PYTHON //////////////////
# /// it will give index along with value in for loop ///
# name = "harry"
# for index, value in enumerate(name):
#     print(f"at index {index} the value is {value}")
# //////////////////////////////////////////////////////
# marks = [78, 85, 62, 90, 55]
# for index, value in enumerate(marks):
#     if(index == 2):
#         print("you have to work hard")
#     else:
#         print(f"at index {index} the mark is {value}")
    
# /////////////////////////////TRY EXCEPT FINALLY CLAUSE IN PYTHON ///////////////////
# try:
#     num = int(input("enter a number:  "))
#     a= [1,6]
#     print(a[num])
# except ValueError:
#     print("not an integer provided")
# except IndexError:
#     print("not in range")
# finally:
#     print("i am always executed")
# ///////////////////////////// RAISING CUSTOM ERRORS IN PYTHON ///////////////////
# in pythoin we can raise a custome error by using a "raize" keyword, this custom raise error will not allow 
# to furthur execute your program if something is went wroung or unexpected
# num = int(input("enter a value between 5 and 10: "))
# if(num <5 or num >10):
#     raise ValueError("Value should be between 5 and 10")
# ///////////////////// Quiz # write a program translate a message into secret code language//////
# Rules=>
# if word contains more then 3 characters , remove the first one and append it to last and then add 3 random character at begining
# and at ending. if word contains less or equal to 3 then simply reverse it
# AND VISE VERSA FOR DECREPTION
# import random
# import string
# all_alphabets = string.ascii_letters
# def wordIncript():
#     word = input("enter your meesage to incripte: ")
#     if(len(word) <= 3 ):
#         print(word[::-1])
#     else:
#         first_char = word[0]
#         remaining_string = word[1:]
#         new_string = remaining_string + first_char
#         beg_random_charachters = "".join(random.choices(all_alphabets, k=3)).lower()
#         end_random_charachters = "".join(random.choices(all_alphabets, k=3)).lower()
#         incriptedMessage = beg_random_charachters+ "" +new_string + "" + end_random_charachters
#         print(f"your incriptedMessage {incriptedMessage}")
# def wordDecript():
#     word = input("enter your meesage to decripte: ")
#     if(len(word) <= 3 ):
#         print(word[::-1])
#     else:
#         remove_beg = word[3:]
#         remove_end = remove_beg[:-3]
#         last_char = remove_end[len(remove_end) -1]
#         remove_end = remove_end[:-1]
#         decriptedMessage = last_char + remove_end
#         print(f"your decriptedMessage {decriptedMessage}")
# choice = input("Want to incripte or Decripte a message, type i for incripte and d for decripte: ").lower()
# if(choice == "i"):
#     wordIncript()
# elif(choice == "d"):
#     wordDecript()
# else:
#     print("invalid option selected")
