file_contents = open("day7.txt").read().split(",")
file_contents = [int(content) for content in file_contents]
print(file_contents)
# found = False
# position = 0
# cacheFuel = 200000000
# while found == False:
#     totalFuel = 0
#     for i, content  in enumerate(file_contents):
#         fuel = content - position
#         if fuel < 0:
#             fuel = -fuel
#         totalFuel += fuel
#     if totalFuel < cacheFuel:
#          cacheFuel = totalFuel
#     position += 1
#     if position == 2000:
#         found = True
# print(cacheFuel)
    
#part 2

found = False
position = 0
cacheFuel = 200000000
newFuel = 0
while found == False:
    totalFuel = 0
    for i, content  in enumerate(file_contents):
        fuel = content - position
        if fuel < 0:
            fuel = -fuel
        newFuel = 0
        for i in range(fuel+1):
            newFuel += i
        
        totalFuel += newFuel
    
    if totalFuel < cacheFuel:
         cacheFuel = totalFuel
    position += 1
    if position == 2000:
        found = True
print(cacheFuel)




    


