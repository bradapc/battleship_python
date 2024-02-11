class Board:
    def __init__(self, player):
        self.player = player
        self.board = []
        for col in range(10):
            self.board.append([])
            for row in range(10):
                self.board[col].append('')

    def updateBoard(self):
        if(self.player):
            print("---PLAYER BOARD---")
        else:
            print("---AI BOARD---")
        for col in range(len(self.board)):
            print(f"{''.join(f'[{item}]' if item else '[ ]' for item in self.board[col])}")

class Ship:
    def __init__(self, player, length, pos):
        self.player = player
        self.length = length
        self.pos = pos
        if(self.player):
            self.board_entity = player_board
        else:
            self.board_entity = enemy_board

    def checkInitialShipCoords(self):
        #Create a list of coordinates that the ship is expected to take on the board.
        coordinate_list = []
        for i in range(self.length):
            coordinate_list.append((self.pos[0] + i, self.pos[1]))
        #Check the board to see if the coordinates can be placed.
        for c_pair in coordinate_list:
            if(self.board_entity.board[c_pair[0]][c_pair[1]]):
                return False
        self.placeShip(coordinate_list)
    
    def placeShip(self, coordinate_list):
        for c_pair in coordinate_list:
            self.board_entity.board[c_pair[0]][c_pair[1]] = 'X'
        self.board_entity.updateBoard()



#Test Cases
player_board = Board(player=True)
player_board.updateBoard()
enemy_board = Board(player=False)
enemy_board.updateBoard()
destroyer = Ship(True, 5, (3,4))
destroyer.checkInitialShipCoords()