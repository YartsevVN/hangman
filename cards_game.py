from random import shuffle

class Card():
    suits = ["пикей",
             "червей",
             "бубей",
             "крестей"]
    values = [None, None, "2", '3', '4', '5', '6', '7', '8', '9', '10', "валета", "даму", "короля", "туза"]
    
    def __init__(self, v, s) -> None:
        self.suit = s
        self.value = v

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    def __repr__(self):
        v = self.values[self.value] + " " +self.suits[self.suit]
        return v

class Deck():
    def __init__(self) -> None:
        self.cards = []
        for v in range(2, 15):
            for s in range(4):
                self.cards.append(Card(v, s))
        shuffle(self.cards)
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
    
class Player():
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game():
    def __init__(self):
        name1 = input("Имя игрока №1: ")
        name2 = input('Имя игрока №2: ')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    
    def wins(self, winner):
        print(f"{winner} забирает карты")

    def draw(self, p1n, p1c, p2n, p2c):
        print(f"{p1n} кладет {p1c}, а {p2n} кладет {p2c}")
    
    def play_game(self):
        cards = self.deck.cards
        print('Поехали!')
        while len(cards) >= 2:
            mes = "Нажмите Х для выхода из игры.\nНажмите любую другую клавишу для начала игры:"
            response = input(mes)
            if response == 'Х':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name

            print(f'{p1n}: {p1c}, {p2n}: {p2c}')
            
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(p1n)
            else:
                self.p2.wins += 1
                self.wins(p2n)
        win = self.winner(self.p1, self.p2)
        print(f"Игра окончена. Выиграл {win}")

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        elif p1.wins < p2.wins:
            return p2.name
        return "Ничья!"
    
game = Game()
game.play_game()