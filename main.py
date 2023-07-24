from TicTacToeLogic import *
from graphic import *
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
    ai_node = Node(gameboard,size)
    while  not ai_node.Terminal() and not node1.Terminal() and gameover == False:
        row, col = input("Podaj rzad i kolumne gdzie chcesz wstawic znak:").split(' ')
        row = int(row)
        col = int(col)
        node1.FillCords(row,col)
        if player == 'x':
            node1.gameboard[row][col] = CROSS
        else:
            node1.gameboard[row][col] = DOT
        print(node1.gameboard)
        tmp_node = minimax(node1, depth,-10000,10000, Player)
        node1.gameboard = tmp_node[0]
        node1.gamescore = tmp_node[1]
        ai_node.gameboard = tmp_node[0]
        ai_node.cords = tmp_node[2]
        print(node1.gameboard)
        if node1.isEnd():
            gameover = True



if __name__ == "__main__":
    main()
