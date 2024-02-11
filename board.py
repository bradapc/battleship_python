import random
from time import sleep

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

    def updateBoards(self, *args):
        self.enemy.updateBoard()
        self.player.updateBoard()
        if(args):
            print("")
            print(args[0])
            print("")

    def beginInitializeBoard(self):
        #Initialize player board
        for key in self.battleship_ships:
            while True:
                print(f"Enter col coord for your {key} [{self.battleship_ships[key]}].")
                col = input()
                print(f"Enter row coord for your {key} [{self.battleship_ships[key]}].")
                row = input()
                print(f"Do you want your {key} horizontal or vertical? (h or v)")
                orientation = input()
                try:
                    coords = (int(col), int(row))
                    coordinate_list = []
                    for i in range(self.battleship_ships[key]):
                        if(orientation.lower() == 'v'):
                            coordinate_list.append((coords[0] + i, coords[1]))
                        elif(orientation.lower() == 'h'):
                            coordinate_list.append((coords[0], coords[1] + i))
                    if(self.checkInitialShipCoords(coordinate_list, self.player)):
                        print(f"{key} placed at {coords}.")
                        self.player.ships.append(Ship(True, self.battleship_ships[key], coordinate_list))
                        self.updateBoards()
                        break
                    else:
                        print("Incorrect placement.")
                        continue
                except:
                    continue
        #Initialize computer board
        for key in self.battleship_ships:
            while True:
                try:
                    coords = (random.randint(0,9), random.randint(0,9))
                    orientation = random.choice(['h', 'v'])
                    coordinate_list = []
                    for i in range(self.battleship_ships[key]):
                        if(orientation == 'h'):
                            coordinate_list.append((coords[0] + i, coords[1]))
                        elif(orientation == 'v'):
                            coordinate_list.append((coords[0], coords[1] + i))
                    if(self.checkInitialShipCoords(coordinate_list, self.enemy)):
                        self.enemy.ships.append(Ship(False, self.battleship_ships[key], coordinate_list))
                        self.updateBoards()
                        break
                    else:
                        continue
                except:
                    continue
        self.playBattleship()

    def checkInitialShipCoords(self, coordinate_list, board_entity):
        for c_pair in coordinate_list:
            try:
                if(board_entity.board[c_pair[0]][c_pair[1]]):
                    return False
            except:
                return False
        return True
    
    def playBattleship(self):
        winner = None
        name_of_winner = ''
        player_turn = True
        while not winner:
            if(player_turn):
                print("Shoot at col coordinate:")
                col = input()
                print("Shoot at row coordinate:")
                row = input()
                try:
                    shot_coords = (int(col), int(row))
                    if(self.enemy.board[shot_coords[0]][shot_coords[1]] not in ["*", "-"]):
                        self.player.fireAtLocation(shot_coords)
                        winner = self.checkForWinner(self.enemy)
                        if winner:
                            name_of_winner = self.player
                        player_turn = False
                        sleep(2)
                    else:
                        print("You've already shot there!")
                except:
                    print("Invalid shot placement.")
            else:
                shot_coords = (random.randint(0,9), random.randint(0,9))
                try:
                    if(self.player.board[shot_coords[0]][shot_coords[1]] not in ["*", "-"]):
                        self.enemy.fireAtLocation(shot_coords)
                        winner = self.checkForWinner(self.player)
                        if winner:
                            name_of_winner = self.enemy
                        player_turn = True
                    else:
                        continue
                except:
                    pass
        self.winGame(name_of_winner)
    
    def winGame(self, name_of_winner):
        if name_of_winner == self.player:
            print("You've won the game!")
        elif name_of_winner == self.enemy:
            print("Robots have taken over.")


    def checkForWinner(self, player):
        for ship in player.ships:
            if(ship.isShipAlive()):
                return False
        return True


class Board:
    def __init__(self, player):
        self.player = player
        self.ships = []
        self.board = []
        self.enemy = None
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
        if(self.player):
            for col in range(len(self.board)):
                print(f"{col} {''.join(f'[{item}]' if item else '[ ]' for item in self.board[col])}")
        else:
            for col in range(len(self.board)):
                print(f"{col} {''.join(f'[{item}]' if item in ["*", "-"] else '[ ]' for item in self.board[col])}")

    def fireAtLocation(self, coords):
        event_report = ''
        match self.enemy[coords[0]][coords[1]]:
            case 'X':
                self.enemy[coords[0]][coords[1]] = '*'
                if(self.player):
                    event_report = f'>>>Hit enemy at {coords[0], coords[1]}!'
                else:
                    event_report = ">>>You've been hit!"
                game.updateBoards(event_report)
            case '':
                self.enemy[coords[0]][coords[1]] = '-'
                if(self.player):
                    event_report = ">>>Shot missed!"
                else:
                    event_report = ">>>AI shot missed!"
                game.updateBoards(event_report)

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