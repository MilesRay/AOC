import re 
file_contents = open("day5.txt").read()
split_coords = re.split(r"\n| -> |,",file_contents)
coords = [unsplit.split("\n") for unsplit in split_coords]
board = [[0]*1000]*2
# print(coords)
for i in coords:
    new_coords = [int(n) for n in coords[i][0]]
print(new_coords)
# count = 1
# for i in coords:
#     k = i
#     print(int(k))
#     # count += 1
#     # if count % 2 == 0:
#     #     if i == i+2:
#     #         for j in 1000:
#     #             board[i][j]
#     # else:
#     #     if i == i+2:
#     #         for j in 1000:
#     #             board[j][i]

    
# print(board)