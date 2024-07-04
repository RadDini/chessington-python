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
        if not self.can_move(board, current_square):
            return square_list

        if self.player == Player.BLACK:
            square_list.append(Square.at(current_square.row - 1, current_square.col))

            if current_square.row == 6 and not self.has_piece_in_front(board, current_square, distance=2):
                square_list.append(Square.at(current_square.row -2, current_square.col))
        else:
            square_list.append(Square.at(current_square.row + 1, current_square.col))
            if current_square.row == 1 and not self.has_piece_in_front(board, current_square, distance=2):
                square_list.append(Square.at(current_square.row + 2, current_square.col))
        square_list += self.get_moves_diag(board, current_square)

        return square_list

    def has_piece_in_front(self, board: Board, current_square, distance=1) -> bool:
        if self.player == Player.BLACK:
            if board.get_piece(Square.at(current_square.row - distance, current_square.col)):
                return True
        else:
            if board.get_piece(Square.at(current_square.row + distance, current_square.col)):
                return True

        return False

    def at_edge(self, square: Square) -> bool:
        if self.player == Player.BLACK:
            if square.row == 0:
                return True
        else:
            if square.row == 7:
                return True

        return False

    def has_piece_diagonal(self, board: Board, square: Square) -> bool:
        if self.player == Player.BLACK:
            diag_left = board.get_piece(Square.at(square.row-1, square.col-1))
            diag_right = board.get_piece(Square.at(square.row-1, square.col+1))

            if (diag_left and diag_left.player == Player.WHITE)\
                    or (diag_right and diag_right.player == Player.BLACK):
                return True
        else:
            diag_left = board.get_piece(Square.at(square.row + 1, square.col - 1))
            diag_right = board.get_piece(Square.at(square.row + 1, square.col + 1))

            if (diag_left and diag_left.player == Player.BLACK) \
                    or (diag_right and diag_right.player == Player.BLACK):
                return True
        return False

    def get_moves_diag(self, board: Board, square: Square) -> List[Square]:
        square_list = []

        if self.player == Player.BLACK:
            diag_left = board.get_piece(Square.at(square.row - 1, square.col - 1))
            diag_right = board.get_piece(Square.at(square.row - 1, square.col + 1))

            if diag_left and diag_left.player == Player.WHITE:
                square_list.append(Square.at(square.row - 1, square.col - 1))
            if diag_right and diag_right.player == Player.WHITE:
                square_list.append(Square.at(square.row - 1, square.col + 1))
        else:
            diag_left = board.get_piece(Square.at(square.row + 1, square.col - 1))
            diag_right = board.get_piece(Square.at(square.row + 1, square.col + 1))

            if diag_left and diag_left.player == Player.BLACK:
                square_list.append(Square.at(square.row + 1, square.col - 1))
            if diag_right and diag_right.player == Player.BLACK:
                square_list.append(Square.at(square.row + 1, square.col + 1))

        return square_list

    def can_move(self, board: Board, square: Square) -> bool:
        if not self.at_edge(square):
            return self.has_piece_diagonal(board, square) or not self.has_piece_in_front(board, square)

        return False



class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        square_list = []

        directions = [(2, 1), (2, -1),
                      (-2, 1), (-2, -1),
                      (1, 2), (1, -2),
                      (-1, 2), (-1, -2)]

        for direction in directions:
            square_to_move = Square.at(current_square.row + direction[0], current_square.col + direction[1])
            if board.is_in_bounds(square_to_move):
                square_list.append(square_to_move)

        return square_list




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