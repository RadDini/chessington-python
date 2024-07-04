import unittest

from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Knight


class TestPawns:

    @staticmethod
    def test_kngiht_can_move_two_up_one_left():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(4, 4)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(6, 3) in moves

    @staticmethod
    def test_knight_can_move_two_up_one_right():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(4, 4)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(6, 5) in moves

    @staticmethod
    def test_knight_can_move_two_right_one_up():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(4, 4)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(5, 6) in moves

    @staticmethod
    def test_knight_can_move_two_right_one_down():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(4, 4)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(3, 6) in moves

    @staticmethod
    def test_knight_can_move_two_down_one_right():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(4, 4)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(2, 5) in moves

    @staticmethod
    def test_knight_can_move_two_down_one_left():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(4, 4)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) in moves

    @staticmethod
    def test_knight_can_move_two_left_one_down():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(4, 4)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(3, 2) in moves

    @staticmethod
    def test_knight_can_move_two_left_one_up():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(4, 4)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(5, 2) in moves



