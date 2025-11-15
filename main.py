# def calculate(a, b, sign):
#     print(f"The value of {a} {sign} {b} = {eval(f'{a}{sign}{b}')}")
# calculate(5, 2, '/')

# # x = input("Enter first digit: ")
# # y = input("Enter first digit: ")
# # print(type(x))
# # print(type(y))
# # print(int(x) +  int(y))


# name="harry"
# print(name[2:-2])

import time
currentTime = time.strftime("%H:%M:%S") 
currentHour = currentTime[0:2]
# print(time.strftime("%H"))
# print(currentTime[0:2])
if(int(currentHour) >= 6 and int(currentHour) <= 12):
    print("good morning")
elif(int(currentHour) >= 13 and int(currentHour) <= 20):
    print("good evening")
elif(int(currentHour) <=5  or int(currentHour) >= 21):
    print("good night")
else:
    print("check time")