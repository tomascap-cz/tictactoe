def play_game():
    line_a = ["-", "-", "-"]
    line_b = ["-", "-", "-"]
    line_c = ["-", "-", "-"]

    column_a = [line_a[0], line_b[0], line_c[0]]
    column_b = [line_a[1], line_b[1], line_c[1]]
    column_c = [line_a[2], line_b[2], line_c[2]]

    dia_a = [line_a[0], line_b[1], line_c[2]]
    dia_b = [line_a[2], line_b[1], line_c[0]]

    matrix = [line_a, line_b, line_c]

    print(line_a)
    print(line_b)
    print(line_c)

    def update_cols(index):
        return [line_a[index], line_b[index], line_c[index]]

    def update_dias():
        return [line_a[0], line_b[1], line_c[2]], [line_a[2], line_b[1], line_c[0]]

    def player_choice(num):
        if num == 1 or num % 2 != 0:
            player = 1
        else:
            player = 2
        print(f"Player {player}'s turn")
        choice = input("Enter your symbol and the X and Y coordinates of your move (like this: X-2-2): ").upper().split("-")
        coords = [char for char in choice]
        if matrix[int(coords[1]) - 1][int(coords[2]) - 1] == "-":
            try:
                matrix[int(coords[1]) - 1][int(coords[2]) - 1] = coords[0]
            except IndexError:
                print("Invalid user input. The game accepts commands in the format 'symbol'-'X coordinate'-'Y coordinate'.")
            else:
                print(line_a)
                print(line_b)
                print(line_c)
        else:
            print("This field is already filled.")
            choice = input("Enter your symbol and the X and Y coordinates of your move (like this: X-2-2): ").upper().split("-")
    def check_same(*arrays):
        for arr in arrays:
            if arr[0] == arr[1] == arr[2] and arr[0] != "-":
                print(f"Game over - {arr[0]}s win!")
                return False
        return True

    proceed = True
    turn = 1

    while proceed:
        player_choice(turn)
        column_a = update_cols(0)
        column_b = update_cols(1)
        column_c = update_cols(2)
        dia_a, dia_b = update_dias()
        proceed = check_same(line_a, line_b, line_c, column_a, column_b, column_c, dia_a, dia_b)
        turn += 1

    new_play = input("Play again? (enter 'y' or 'n'): ")
    if new_play == 'y':
        play_game()
    else:
        print("Thanks for playing!")

play_game()
