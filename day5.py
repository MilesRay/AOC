import re 
file_contents = open("day5.txt").read()
split_coords = re.split(r"\n| -> |,",file_contents)
coords = [unsplit.split("\n") for unsplit in split_coords]
coords = [int(coord[0]) for coord in coords]
board = [[0]*1000]*2
# print(coords)
count = 1
# print(zip(coords[:-2], coords[2:]).__next__())
for i, j in zip(coords[:-2], coords[2:]):
    count += 1
    if count % 2 == 0:
        if coords[i] == coords[i+2]:
            for j in range(1000):
                board[i][j] + 1
    else:
        if coords[i] == coords[i+2]:
            for j in range(1000):
                board[j][i] + 1

    
# print(board)
print(board)