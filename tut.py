print("Hello World")

print("hello " + "world", 23)

s = "hell"
myint = 9099
myfloat = 3.455

# type casting

int()
str()
float()
list()
bool()
dict()

i = 0

i = i + 1 # same with -/*+
i += 1

my_list = [2, 46, 7, "heelo"]

print(my_list[0]) # 2

my_dict = {
    'hello': 1,
    1818: "he"
}

print(my_dict['hello']) # 1

print(type(my_dict))


# dynamic types (same as js)
a = "hello"
a = 11


print(list(range(5))) # 0, 1, 2, 3, 4
print(list(range(0, 5))) # 0, 1, 2, 3, 4
print(list(range(4, 7))) # 4, 5, 6
print(list(range(6, 3, -1))) # 6, 5, 4


# loop over values
for t in my_list: 
    print(t)

for i in range(len(my_list)):
    print(my_list[i])

for i, value in enumerate(my_list):
    print(i, value)






for key in my_dict:
    print(key, my_dict[key])

for key in my_dict.keys():
    print(key, my_dict[key])

for val in my_dict.values():
    print(val)

for key, val in my_dict.items():
    print(key, val)


i = 0
while 1:
    if i == 5:
        break
    i += 1

if i == 4:
    print("i is 4")

if i:
    print("i exists")


f = open("day1.txt")
file_contents = f.read()

file_contents = file_contents.split("\n")


# new_list = []

# for number in file_contents:
#     new_list.append(int(number))



new_list = [int(n) for n in file_contents]


#part 1
count = 0
for i in range(1,len(new_list)):
    if new_list[i-1] < new_list[i] :
        count += 1

print(count)


#part 2
count = 0
for i in range(3,len(new_list)):
    total1 = new_list[i-1] + new_list[i-2] + new_list[i-3]
    total2 = new_list[i] + new_list[i-1] + new_list[i-2]
    
    

    if total2 > total1 :
        count += 1

print(count)



mystring = "hello there"

print(mystring[5])
print(mystring[2:5])
print(mystring[2:])
print(mystring[:5])
print(mystring[-1:])
print(mystring[:-1])

this = [3,2,5,8]
mylist = [5, 2, 8, 9, 1]

print(mylist[2:])

var1, var2 = [4, 6]
print(var1, var2)
print(mystring.replace(" ", ""))


# #list comp
# called = []
# for number in numbers.split(","):
#     called.append(int(number))
    
# called = [int(n) for n in numbers.split(",")]

print(sum(set(this) - set(mylist)))
    