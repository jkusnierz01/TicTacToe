import math
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
        row_indexes = [(3 * self.cords[0]) + y for y in range(3)]  # list of row indexes
        col_indexes = [3 * y + self.cords[1] for y in range(3)]  # list of column indexes
        first_diagonal = [self.board[2], self.board[4], self.board[6]]
        second_diagonal = [self.board[0], self.board[4], self.board[8]]
        row = [self.board[x] for x in row_indexes]
        col = [self.board[x] for x in col_indexes]
        # check the row and column
        if all(s == mark for s in row):  # we check if in row we have all 3 marks
            return True
        elif all(s == mark for s in col):
            return True

        elif all(s == mark for s in first_diagonal):
            return True
        elif all(s == mark for s in second_diagonal):
            return True
        else:
            return False


    def make_move(self, mark):
        while self.prepare_move():
            index = int(self.cords[0] * 3 + self.cords[1])
            self.board[index] = mark
            self.print_board()
            return

    def check_draw(self):
        if self.num_moves() == 0:
            return True
        return False

    def num_moves(self):
        number = 0
        for x in self.board:
            if x == ' ':
                number = number + 1
        return number


    def game(self, player_one,player_two):
        self.print_board()
        while True:
            move_index = player_one.check_move(self)
            self.board[move_index] = player_one.mark
            self.print_board()
            if self.winner(player_one.mark):
                print(f"Player {player_one.mark} won!")
                return True
            if self.check_draw():
                print("Draw!")
                return True
            values_dict = player_two.minimax(self, player_one.mark, 5)
            self.board[values_dict['position']] = player_two.mark
            self.print_board()
            if self.winner(player_two.mark):
                print(f"Player {player_two.mark} won!")
                return True
            if self.check_draw():
                print("Draw!")
                return True











@dataclass
class Player:
    mark: str  # 'x' or 'o'

class HumanPlayer(Player):

    def possible_moves(self, board):
        return [index for index, elem in enumerate(board.board) if elem == ' ']

    def check_move(self, board):
        valid_move = False
        while not valid_move:
            cord_x = int(input("Pass row in which you want to place your mark (0-2): "))
            cord_y = int(input("Pass column in which you want to place your mark (0-2): "))
            index = int(cord_x * 3 + cord_y)
            try:
                if index not in self.possible_moves(board):
                    raise ValueError
                valid_move = True
                board.cords[0] = int(cord_x)
                board.cords[1] = int(cord_y)
            except ValueError:
                print("This spot is already used! Try again!")
        return index

# we want ComputerPlayer's mark to be 'o'
class ComputerPlayer(Player):

    # we hand over 2 arguments:
    #   - actual board
    #   - and minimax player's mark
    #
    # ComputerPlayer => 'o' - min_player
    # HumanPlayer => 'x' - max_player
    def minimax(self, board, player_mark, depth):
        value_list = list()
        f_player_mark = player_mark
        other_player_mark = 'x' if f_player_mark == 'o' else 'o'
        possible_moves = [index for index, elem in enumerate(board.board) if elem == ' ']
        if board.winner(other_player_mark):
            if other_player_mark == 'o':
                return {'position': None, 'score': -1 * board.num_moves()}
            else:
                return {'position': None, 'score': 1 * board.num_moves()}
        if depth == 0 or possible_moves == []:
            return {'position': None, 'score': 0}
        player = other_player_mark
        if f_player_mark == 'o':  # this player wants to minimalize the value - ComputerPlayer - mark 'o'
            value = math.inf
            for move in possible_moves:
                board.board[move] = f_player_mark
                values_dict = self.minimax(board, player, depth - 1)
                board.board[move] = ' '
                value_list.append(values_dict['score'])
                value = min(value, values_dict['score'])
        if f_player_mark == 'x':  # this player wants to maximize the value
            value = -math.inf
            for move in possible_moves:
                board.board[move] = f_player_mark
                values_dict = self.minimax(board, player, depth - 1)
                board.board[move] = ' '
                value_list.append(values_dict['score'])
                value = max(value, values_dict['score'])
        index = value_list.index(value)
        best = {'position': possible_moves[index], 'score': value}
        return best
#       - nie możemy tego w ten sposob zwracac bo przez to
#                                       zamiast wyniku oceny danego boarda robi nam sie zwrotka konkretnego indeksu ruchy
#       musimy znalezc sposob zeby normalnie zwracac wycene danego boarda i jednoczesnie pozniej przekazac najlepszy
#       ruch dla ktorego dana wartosc zostala wyceniona


board = Board()
Human = HumanPlayer('x')
Computer = ComputerPlayer('o')
board.game(Human, Computer)



