class Board:
    def __init__(self):
        self.board = []
        for x in range(10):
            self.board.append([])
            for y in range(10):
                self.board[x].append([])

player = Board()