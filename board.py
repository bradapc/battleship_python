class GameHandler:
    def __init__(self):
        self.player = player_board
        self.enemy = enemy_board
        self.battleship_ships = {
            'Carrier': 5,
            'Battleship': 4,
            'Cruiser':	3,
            'Submarine': 3,
            'Destroyer': 2 
        }

    def updateBoards(self):
        self.player.updateBoard()
        self.enemy.updateBoard()

    def beginInitializeBoard(self):
        for key in self.battleship_ships:
            while True:
                print(f"Enter col coord for your {key} [{self.battleship_ships[key]}].")
                col = input()
                print(f"Enter row coord for your {key} [{self.battleship_ships[key]}].")
                row = input()
                try:
                    coords = (int(col), int(row))
                    coordinate_list = []
                    for i in range(self.battleship_ships[key]):
                        coordinate_list.append((coords[0] + i, coords[1]))
                    if(self.checkInitialShipCoords(coordinate_list, self.battleship_ships[key], self.player)):
                        print(f"{key} placed at {coords}.")
                        self.player.ships.append(Ship(True, self.battleship_ships[key], coordinate_list))
                        self.updateBoards()
                        break
                    else:
                        print("Incorrect placement.")
                        continue
                except:
                    continue

    def checkInitialShipCoords(self, coordinate_list, len, board_entity):
        for c_pair in coordinate_list:
            try:
                if(board_entity.board[c_pair[0]][c_pair[1]]):
                    return False
            except:
                return False
        return True


class Board:
    def __init__(self, player):
        self.player = player
        self.ships = []
        self.board = []
        self.enemy = ''
        for col in range(10):
            self.board.append([])
            for row in range(10):
                self.board[col].append('')
        self.updateBoard()

    def updateBoard(self):
        print("")
        if(self.player):
            print("PLAYER")
        else:
            print("AI")
        print("   0  1  2  3  4  5  6  7  8  9")
        for col in range(len(self.board)):
            print(f"{col} {''.join(f'[{item}]' if item else '[ ]' for item in self.board[col])}")

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
    def __init__(self, is_player, length, coordinate_list):
        self.is_player = is_player
        self.length = length
        self.coordinate_list = coordinate_list
        self.alive = True
        self.coordinates = None
        if(self.is_player):
            self.board_entity = player_board
        else:
            self.board_entity = enemy_board
        self.placeShip(coordinate_list)
    
    def placeShip(self, coordinate_list):
        self.coordinates = coordinate_list
        for c_pair in coordinate_list:
            self.board_entity.board[c_pair[0]][c_pair[1]] = 'X'
        self.board_entity.updateBoard()

    def isShipAlive(self):
        hp = self.length
        for coord in self.coordinates:
            if(self.board_entity.board[coord[0]][coord[1]]) == '*':
                hp -= 1
        if(hp > 0):
            return True
        return False

if __name__ == '__main__':
    player_board = Board(player=True)
    enemy_board = Board(player=False)
    game = GameHandler()
    player_board.enemy = enemy_board.board
    enemy_board.enemy = player_board.board
    game.beginInitializeBoard()