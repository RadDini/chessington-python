from __future__ import annotations
from abc import ABC, abstractmethod
from chessington.engine.data import Player, Square
from typing import TYPE_CHECKING, List, Tuple

if TYPE_CHECKING:
    from chessington.engine.board import Board

BOARD_SIZE = 8


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

    def has_piece_diagonal(self, board: Board, square: Square) -> bool:
        increment = 1
        if self.player == Player.BLACK:
            increment = -1

            diag_left = board.get_piece(Square.at(square.row + increment, square.col - 1))
            diag_right = board.get_piece(Square.at(square.row + increment, square.col + 1))

            if (diag_left and diag_left.player != self.player) \
                    or (diag_right and diag_right.player != self.player):
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

    def get_available_moves(self, board) -> List[Square]:
        current_square = board.find_piece(self)
        square_list = []
        increment = 1
        if not self.can_move(board, current_square):
            return square_list

        if self.player == Player.BLACK:
            increment *= -1

        square_list.append(Square.at(current_square.row + increment, current_square.col))
        if self.has_not_moved(current_square) and not self.has_piece_in_front(board, current_square, distance=2):
            square_list.append(Square.at(current_square.row + (2 * increment), current_square.col))

        square_list += self.get_moves_diag(board, current_square)

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



def get_moves_on_directions(board: Board, square: Square, player, directions : List[Tuple[int, int]]) -> List[Square]:
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
        return []
