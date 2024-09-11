'''x = 5#int
y = 3.14#float
z = 2+3j#complex
print(x)
print(y)
print(z)


text = "hello worl"
print(text)

numbers = [1,2,2,3,45]
for i in numbers:
    print(i)

coords = (10,20)
print(coords)

person = {"name":"john","age":30}
print(person)
print(person["name"])

for i in person:
    print(i,person[i])

setnumbs = {1,2,3}
for i in setnumbs:
    print(i)
'''
# == != > < >= <=
'''if(4<6):
    print("true")

#and or not
if(4<6) and  (5>2):
    print("true")'''

'''x=5
if x<6:
    print("true")
elif x<=5:
    print("true")
else:
    print("false")


numbers = [1,2,3,4,5,6]
for i in range(len(numbers)):
    print(numbers[i],end="")
'''
#виводим тільки парні 
'''
numbers = [1,2,3,4,5,6,7]
for i in range(len(numbers)):
    if (numbers[i] % 2 == 0):
        print(numbers[i])'''

'''import math as m
print(m.sqrt(25))
'''
''''
command = input()

match command:
    case "start":
        print("program had started")
    case "falied":
        print("program has not started")
    case_:
        print("lol dude")'''
'''
x = 0
while x<5:
    print(x)
    x+=1

for i in range(10):
    print(i)
else:
    print(124125124)
'''

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

index = len(numbers)
for i in range(len(numbers)):
    if(index == 0):
        break
    index - 1
    if(index%2 == 0):
        continue
    if(numbers[i] % 2 != 0):
        print(numbers[i])



    
