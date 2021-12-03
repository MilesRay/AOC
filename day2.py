f = open("day2.txt")

file_contents = f.read()

file_contents = file_contents.split(" ")
new_list = [n for n in file_contents]

for i in range(0, len(new_list)):
    print(new_list[i])


f = open("day2.txt")

file_contents = f.read()

forwardCount = 0
depthCount = 0
file_contents = file_contents.split(" ")
new_list = [n for n in file_contents]

for i in range(0, len(new_list)):
    if new_list[i] == "forward":
        forwardCount = forwardCount + int(new_list[i+1][:1])

    if new_list[i] == "up":
        depthCount = depthCount + int(new_list[i+1][:1])

    if new_list[i] == "down":
        depthCount = depthCount - int(new_list[i+1][:1])


print(forwardCount*depthCount)




