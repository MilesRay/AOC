file_contents = open("day7.txt").read().split(",")
file_contents = [int(content) for content in file_contents]
print(file_contents)
found = False
position = 0
while found == False:
    position += 1
    totalFuel = 0
    for i, content  in enumerate(file_contents):
        fuel = content - position
        if fuel < 0:
            fuel = -fuel
        totalFuel += fuel



    


