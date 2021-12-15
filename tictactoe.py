board = [[" "] * 3 for i in range(3)]
current_turn = 1


def get_current_player():
    global current_turn
    return "X" if current_turn % 2 == 1 else "O"


def show_board():
    global board

    print("  1 2 3")
    for i, row in enumerate(board):
        print(f"{i + 1}│{row[0]}│{row[1]}│{row[2]}│")
    return True


def handle_input_data(input_data):
    global board

    input_data = input_data.split()

    if len(input_data) != 2:
        print("неверное количество координат")
        return ""

    if input_data[0] not in {"1", "2", "3"} or input_data[1] not in {"1", "2", "3"}:
        print("координаты должны быть числами от 1 до 3")
        return ""

    input_data = tuple([int(i) - 1 for i in input_data])

    if board[input_data[0]][input_data[1]] != " ":
        print("данная клетка занята")
        return ""
    return input_data


def prompt_coords():
    input_data = ""
    while not input_data:
        input_data = handle_input_data(input("введите через пробел координаты клетки, строка слева\n"))
    return input_data


def make_move(coords):
    global board, current_turn
    board[coords[0]][coords[1]] = get_current_player()
    current_turn = current_turn + 1


def is_win(line_set):
    return len(line_set) == 1 and line_set != {" "}


def get_winner():
    global board

    for row in board:
        row = set(row)
        if is_win(row):
            return row.pop()

    for j in range(3):
        column = {board[i][j] for i in range(3)}
        if is_win(column):
            return column.pop()

    diagonal = {board[i][i] for i in range(3)}
    if is_win(diagonal):
        return diagonal.pop()

    diagonal = {board[i][2 - i] for i in range(3)}
    if is_win(diagonal):
        return diagonal.pop()
    return False


def check_draw_con():
    global current_turn

    if current_turn > 9:
        return True
    return False


while True:
    show_board()
    print(f"ходит {get_current_player()}")
    make_move(prompt_coords())
    winner = get_winner()
    if winner:
        show_board()
        print(f"{winner} выиграл")
        quit()
    elif check_draw_con():
        show_board()
        print("ничия")
        quit()
