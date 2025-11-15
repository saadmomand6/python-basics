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
