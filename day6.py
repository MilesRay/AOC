file_contents = open("day6.txt").read().split(",")

file_contents = [int(content) for content in file_contents]

print(file_contents)
for i in range(80):
    for j in range(len(file_contents)):
        file_contents[j] -= 1
        if file_contents[j] == 0:
            file_contents.append(8)
            file_contents[j] = 6

print(len(file_contents))
