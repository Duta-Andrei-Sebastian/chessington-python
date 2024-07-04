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
        possible_squares = self.get_possible_squares(board, current_square)
        if self.player == Player.BLACK:
            starting_row = 6
            starting_color = Player.BLACK
        else:
            starting_row = 1
            starting_color = Player.WHITE

        if board.is_inside_bounds(possible_squares[0]) is True and board.get_piece(possible_squares[0]) is None:
            available_moves.append(possible_squares[0])
            if board.is_inside_bounds(possible_squares[1]) is True and board.get_piece(possible_squares[1]) is None:
                if self.player == starting_color and current_square.row == starting_row:
                    available_moves.append(possible_squares[1])

        for i in (2,3):
            if board.is_inside_bounds(possible_squares[i]) is True and board.get_piece(possible_squares[i]) is not None:
                if board.get_piece(possible_squares[i]).player != self.player:
                    available_moves.append(possible_squares[i])

        return available_moves

    def get_possible_squares(self, board, current_square):
        possible_squares = []
        if board.get_piece(current_square).player == Player.BLACK:
            possible_squares.append(Square.at(current_square.row - 1, current_square.col))  # 1 up -> 0
            possible_squares.append(Square.at(current_square.row - 2, current_square.col))  # 2 up -> 1
            possible_squares.append(Square.at(current_square.row - 1, current_square.col - 1))  # take left -> 2
            possible_squares.append(Square.at(current_square.row - 1, current_square.col + 1))  # take right -> 3
        else:
            possible_squares.append(Square.at(current_square.row + 1, current_square.col))
            possible_squares.append(Square.at(current_square.row + 2, current_square.col))
            possible_squares.append(Square.at(current_square.row + 1, current_square.col - 1))
            possible_squares.append(Square.at(current_square.row + 1, current_square.col + 1))

        return possible_squares


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        available_moves = []
        current_square = board.find_piece(self)
        possible_squares = self.get_possible_squares(board, current_square)

        for square in possible_squares:
            if board.get_piece(square) is None:
                available_moves.append(square)
            elif board.get_piece(square).player != self.player:
                available_moves.append(square)

        return available_moves

    def get_possible_squares(self, board, current_square):
        possible_squares = []
        possible_squares.append(Square(current_square.row - 1, current_square.col - 2))
        possible_squares.append(Square.at(current_square.row + 1, current_square.col - 2))
        possible_squares.append(Square.at(current_square.row + 2, current_square.col - 1))
        possible_squares.append(Square.at(current_square.row + 2, current_square.col + 1))
        possible_squares.append(Square.at(current_square.row + 1, current_square.col + 2))
        possible_squares.append(Square.at(current_square.row - 1, current_square.col + 2))
        possible_squares.append(Square.at(current_square.row - 2, current_square.col + 1))
        possible_squares.append(Square.at(current_square.row - 2, current_square.col - 1))
        return self.get_legal_squares(board, possible_squares)

    def get_legal_squares(self, board, possible_squares):
        legal_squares = []
        for square in possible_squares:
            if board.is_inside_bounds(square) is True:
                legal_squares.append(square)
        return legal_squares


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
