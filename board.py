class Board:
    def __init__(self):
        self.board = []
        for col in range(10):
            self.board.append([])
            for row in range(10):
                self.board[col].append('')

    def updateBoard(self):
        for col in range(len(self.board)):
            print(f"{''.join('[X]' if item else '[ ]' for item in self.board[col])}")


player = Board()
player.updateBoard()