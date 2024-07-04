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
        current_square = board.find_piece(self)
        square_list = []
        if self.player == Player.BLACK and not self.has_piece_in_front(board, current_square):
            square_list.append(Square.at(current_square.row - 1, current_square.col))
            if current_square.row == 6 and not self.has_piece_in_front(board, current_square, distance=2):
                square_list.append(Square.at(current_square.row -2, current_square.col))
        elif not self.has_piece_in_front(board, current_square):
            square_list.append(Square.at(current_square.row + 1, current_square.col))
            if current_square.row == 1 and not self.has_piece_in_front(board, current_square, distance=2):
                square_list.append(Square.at(current_square.row + 2, current_square.col))
        return square_list

    def has_piece_in_front(self, board: Board, current_square, distance=1) -> bool:
        if self.player == Player.BLACK:
            if board.get_piece(Square.at(current_square.row - distance, current_square.col)):
                return True
        else:
            if board.get_piece(Square.at(current_square.row + distance, current_square.col)):
                return True

        return False



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