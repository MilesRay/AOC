f = open("Github/AOC/day2.txt")

file_contents = f.read()

file_contents = file_contents.split(" ")
new_list = [int(n) for n in file_contents]

for i in range(0, len(new_list)):
    print(new_list[i])





