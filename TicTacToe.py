import copy
import numpy as np
from collections import deque

CROSS = 1
DOT = -1
PLAYER_CROSS = True
PLAYER_DOT = False


# player True - max - krzyzyk
# player Flase - min - kolko

class Node:
    def __init__(self, gamestate, boardsize):
        self.size = boardsize
        self.gameboard = gamestate
        self.gamescore = 0
        self.cords = [0,0]
        self.gameend = False


    def FillCords(self, x_cord, y_cord):
        self.cords[0] = x_cord
        self.cords[1] = y_cord
    def IsInTable(self, x_cord, y_cord):
        if x_cord < 0 or x_cord > self.size - 1:
            return False
        elif y_cord < 0 or y_cord > self.size - 1:
            return False
        return True

    def isEnd(self):
        tmp = 0
        for x in range(self.size):
            for y in range(self.size):
                if self.gameboard[x][y] != 0:
                    tmp = tmp + 1
        if tmp == self.size*self.size:
            return True
        elif tmp != self.size*self.size:
            return False


    # metoda w ktorej opisane sa wszystkie warunki zwycieztwa dla planszy 3x3
    def Terminal(self):
        winning = 4
        tmp = 0
        char_list_row = []
        char_list_col = []
        char_list_one = []
        char_list_two = []
        row = self.cords[0]
        col = self.cords[1]
        # print(str(row) +" " +  str(col))
        for i in range(self.size):
            char_list_row.append(self.gameboard[row][i])
            char_list_col.append(self.gameboard[i][col])
        if char_list_row.count(CROSS) >= winning:
            if checkk_numbers(char_list_row):
                self.gamescore = CROSS
                return True
        if char_list_row.count(DOT) >= winning:
            if checkk_numbers(char_list_row):
                self.gamescore = DOT
                return True
        if char_list_col.count(CROSS) >= winning:
            if checkk_numbers(char_list_col):
                print(char_list_col)
                self.gamescore = CROSS
                return True
        if char_list_col.count(DOT) >= winning:
            if checkk_numbers(char_list_col):
                self.gamescore = DOT
                return True
        # to bylo sprawdzenie czy zwyciestwo kolka czy krzyzyka po ruchu w tej samej kolumnie albo wierszu

        #sprawdzenie przekatnych
        char_list_one.append(self.gameboard[row][col])
        char_list_two.append(self.gameboard[row][col])
        for x in range(1,5):
            if self.IsInTable(row - x, col - x):
                char_list_one.append(self.gameboard[row-x][col-x])
            if self.IsInTable(row + x, col + x):
                char_list_one.append(self.gameboard[row + x][col + x])
            if self.IsInTable(row - x, col + x):
                char_list_two.append(self.gameboard[row-x][col+x])
            if self.IsInTable(row + x, col - x):
                char_list_two.append(self.gameboard[row + x][col - x])
        if char_list_one.count(CROSS) >= winning:
            if checkk_numbers(char_list_one):
                self.gamescore = CROSS
                return True
        if char_list_one.count(DOT) >= winning:
            if checkk_numbers(char_list_one):
                self.gamescore = DOT
                return True
        if char_list_two.count(CROSS) >= winning:
            if checkk_numbers(char_list_two):
                self.gamescore = CROSS
                return True
        if char_list_two.count(DOT) >= winning:
            if checkk_numbers(char_list_two):
                self.gamescore = DOT
                return True
        self.gamescore = 0
        return False



        # tmp = 0
        # for x in range(self.size):
        #     if self.gameboard[x][0] == CROSS and self.gameboard[x][1] == CROSS and self.gameboard[x][2] == CROSS:
        #         self.gamescore = CROSS
        #         return True
        #     elif self.gameboard[x][0] == DOT and self.gameboard[x][1] == DOT and self.gameboard[x][2] == DOT:
        #         self.gamescore = DOT
        #         return True
        #     elif self.gameboard[0][x] == CROSS and self.gameboard[1][x] == CROSS and self.gameboard[2][x] == CROSS:
        #         self.gamescore = CROSS
        #         return True
        #     elif self.gameboard[0][x] == DOT and self.gameboard[1][x] == DOT and self.gameboard[2][x] == DOT:
        #         self.gamescore = DOT
        #         return True
        # if self.gameboard[0][0] == DOT and self.gameboard[1][1] == DOT and self.gameboard[2][2] == DOT:
        #     self.gamescore = DOT
        #     return True
        # elif self.gameboard[0][2] == DOT and self.gameboard[1][1] == DOT and self.gameboard[2][0] == DOT:
        #     self.gamescore = DOT
        #     return True
        # elif self.gameboard[0][0] == CROSS and self.gameboard[1][1] == CROSS and self.gameboard[2][2] == CROSS:
        #     self.gamescore = CROSS
        #     return True
        # elif (int(self.gameboard[0][2]) == CROSS and int(self.gameboard[1][1]) == CROSS and int(
        #         self.gameboard[2][0]) == CROSS):
        #     self.gamescore = CROSS
        #     return True
        # for x in range(self.size):
        #     for y in range(self.size):
        #         if self.gameboard[x][y] != 0:
        #             tmp = tmp + 1
        # if tmp == 9:
        #     self.gamescore = 2
        #     return True
        # elif tmp != 9:
        #     self.gamescore = 0
        #     return False

