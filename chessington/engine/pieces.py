from __future__ import annotations

import logging

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List, Tuple, Any

from chessington.engine.data import Player, Square

if TYPE_CHECKING:
    from chessington.engine.board import Board

BOARD_SIZE = 8

logger = logging.getLogger(__name__)
logging.basicConfig(filename='chessington.log', level=logging.DEBUG)


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

    def __init__(self, player: Player):
        super().__init__(player)
        self.has_moved_two = False

    def has_not_moved(self, current_square) -> bool:
        if self.player == Player.BLACK:
            if current_square.row == BOARD_SIZE - 2:
                return True
        else:
            if current_square.row == 1:
                return True
        return False

    def has_piece_in_front(self, board: Board, current_square, distance=1) -> bool:
        if self.player == Player.BLACK:
            distance *= -1

        if board.get_piece(Square.at(current_square.row + distance, current_square.col)):
            return True

        return False

    def at_edge(self, square: Square) -> bool:
        if self.player == Player.BLACK:
            if square.row == 0:
                return True
        elif square.row == BOARD_SIZE - 1:
            return True

        return False

    def get_moves_diagonal(self, board: Board, square: Square) -> List[Square]:
        square_in_front = 1
        square_list = []
        if self.player == Player.BLACK:
            square_in_front = -1

        square_diag_left = Square.at(square.row + square_in_front, square.col - 1)
        square_diag_right = Square.at(square.row + square_in_front, square.col + 1)
        diag_left = None
        diag_right = None

        if board.is_in_bounds(square_diag_left):
            diag_left = board.get_piece(square_diag_left)

        if board.is_in_bounds(square_diag_right):
            diag_right = board.get_piece(square_diag_right)

        if diag_left and diag_left.player != self.player:
            square_list.append(square_diag_left)

        if diag_right and diag_right.player != self.player:
            square_list.append(square_diag_right)

        return square_list

    def get_en_passant(self, board: Board, square: Square) -> Any | None:
        print("in enpassant on square" + str(square))
        square_in_front = 1

        if self.player == Player.BLACK:
            if square.row != 3:
                return None
            square_in_front = -1

        elif square.row != BOARD_SIZE - 4:
            return None

        square_left = Square.at(square.row, square.col - 1)
        square_right = Square.at(square.row, square.col + 1)

        piece_left = None
        piece_right = None

        if board.is_in_bounds(square_left):
            piece_left = board.get_piece(square_left)
        if board.is_in_bounds(square_right):
            piece_right = board.get_piece(square_right)

        if piece_left and piece_left.player != self.player and board.last_piece_moved == piece_left \
                and type(piece_left) is Pawn and piece_left.has_moved_two:
            return Square.at(square_left.row + square_in_front, square_left.col)

        if piece_right and piece_right.player != self.player and board.last_piece_moved == piece_right \
                and type(piece_right) is Pawn and piece_right.has_moved_two:
            return Square.at(square_right.row + square_in_front, square_right.col)

    def can_move_forward(self, board: Board, square: Square) -> bool:
        return not (self.at_edge(square) or self.has_piece_in_front(board, square))

    def get_available_moves(self, board) -> List[Square]:
        current_square = board.find_piece(self)
        square_in_front = 1

        square_list = self.get_moves_diagonal(board, current_square)

        en_passant = self.get_en_passant(board, current_square)
        if en_passant:
            square_list.append(en_passant)

        if not self.can_move_forward(board, current_square):
            return square_list

        if self.player == Player.BLACK:
            square_in_front *= -1

        square_list.append(Square.at(current_square.row + square_in_front, current_square.col))
        if self.has_not_moved(current_square) and not self.has_piece_in_front(board, current_square, distance=2):
            square_list.append(Square.at(current_square.row + (2 * square_in_front), current_square.col))

        return square_list


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
                # check if not same color piece on square_to_move
                piece_on_square = board.get_piece(square_to_move)
                if piece_on_square and piece_on_square.player == self.player:
                    continue

                square_list.append(square_to_move)

        return square_list


def get_moves_on_directions(board: Board, square: Square, player, directions: List[Tuple[int, int]]) -> List[Square]:
    next_squares = [square for _ in directions]
    invalid_directions = []

    square_list = []

    while len(invalid_directions) < len(directions):
        next_squares = [Square.at(square.row + directions[i][0], square.col + directions[i][1])
                        for i, square in enumerate(next_squares)]

        for square_index, next_square in enumerate(next_squares):
            # check valid direction
            if square_index in invalid_directions:
                continue

            # check if is in bounds
            if not board.is_in_bounds(next_square):
                invalid_directions.append(square_index)
                continue

            # check if piece in front
            piece = board.get_piece(next_square)
            if piece:
                invalid_directions.append(square_index)
                if piece.player == player:
                    continue

            square_list.append(next_square)

    return square_list


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        return get_moves_on_directions(board, current_square, self.player, directions)


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        return get_moves_on_directions(board, current_square, self.player, directions)


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]

        return get_moves_on_directions(board, current_square, self.player, directions)


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        square_list = []

        for direction in directions:
            next_square = Square.at(current_square.row + direction[0], current_square.col + direction[1])

            if not board.is_in_bounds(next_square):
                continue

            piece = board.get_piece(next_square)

            if piece:
                if piece.player == self.player:
                    continue

            square_list.append(next_square)

        return square_list
