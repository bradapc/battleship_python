class GameHandler:
    def __init__(self, player, enemy):
        self.player = player_board
        self.enemy = enemy_board
    def updateBoards(self):
        self.player.updateBoard()
        self.enemy.updateBoard()


class Board:
    def __init__(self, player):
        self.player = player
        self.board = []
        self.enemy = ''
        for col in range(10):
            self.board.append([])
            for row in range(10):
                self.board[col].append('')
        self.updateBoard()

    def updateBoard(self):
        if(self.player):
            print("---PLAYER BOARD---")
        else:
            print("---AI BOARD---")
        for col in range(len(self.board)):
            print(f"{''.join(f'[{item}]' if item else '[ ]' for item in self.board[col])}")

    def fireAtLocation(self, coords):
        match self.enemy[coords[0]][coords[1]]:
            case 'X':
                self.enemy[coords[0]][coords[1]] = '*'
                game.updateBoards()
                print(f'Hit at {coords[0], coords[1]}!')
            case '*':
                print("Miss!")
            case '':
                print("Miss!")

class Ship:
    def __init__(self, player, length, pos):
        self.player = player
        self.length = length
        self.pos = pos
        self.alive = True
        if(self.player):
            self.board_entity = player_board
        else:
            self.board_entity = enemy_board
        self.checkInitialShipCoords()

    def checkInitialShipCoords(self):
        #Create a list of coordinates that the ship is expected to take on the board.
        coordinate_list = []
        for i in range(self.length):
            coordinate_list.append((self.pos[0] + i, self.pos[1]))
        #Check the board to see if the coordinates can be placed.
        for c_pair in coordinate_list:
            try:
                if(self.board_entity.board[c_pair[0]][c_pair[1]]):
                    return False
            except:
                return False
        self.placeShip(coordinate_list)
    
    def placeShip(self, coordinate_list):
        for c_pair in coordinate_list:
            self.board_entity.board[c_pair[0]][c_pair[1]] = 'X'
        self.board_entity.updateBoard()

if __name__ == '__main__':
    player_board = Board(player=True)
    enemy_board = Board(player=False)
    game = GameHandler(player_board, enemy_board)
    player_board.enemy = enemy_board.board
    enemy_board.enemy = player_board.board
    destroyer = Ship(True, 5, (4,4))
    destroyer = Ship(False, 5, (4,4))
    player_board.fireAtLocation((4,4))