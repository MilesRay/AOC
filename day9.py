file_contents = open("day9.txt").read().split("\n")
# nums = [int(contents) for contents in file_contents ]
# print(file_contents)
# all_Nums = [[0]*100]*100
for i in range(100):
    nums = [int(num) for num in file_contents[i]]

print(nums[3])
    

    