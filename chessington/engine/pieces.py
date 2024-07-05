from __future__ import annotations
from abc import ABC, abstractmethod

from chessington.engine import board
from chessington.engine.data import Player, Square
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from chessington.engine.board import Board


class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player: Player):
        self.player = player
        self.is_first_move = 0

    @abstractmethod
    def get_available_moves(self, board: Board) -> List[Square]:
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        if self.is_first_move == 0:
            self.is_first_move = 1
        board.move_piece(current_square, new_square)

    def travel_along_directions_continuous(self, board, current_square, directions):
        possible_squares = []
        for direction in directions:
            square = current_square
            invalid_direction = False
            while invalid_direction is False:
                square = Square.at(square.row + direction[0], square.col + direction[1])
                if board.is_inside_bounds(square) is True:
                    if board.get_piece(square) is None:
                        possible_squares.append(square)
                    else:
                        if board.get_piece(square).player != self.player and isinstance(board.get_piece(square), King) is False:
                            possible_squares.append(square)
                        invalid_direction = True
                else:
                    invalid_direction = True
        return possible_squares


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """
    def __init__(self, player: Player):

        super().__init__(player)
        self.has_moved_2 = 0

    def get_available_moves(self, board) -> List[Square]:
        available_moves = []
        current_square = board.find_piece(self)
        possible_squares = self.get_possible_squares(current_square)

        if board.is_inside_bounds(possible_squares[0]) is True and board.get_piece(possible_squares[0]) is None:
            available_moves.append(possible_squares[0])
            if board.is_inside_bounds(possible_squares[1]) is True and board.get_piece(possible_squares[1]) is None:
                if self.is_first_move == 0:
                    available_moves.append(possible_squares[1])

        for i in (2,3):
            if board.is_inside_bounds(possible_squares[i]) is True and board.get_piece(possible_squares[i]) is not None:
                if board.get_piece(possible_squares[i]).player != self.player and isinstance(board.get_piece(possible_squares[i]),King) is False:
                    available_moves.append(possible_squares[i])

        if current_square.row == 4 or current_square.row == 3:
            available_moves = self.check_en_passant(board, current_square, available_moves)
        return available_moves

    def get_possible_squares(self, current_square):
        possible_squares = []
        multiplier = 1
        if self.player == Player.BLACK:
            multiplier = -1
        possible_squares.append(Square.at(current_square.row + multiplier, current_square.col))  # 1 up -> 0
        possible_squares.append(Square.at(current_square.row + 2 * multiplier, current_square.col))  # 2 up -> 1
        possible_squares.append(Square.at(current_square.row + multiplier, current_square.col - 1))  # take left -> 2
        possible_squares.append(Square.at(current_square.row + multiplier, current_square.col + 1))  # take right -> 3
        possible_squares.append(Square.at(current_square.row, current_square.col + 1))
        possible_squares.append(Square.at(current_square.row, current_square.col - 1))

        return possible_squares

    def check_en_passant(self, board, current_square, available_moves):
        multiplier = 1
        if self.player == Player.BLACK:
            multiplier = -1
        pieces = [board.get_piece(Square.at(current_square.row, current_square.col - 1)), board.get_piece(Square.at(current_square.row, current_square.col + 1))]
        square = [Square.at(current_square.row + multiplier, current_square.col - 1), Square.at(current_square.row + multiplier, current_square.col + 1)]
        empty_space = [board.get_piece(square[0]), board.get_piece(square[1])]
        for i in (0,1):
            if pieces[i] is not None and empty_space[i] is None:
                if isinstance(pieces[i], Pawn) is True and pieces[i].has_moved_2 == 1 and board.last_piece_moved == pieces[i] and pieces[i].player != self.player:
                    available_moves.append(square[i])
        return available_moves




class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        directions = [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1]
        return self.travel_along_directions_knight(board, current_square, directions)

    def travel_along_directions_knight(self, board, current_square, directions):
        possible_squares = []
        for direction in directions:
            square = current_square
            square = Square.at(square.row + direction[0], square.col + direction[1])
            if board.is_inside_bounds(square) is True:
                if board.get_piece(square) is None:
                    possible_squares.append(square)
                elif board.get_piece(square).player != self.player and isinstance(board.get_piece(square), King) is False:
                        possible_squares.append(square)
        return possible_squares


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        directions = [-1, -1], [1, 1], [-1, 1], [1, -1]
        return self.travel_along_directions_continuous(board, current_square, directions)


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        directions = [0, -1], [0, 1], [1, 0], [-1, 0]
        directions = [0, -1], [0, 1], [1, 0], [-1, 0]
        return self.travel_along_directions_continuous(board, current_square, directions)

#
class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        directions = [0, -1], [0, 1], [1, 0], [-1, 0], [-1, -1], [1, 1], [-1, 1], [1, -1]
        return self.travel_along_directions_continuous(board, current_square, directions)


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        directions = [0, -1], [0, 1], [1, 0], [-1, 0], [-1, -1], [1, 1], [-1, 1], [1, -1]
        return self.travel_along_directions_king(board, current_square, directions)

    def travel_along_directions_king(self, board, current_square, directions):
        possible_squares = []
        for direction in directions:
            square = current_square
            square = Square.at(square.row + direction[0], square.col + direction[1])
            if board.is_inside_bounds(square) is True:
                if board.get_piece(square) is None:
                    possible_squares.append(square)
                elif board.get_piece(square).player != self.player and isinstance(board.get_piece(square), King) is False:
                        possible_squares.append(square)
        return possible_squares