#metoda sprawdzajaca czy nastepuja po sobie 4 takie same liczby
def checkk_numbers(lst):
    winning = 4
    diffs = np.diff(lst) #zwraca liste ktora zawiera roznice miedzy kolejnymi elementami
    if np.count_nonzero(diffs == 0) > winning - 2:
        return True
    return False




def CreateGraph(node: Node, player: bool):
    graph = deque()
    for x in range(node.size):
        for y in range(node.size):
            if node.gameboard[x][y] == 0:
                if player == PLAYER_DOT:
                    node.gameboard[x][y] = DOT
                    node.cords[0] = (int(x))
                    node.cords[1] = (int(y))
                    tmp_node = copy.deepcopy(node)
                    graph.append(tmp_node)
                    node.gameboard[x][y] = 0
                elif player == PLAYER_CROSS:
                    node.gameboard[x][y] = CROSS
                    node.cords[0] = (int(x))
                    node.cords[1] = (int(y))
                    tmp_node = copy.deepcopy(node)
                    graph.append(tmp_node)
                    node.gameboard[x][y] = 0
    return graph




def minimax(node: Node, dept: int, player: bool) -> Node:
    new_node = copy.deepcopy(node)
    if new_node.Terminal() == True or dept == 0:
        return new_node.gameboard,new_node.gamescore
    graph = CreateGraph(new_node, player)
    if player == PLAYER_DOT:
        value = 1000
        tmp_player = not player
        for item in graph:
            tmp = minimax(item, dept - 1, tmp_player)
            item.gamescore = tmp[1]
            value = min(value, tmp[1])
    elif player == PLAYER_CROSS:
        value = -1000
        tmp_player = not player
        for item in graph:
            tmp = minimax(item, dept - 1, tmp_player)
            item.gamescore = tmp[1]
            value = max(value, tmp[1])
    for item in graph:
        if item.gamescore == value:
            return item.gameboard, item.gamescore




def main():
    gameover = False
    # True - krzyżyk; Flase - kółko
    size = int(input("Podaj rozmiar planszy (size x size): "))
    depth = int(input("Podaj glebokosc: "))
    player = input("Wybierz gracza (x lub o):")
    if player == 'x':
        Player = PLAYER_DOT
    else:
        Player = PLAYER_CROSS
    rows, cols = (size, size)
    gameboard = np.zeros((rows, cols))
    node1 = Node(gameboard, size)
    while node1.gamescore == 0 and gameover == False:
        row, col = input("Podaj rzad i kolumne gdzie chcesz wstawic znak:").split(' ')
        row = int(row)
        col = int(col)
        node1.FillCords(row,col)
        if player == 'x':
            node1.gameboard[row][col] = CROSS
        else:
            node1.gameboard[row][col] = DOT
        print(node1.gameboard)
        tmp_node = minimax(node1, depth, Player)
        node1.gameboard = tmp_node[0]
        node1.gamescore = tmp_node[1]
        print(node1.gameboard)
        print(node1.gamescore)
        if node1.isEnd():
            gameover = True



if __name__ == "__main__":
    main()
