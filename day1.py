
f = open("day1.txt")
file_contents = f.read()

file_contents = file_contents.split("\n")


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