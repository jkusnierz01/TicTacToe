from TicTacToeLogic import *
from graphic import *
import os

SIZE = 5
DEPTH = 5


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
    while not ai_node.Terminal() and not node1.Terminal() and gameover == False:
        row, col = input("Podaj rzad i kolumne gdzie chcesz wstawic znak:").split(' ')
        row = int(row)
        col = int(col)
        node1.FillCords(row,col)
        if player == 'x':
            node1.gameboard[row][col] = CROSS
        else:
            node1.gameboard[row][col] = DOT
        print(node1.gameboard)
        node1.Terminal(dd=4)
        tmp_node = minimax(node1, depth, -10000, 10000, Player)
        node1.gameboard = tmp_node[0]
        node1.gamescore = tmp_node[1]
        ai_node.gameboard = tmp_node[0]
        ai_node.cords = tmp_node[2]
        print(node1.gameboard)
        if node1.isEnd():
            gameover = True


# True - krzyżyk; Flase - kółko
# def main():
#     gameover = False
#     # player = input("Wybierz gracza (x lub o):")
#     # if player == 'x':
#     #     Player = PLAYER_DOT
#     # else:
#     #     Player = PLAYER_CROSS
#     player = PLAYER_CROSS
#     Player = PLAYER_DOT
#     rows, cols = (SIZE, SIZE)
#     gameboard = np.zeros((rows, cols))
#     node1 = Node(gameboard, SIZE)
#     ai_node = Node(gameboard, SIZE)
#     init_board(x, y)
#     while not ai_node.Terminal() and not node1.Terminal() and gameover is False:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 print(node1.gameboard)
#                 cords = pygame.mouse.get_pos()
#                 aproxed_cords = approx_cords(game_cords_match, cords)
#                 screen.blit(x_mark, aproxed_cords)
#                 pygame.display.update()
#                 tab_tuple = game_cords_match_reverse[aproxed_cords]
#                 node1.FillCords(tab_tuple[0], tab_tuple[1])
#                 if player == PLAYER_CROSS:
#                     node1.gameboard[tab_tuple[0]][tab_tuple[1]] = CROSS
#                 else:
#                     node1.gameboard[tab_tuple[0]][tab_tuple[1]] = DOT
#                 tmp_node = minimax(node1, DEPTH, -10000, 10000, Player)
#                 node1.gameboard = tmp_node[0]
#                 node1.gamescore = tmp_node[1]
#                 ai_node.gameboard = tmp_node[0]
#                 ai_node.cords = tmp_node[2]
#                 ai_cords = tuple(ai_node.cords)
#                 screen.blit(o_mark, game_cords_match[ai_cords])
#                 if node1.isEnd():
#                     gameover = True
#         pygame.display.update()
#         clock.tick(60)  # limits FPS to 60
#     pygame.quit()


if __name__ == "__main__":
    main()
