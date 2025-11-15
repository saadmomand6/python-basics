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
