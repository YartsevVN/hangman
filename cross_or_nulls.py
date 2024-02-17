def cross_or_nulls(first_step):
    def printing():
        for i in board_with_nums:
            print(*i)

    def win(board):
        for i in range(len(board)):
            if board[i][1] == board[i][3] and board[i][3] == board[i][5] and (board[i][1] == 'X' or board[i][1] == 'O'):
                return True
        if board[1][1] == board[3][3] and board[3][3]== board[5][5] and (board[1][1] == 'X' or board[1][1] == 'O'):
            return True
        if board[1][5] == board[3][3] and board[3][3] == board[5][1] and (board[1][5] == 'X' or board[1][5] == 'O'):
            return True
        for i in range(1, 6, 2):
            if board[1][i] == board[3][i] and board[3][i] == board[5][i] and (board[1][i] == 'X' or board[1][i] == 'O'):
                return True
        return False
    
    used = []
    board_with_nums =[[' '," "," | "," "," | ",' '],
                      [' ',"7"," | ","8"," | ",'9'],
                      ['___',' |','___','|','___'],
                      [' ',"4"," | ","5"," | ",'6'],
                      ['___',' |','___','|','___'],
                      [' ',"1"," | ","2"," | ",'3'],
                      [' '," "," | "," "," | ",' ']]
    ch = first_step
    def change():
        if ch == 'O':
            return 'X'
        return 'O'
    step = 0
    printing()
    while not win(board_with_nums):
        n = input(f'В какую ячейку поставить {ch}?\n')
        if (n.isdigit) and (n not in used) and (step < 9):
            used.append(n)
            for i in range(len(board_with_nums)):
                for j in range(len(board_with_nums[i])):
                    if n == board_with_nums[i][j]:
                        board_with_nums[i][j] = ch
                        if win(board_with_nums):
                            print(f'Игра окончена, {ch}-и победили!')
                            break
                        ch = change()
                        step += 1
                        printing()
                        
        else:
            print('Повторите попытку')
        if step == 9:
            print('Ничья!')
            exit()

play = input('Хотите сыграть? (да или нет)')
while play == 'да':
    first_step = input('Игрок1, за кого вы хотите играть - X или O? ')
    sootv = (first_step == "X" or first_step == "O")
    while not sootv:
        print('Повторите попытку')
        first_step = input('Игрок1, за кого вы хотите играть - X или O? ')
        sootv = (first_step in ['X', 'O'])
    cross_or_nulls(first_step)
    play = input('Хотите сыграть? (да или нет)')

print('Игра окончена')
