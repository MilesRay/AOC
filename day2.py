
f = open("day2.txt")

file_contents = f.read()

forwardCount = 0
depthCount = 0
file_contents = file_contents.split("\n")

new_list = [n for n in file_contents]


for i in range(0, len(new_list)):
    new_list[i] = new_list[i].split(" ")
    
print(new_list)
for i in range(0, len(new_list)):
    if new_list[i][0] == "forward":
        forwardCount = forwardCount + int(new_list[i][1])

    if new_list[i][0] == "up":
        depthCount = depthCount - int(new_list[i][1])

    if new_list[i][0] == "down":
        depthCount = depthCount + int(new_list[i][1])


print(forwardCount*depthCount)


#part 2


file_contents = open("day2.txt").read()

forwardCount = 0
depthCount = 0
file_contents = file_contents.split("\n")

new_list = [n for n in file_contents]


for i in range(0, len(new_list)):
    new_list[i] = new_list[i].split(" ")
    
print(new_list)
for i in range(0, len(new_list)):
    if new_list[i][0] == "forward":
        forwardCount = forwardCount + int(new_list[i][1])

    if new_list[i][0] == "up":
        depthCount = depthCount - int(new_list[i][1])

    if new_list[i][0] == "down":
        depthCount = depthCount + int(new_list[i][1])


print(forwardCount*depthCount)
