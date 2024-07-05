import unittest

from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import King


class TestKing:

    @staticmethod
    def test_king_can_move_up():
        # Arrange
        board = Board.empty()
        king = King(Player.BLACK)
        square = Square.at(4, 4)
        board.set_piece(square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(5, 4) in moves

    @staticmethod
    def test_king_can_move_down():
        # Arrange
        board = Board.empty()
        king = King(Player.BLACK)
        square = Square.at(4, 4)
        board.set_piece(square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) in moves

    @staticmethod
    def test_king_can_move_right():
        # Arrange
        board = Board.empty()
        king = King(Player.BLACK)
        square = Square.at(4, 4)
        board.set_piece(square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(4, 5) in moves

    @staticmethod
    def test_king_can_move_left():
        # Arrange
        board = Board.empty()
        king = King(Player.BLACK)
        square = Square.at(4, 4)
        board.set_piece(square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(4, 3) in moves

    @staticmethod
    def test_king_can_take_other_color_piece():
        # Arrange
        board = Board.empty()

        king = King(Player.BLACK)
        piece_to_take = King(Player.WHITE)

        square = Square.at(4, 4)
        square_to_take = Square.at(4, 5)

        board.set_piece(square, king)
        board.set_piece(square_to_take, piece_to_take)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(4, 5) in moves

    @staticmethod
    def test_king_cannot_take_same_color_piece():
        # Arrange
        board = Board.empty()

        king = King(Player.BLACK)
        piece_to_take = King(Player.BLACK)

        square = Square.at(4, 4)
        square_to_take = Square.at(4, 5)

        board.set_piece(square, king)
        board.set_piece(square_to_take, piece_to_take)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(4, 5) not in moves



