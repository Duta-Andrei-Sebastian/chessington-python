from __future__ import annotations
from abc import ABC, abstractmethod
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
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board) -> List[Square]:
        available_moves = []
        current_square = board.find_piece(self)
        if self.player == Player.BLACK:
            square_in_front = Square.at(current_square.row - 1, current_square.col)
            square_2_in_front = Square.at(current_square.row - 2, current_square.col)
            square_left_front = Square.at(current_square.row - 1, current_square.col - 1)
            square_right_front = Square.at(current_square.row - 1, current_square.col + 1)

            if board.is_inside_bounds(square_in_front) is True and board.get_piece(square_in_front) is None:
                available_moves.append(square_in_front)
                if current_square.row == 6 and board.get_piece(square_2_in_front) is None:
                    available_moves.append(square_2_in_front)
            if board.is_inside_bounds(square_left_front) and board.get_piece(square_left_front) is not None:
                if board.get_piece(square_left_front).player == Player.WHITE:
                    available_moves.append(square_left_front)
            if board.is_inside_bounds(square_left_front) and board.get_piece(square_right_front) is not None:
                if board.get_piece(square_right_front).player == Player.WHITE:
                    available_moves.append(square_right_front)

            return available_moves
        else:
            square_in_front = Square.at(current_square.row + 1, current_square.col)
            square_2_in_front = Square.at(current_square.row + 2, current_square.col)
            square_left_front = Square.at(current_square.row + 1, current_square.col - 1)
            square_right_front = Square.at(current_square.row + 1, current_square.col + 1)

            if board.is_inside_bounds(square_in_front) is True and board.get_piece(square_in_front) is None:
                available_moves.append(square_in_front)
                if current_square.row == 1 and board.get_piece(square_2_in_front) is None:
                    available_moves.append(square_2_in_front)
            if board.is_inside_bounds(square_left_front) and board.get_piece(square_left_front) is not None:
                if board.get_piece(square_left_front).player == Player.BLACK:
                    available_moves.append(square_left_front)
            if board.is_inside_bounds(square_left_front) and board.get_piece(square_right_front) is not None:
                if board.get_piece(square_right_front).player == Player.BLACK:
                    available_moves.append(square_right_front)

            return available_moves


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []
