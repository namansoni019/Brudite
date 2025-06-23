import csv

SCORE_FILE = "scores.csv"

def load_scores(path):
    data = []
    try:
        with open(path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    name, score = row
                    data.append((name, int(score)))
    except FileNotFoundError:
        print("No score file found, starting fresh.")
    except:
        print("Something went wrong while loading scores.")
    return data

def save_scores(path, data):
    try:
        with open(path, 'w') as file:
            writer = csv.writer(file)
            for item in data:
                writer.writerow(item)
    except:
        print("Couldn't save scores.")

def add_score(data, name, score):
    data.append((name, score))

def top_scores(data, n):
    return sorted(data, key=lambda x: x[1], reverse=True)[:n]

# ---------- TICTACTOE PART ----------

def choose_symbols():
    sym = ""
    while sym not in ['X', 'O']:
        sym = input("Player 1, choose X or O: ").upper()
    p1 = sym
    p2 = 'O' if sym == 'X' else 'X'
    return p1, p2

def make_board():
    return [" "] * 9

def show_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def valid(board, index):
    return board[index] == " "

def get_move(symbol, board):
    while True:
        val = input(f"Player {symbol}, enter spot (1-9): ")
        if not val.isdigit():
            print("Not a number.")
            continue
        pos = int(val) - 1
        if pos < 0 or pos > 8:
            print("Enter between 1-9 only.")
            continue
        if not valid(board, pos):
            print("Already taken.")
            continue
        return pos

def check_win(board, symbol):
    win = [
        (0,1,2), 
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7), 
        (2,5,8),
        (0,4,8), 
        (2,4,6)
    ]
    for a,b,c in win:
        if board[a] == board[b] == board[c] == symbol:
            return True
    return False

def play_tictactoe():
    print("\n--- Tic Tac Toe ---")
    p1, p2 = choose_symbols()
    name1 = input(f"Name for Player {p1}: ")
    name2 = input(f"Name for Player {p2}: ")
    sym_to_name = {p1: name1, p2: name2}
    
    board = make_board()
    current = p1

    show_board([str(i+1) for i in range(9)])

    while True:
        show_board(board)
        pos = get_move(current, board)
        board[pos] = current

        if check_win(board, current):
            show_board(board)
            print(f"{sym_to_name[current]} (Player {current}) wins!")
            return sym_to_name[current]
        elif " " not in board:
            show_board(board)
            print("It's a draw.")
            return None
        current = p2 if current == p1 else p1

# ----------- MENU PART ------------

def get_number(msg, minimum=None, maximum=None):
    while True:
        try:
            val = int(input(msg))
            if minimum is not None and val < minimum:
                print("Too low.")
                continue
            if maximum is not None and val > maximum:
                print("Too high.")
                continue
            return val
        except:
            print("Not a valid number.")

def main():
    recordsList = load_scores(SCORE_FILE)

    while True:
        print("\n--- MENU ---")
        print("a. Play Tic Tac Toe")
        print("b. Show Top Scores")
        print("c. Add New Score")
        print("d. Exit")

        choice = input("Your choice (a/b/c/d): ").strip().lower()

        if choice == "a":
            winner = play_tictactoe()
            if winner:
                print(f"{winner} gets 10 points.")
                add_score(recordsList, winner, 10)
                save_scores(SCORE_FILE, recordsList)
            else:
                print("No points for draw.")

        elif choice == "b":
            try:
                n = int(input("How many top scores to show? "))
                top = top_scores(recordsList, n)
                print("\nTop Players:")
                for i, (name, score) in enumerate(top, start=1):
                    print(f"{i}. {name} - {score}")
            except:
                print("Invalid number.")

        elif choice == "c":
            name = input("Enter name: ")
            try:
                scr = int(input("Enter score: "))
                add_score(recordsList, name, scr)
                save_scores(SCORE_FILE, recordsList)
                print("Score added.")
            except:
                print("Invalid score input.")

        elif choice == "d":
            print("Bye!")
            break

        else:
            print("Invalid choice. Please type a, b, c, or d.")


if __name__ == "__main__":
    main()
