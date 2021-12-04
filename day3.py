
# def test(var1, var2):
#     var1 += " world"
#     var2.append("world")

# v1 = "hello"
# v2 = ["hello"]

# print(v1, v2)
# test(v1, v2)
# print(v1, v2)

# quit()
file_contents = open("day3.txt").read().split("\n")
final = [None] *12
final2 = [None] *12

for position in range(len(file_contents[0])):
    count1 = 0
    count0 = 0
    for binary in file_contents:
        
        if binary[position] == '1':
            count1 += 1

        if binary[position] == '0':
            count0 += 1
    print(count1,count0)
    if count1 > count0:
        final[position] = '1'
    
    else:
        final[position] = '0'

for i in range(12):
    if final[i] == '0':
        final2[i] = '1'
    else: final2[i] = '0'

final2 = ["0" if n == "1" else "1" for n in final]

epsilon = int("".join(final2), 2)

gamma = int("".join(final), 2)


print(gamma*epsilon)





print(final)
    

#part 2

file_contents2 = file_contents.copy()


for position in range(len(file_contents[0])):
    
    
    count1 = 0
    count0 = 0
    array2 = [] 
    for binary in file_contents:
        
        if binary[position] == '1':
            count1 += 1

        if binary[position] == '0':
            count0 += 1
#oxygen
  
    for binary in file_contents:
        if count1 >= count0:
             if binary[position] == '1':
                array2.append(binary)
        else:
            if binary[position] == '0':
                array2.append(binary)
    
    
    
    file_contents = array2
    print(len(file_contents))
    if len(file_contents) == 1:
        break

print(file_contents)
oxygen = int((file_contents[0]), 2)

#C02
  
for position in range(len(file_contents2[0])):

    count1 = 0
    count0 = 0
    array1 = []

    for binary in file_contents2:
        
        if binary[position] == '1':
            count1 += 1

        if binary[position] == '0':
            count0 += 1



    for binary in file_contents2:
        if count1 < count0:
             if binary[position] == '1':
                array1.append(binary)
        else:
            if binary[position] == '0':
                array1.append(binary)
    
    
    file_contents2 = array1

    print(len(file_contents2))
    

    if len(array1) == 1:
        break

c02 = int((file_contents2[0]), 2)
print(file_contents2)

print(oxygen*c02)
    


    
    


  # if count1 >= count0:

    #     for binary in file_contents:
        
    #         if binary[position] == '1':
    #             array2.append(binary)

    # elif count1 < count0:
    #     for binary in file_contents:
        
    #         if binary[position] == '0':
    #             array2.append(binary)

            


        

            


        



