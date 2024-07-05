"""
A module providing a representation of a chess board. The rules of chess are not implemented - 
this is just a "dumb" board that will let you move pieces around as you like.
"""

from chessington.engine.data import Player, Square
from chessington.engine.pieces import Pawn, Knight, Bishop, Rook, Queen, King
from chessington.ui.PromotionUI import promotion_window
BOARD_SIZE = 8


class Board:
    """
    A representation of the chess board, and the pieces on it.
    """

    def __init__(self, player, board_state):
        self.current_player = Player.WHITE
        self.board = board_state
        self.last_piece_moved = None

    @staticmethod
    def empty():
        return Board(Player.WHITE, Board._create_empty_board())

    @staticmethod
    def at_starting_position():
        return Board(Player.WHITE, Board._create_starting_board())

    @staticmethod
    def _create_empty_board():
        return [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    @staticmethod
    def _create_starting_board():

        # Create an empty board
        board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

        # Setup the rows of pawns
        board[1] = [Pawn(Player.WHITE) for _ in range(BOARD_SIZE)]
        board[6] = [Pawn(Player.BLACK) for _ in range(BOARD_SIZE)]

        # Setup the rows of pieces
        piece_row = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        board[0] = list(map(lambda piece: piece(Player.WHITE), piece_row))
        board[7] = list(map(lambda piece: piece(Player.BLACK), piece_row))

        return board

    def set_piece(self, square, piece):
        """
        Places the piece at the given position on the board.
        """
        self.board[square.row][square.col] = piece

    def get_piece(self, square):
        """
        Retrieves the piece from the given square of the board.
        """
        return self.board[square.row][square.col]

    def find_piece(self, piece_to_find):
        """
        Searches for the given piece on the board and returns its square.
        """
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] is piece_to_find:
                    return Square.at(row, col)
        raise Exception('The supplied piece is not on the board')

    def move_piece(self, from_square, to_square):
        """
        Moves the piece from the given starting square to the given destination square.
        """
        moving_piece = self.get_piece(from_square)
        is_square_empty = self.get_piece(to_square) is None
        if moving_piece is not None and moving_piece.player == self.current_player:
            self.set_piece(to_square, moving_piece)
            self.set_piece(from_square, None)
            self.last_piece_moved = moving_piece
            if isinstance(moving_piece, Pawn) and abs(to_square.row - from_square.row) == 2:
                moving_piece.has_moved_2 = 1
            if isinstance(moving_piece, Pawn) and abs(to_square.col - from_square.col) == 1 and abs(to_square.row - from_square.row) == 1 and is_square_empty is True:
                self.set_piece(Square.at(from_square.row, to_square.col), None)
            self.current_player = self.current_player.opponent()
        if isinstance(moving_piece, Pawn) is True and (to_square.row == 7 or to_square.row == 0):
            self.set_piece(to_square, None)
            #promotion_window(moving_piece.player)
            queen = Queen(moving_piece.player)
            self.set_piece(to_square,queen)

    @staticmethod
    def is_inside_bounds(square : Square) -> bool:
        """
        Checks if the given square is inside the bounds of the board
        """
        return 0 <= square.row < BOARD_SIZE and 0 <= square.col < BOARD_SIZE

    def is_in_check (self, player, checked_square: Square) -> bool:
        all_available = []
        for i in range(0,BOARD_SIZE):
            for j in range(0, BOARD_SIZE):
                current_square = Square.at(i, j)
                piece = self.get_piece(current_square)
                if piece is not None and piece.player != player:
                    all_available.extend(piece.get_available_moves())
        return checked_square in all_available