import json
file_contents = open("day4.txt").read().split("\n\n")
# print(json.dumps(file_contents, indent = 4))

bingo = []
numbers, boards = file_contents[0], file_contents[1:]

called = [int(n) for n in numbers.split(",")]
  
for board in  boards:
    rows = board.split("\n")
    new_board = []
    for row in rows:
        row = [int(c) for c in row.replace("  "," ").lstrip().split(" ")]
        new_board.append(row)
    bingo.append(new_board)

def find_winner(find_last=False): 
    row_matches = [[0 for _ in range(5)] for _ in range(len(boards))]
    col_matches = [[0 for _ in range(5)] for _ in range(len(boards))]

    winners = set()
    for n, number in enumerate(called):
        for board_id, board in enumerate(bingo):
            for r, row in enumerate(board):
                for c, cell in enumerate(row):
                    if number == cell:
                        # print(f"num={number} i={board_id} r={r} c={c}")
                        row_matches[board_id][r] += 1
                        col_matches[board_id][c] += 1

                        if row_matches[board_id][r] == 5:
                            winners.add(board_id)
                            if not find_last:
                                return board_id, number, called[:n+1]
                            
                        if col_matches[board_id][c] ==5:
                            winners.add(board_id)
                            if not find_last:
                                return board_id, number, called[:n+1]

                        if len(winners) == len(bingo):
                            return board_id, number, called[:n+1]

board_id,wining_number,numbers_called = find_winner()
print(sum(set(sum(bingo[board_id], [])) - set(numbers_called))*wining_number)

board_id,wining_number,numbers_called = find_winner(True)
print(sum(set(sum(bingo[board_id], [])) - set(numbers_called))*wining_number)







                    







