from dataclasses import dataclass


class Board:
    def __init__(self):
        self.board = self.make_board()
        self.__gamescore = 0
        self.cords = [0, 0]

    @staticmethod
    def make_board():
        return [' ' for x in range(9)]

    @property
    def gamescore(self):
        return self.__gamescore

    @gamescore.setter
    def gamescore(self, value):
        self.__gamescore = value

    @gamescore.getter
    def gamescore(self):
        return self.__gamescore

    def print_board(self):
        print("\n")
        print('\t' + " " + '0' + "   " + '1' + "   " + '2')
        for z in range(3):
            print('      ' + str(z) + "  " + self.board[3*z] + " | " + self.board[3*z+1] + " | " + self.board[3*z+2])
            if z < 2:
                print('\t' + "-----------")
        print("\n" + '\n')


    def prepare_move(self):
        self.cords[0] = input("Pass row in which you want to place your mark (0-2): ")
        self.cords[1] = input("Pass column in which you want to place your mark (0-2): ")
        index = int(self.cords[0] * 3 + self.cords[1])
        if self.board[index] != ' ':
            print("This spot is already used! Try again!")
            return False
        else:
            return True



    # musimy przekazywać letter - czyli literke która jest gracz
    def winner(self, mark):
        row = [(3 * self.cords[0]) + y for y in range(3)]  # list of row indexes
        col = [3 * y + self.cords[1] for y in range(3)]  # list of column indexes

        # check the row and column
        if all(s == mark for s in row):  # we check if in row we have all 3 marks
            return True
        elif all(s == mark for s in col):
            return True
        elif self.board[2] == self.board[4] == self.board[6]:
            return True
        elif self.board[0] == self.board[4] == self.board[8]:
            return True
        else:
            return False


    def make_move(self, mark):
        while self.prepare_move():
            index = int(self.cords[0] * 3 + self.cords[1])
            self.board[index] = mark
            self.print_board()
            return




    def game(self, player_one,player_two):
        self.print_board()
        while True:
            self.make_move(player_one.mark)
            if self.winner(player_one.mark):
                print("player one won!")
                return True
            comp_move_index = player_two.minimax()
            self.board[comp_move_index] = player_two.mark
            self.print_board()
            if self.winner(player_two.mark):
                print("Win Player Two")
                return True











@dataclass
class Player:
    mark: str  # 'x' or 'o'

class HumanPlayer(Player):
    pass


class ComputerPlayer(Player):

    def minimax(self, board, player_one):
        player = self.mark
        if board.winner() == True:
            return board.cords
        if player == self.mark:
            value = 1000
            player = player_one.mark
            possible_moves = [index for elem, index in enumerate(self.board) if elem == ' '] # trzeba stworzyć liste indeksów z wszystkimi możliwymi ruchami






lista = [' ' for x in range(9)]
lista[2] = 'x'
poss = [index for elem, index in enumerate(lista) if elem == ' ']
print(poss)
