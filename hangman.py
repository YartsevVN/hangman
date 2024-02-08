from random import choice as c
def hangman(word: str):
    wrong = 0
    stages = ["",
              "_____     ",
              "|    |     ",
              "|    0     ",
              "|   /|\    ",
              "|   / \    ",
              "|_         ",
              ]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print('Добро пожаловать в игру')

    while wrong < len(stages) - 1:
        print('\n')
        char = input("Введите букву: ")
        if char in rletters:
            char_ind = rletters.index(char)
            board[char_ind] = char
            rletters[char_ind] = "$"
        else:
            wrong += 1
        
        print(" ".join(board))
        print("\n".join(stages[0:wrong+1]))
        if "_" not in board:
            print(f'Вы выиграли! Было загадано слово {word}')
            print("Ваш приз - 🎁")
            win = True
            break

    if not win:
        print("/n".join(stages))
        print(f"Вы проиграли! Было загадано слово {word}")


list_words = ['кот', 'собака', 'поросёнок', 'обезьяна']

hangman(c(list_words))
