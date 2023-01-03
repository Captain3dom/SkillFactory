def greeting():
    print('-----------------------------------------')
    print('|               Welcome!                |')
    print('|           You are playing             |')
    print('|             tic-tac-toe               |')
    print('|---------------------------------------|')
    print('|                Rules:                 |')
    print('| Enter coordinated of enpty cell: x y  |')
    print('|        x - Horizontal coorinate       |')
    print('|        y - Vertical Coordinate        |')
    print('-----------------------------------------')

def show():
    print()
    print('    | 0 | 1 | 2 | ')
    print('-----------------')
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '. join(row)} | "
        print(row_str)
        print("-----------------")
    print()

def ask():
    while True:
        cords = input("             Your move: ").split()

        if len(cords) != 2:
            print("Please input 2 coordinates")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Please input digits! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Coordinates are out of range!")
            continue

        if field [x] [y]  != " ":
            print("The cell is occupied ")
            continue
        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)),
                ((1, 0), (1, 1), (1, 2)),
                ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)),
                ((0, 0), (1, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)),
                ((0, 2), (1, 2), (2, 2)))

    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("The winner is - X - !")
            return True
        if symbols == ["O", "0", "0"]:
            print("The winner is - 0 - !")
            return True
    return False

greeting()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
       print("'X' Moves!")
    else:
        print("'0' Moves!")

    x, y = ask()
    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print("Draw!")
        break
