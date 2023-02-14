from chess.chess import *


def process(str_move, board, turn):

    if str_move == "0-0":
        pass
    if str_move == "0-0-0":
        pass


    # Tokenize
    tokenized = []
    for i in str_move:
        if i in "1234567890":
            tokenized[-1] += i
        else:
            tokenized.append(i)
    
    piece_char = None
    d_file = None
    d_rank = None
    for i in tokenized:
        if len(i) == 1:
            if i == "x":
                continue
            if i in "abcdefgh":
                d_rank = i
            if i in ["R", "N", "B", "Q", "K"]:
                piece_char = i
        if len(i) == 2:
            if i[0:1] in ["R", "N", "B", "Q", "K"]:
                piece_char = i
                d_file = i[1:2]
            if i[0] in "abcdefgh" and i[1] in "12345678":
                position = locate(i)
    if piece_char is None:
        piece_char = "P"

    # Get all possible pieces
    possible_pieces = [piece for piece in board.pieces[turn] 
            if piece.is_valid(position)\
            and piece.char == piece_char]
    if d_file is not None:
        possible_pieces = [piece for piece in possible_pieces
                if "12345678"[piece.position.row] == d_file]
    if d_rank is not None:
        possible_pieces = [piece for piece in possible_pieces
                if "abcdefgh"[piece.position.col] == d_rank]
    if len(possible_pieces) != 1:
        raise ValueError("Your move specifies {0} possible moves.".format(
            len(possible_pieces)))
    return Move(possible_pieces[0], position)

class Game:
    def __init__(self):
        self.board = Board()

        while True:
            print(self.board)
            print("Player {0}'s turn".format(self.board.turn))
            move = process(input("Make your move: "), self.board)
            self.board.make_move(move)
