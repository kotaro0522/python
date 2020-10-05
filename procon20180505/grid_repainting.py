h, w = map(int, input().split())

def check(x, y, board, h, w):
  if x > 0:
    if board[x-1][y] == '#':
      return True

  if y > 0:
    if board[x][y-1] == '#':
      return True

  if y != w-1:
    if board[x][y+1] == '#':
      return True

  if x != h-1:
    if board[x+1][y] == '#':
      return True

  return False

board = []
answer = 'Yes'

for i in range(h):
  board.append(list(input()))

for i in range(h):
  for j in range(w):
    if board[i][j] == '#':
      if check(i, j, board, h, w) == False:
        answer = 'No'

print(answer)
