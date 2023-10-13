import random

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if all(cell == row[0] and cell != ' ' for cell in row):
            return True

    for col in range(3):
        if all(row[col] == board[0][col] and board[0][col] != ' ' for row in board):
            return True
for col in range(3):
  if all(row[col] == board[0][col] and board[0][col] != ' ' for row in board):
      return True

if all(board[i][i] == board[0][0] and board[i][i] != ' ' for i in range(3)) or \
 all(board[i][2 - i] == board[0][2] and board[i][2 - i] != ' ' for i in range(3)):
  return True

return False

def check_draw(board):
# Check if the board is full, indicating a draw
return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
# Get a list of empty cells on the board
return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
if check_winner(board):
  return -1 if is_maximizing else 1

if check_draw(board):
  return 0

scores = []
empty_cells = get_empty_cells(board)

for i, j in empty_cells:
  board[i][j] = 'X' if is_maximizing else 'O'
  score = minimax(board, depth + 1, not is_maximizing)
  scores.append(score)
  board[i][j] = ' ' # Undo the move

return max(scores) if is_maximizing else min(scores)

def best_move(board):
best_score = float('-inf')
best_move = None

empty_cells = get_empty_cells(board)

for i, j in empty_cells:
  board[i][j] = 'X'
  score = minimax(board, 0, False)
  board[i][j] = ' '

  if score > best_score:
      best_score = score
      best_move = (i, j)

return best_move

def play_tic_tac_toe():
board = [[' ' for _ in range(3)] for _ in range(3)]

while True:
  print_board(board)

  # Player's move
  row = int(input("Enter row (0, 1, or 2): "))
  col = int(input("Enter column (0, 1, or 2): "))

  if board[row][col] != ' ':
      print("Cell already occupied. Try again.")
      continue

  board[row][col] = 'O'

  # Check if the player wins
  if check_winner(board):
      print_board(board)
      print("Congratulations! You win!")
      break

  # Check for a draw
  if check_draw(board):
      print_board(board)
      print("It's a draw!")
      break

  # AI's move
  print("AI's move:")
  ai_row, ai_col = best_move(board)
  board[ai_row][ai_col] = 'X'

  # Check if the AI wins
  if check_winner(board):
      print_board(board)
      print("AI wins! Better luck next time.")
      break

  # Check for a draw
  if check_draw(board):
      print_board(board)
      print("It's a draw!")
      break

if __name__ == "__main__":
play_tic_tac_toe()
