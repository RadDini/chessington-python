import unittest

from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Bishop


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
    def test_bishop_can_move_up_right_diagonal():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.BLACK)
        square = Square.at(0, 0)
        board.set_piece(square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        for pos in range(1, 7):
            assert Square.at(pos, pos) in moves

    @staticmethod
    def test_bishop_can_move_up_left_diagonal():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.BLACK)
        square = Square.at(0, 7)
        board.set_piece(square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        for pos in range(1, 7):
            assert Square.at(pos, 8 - pos) in moves

    @staticmethod
    def test_bishop_can_move_down_right_diagonal():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.BLACK)
        square = Square.at(7, 7)
        board.set_piece(square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        for pos in range(1, 7):
            assert Square.at(8 - pos, 8 - pos) in moves

    @staticmethod
    def test_bishop_can_move_down_left_diagonal():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.BLACK)
        square = Square.at(7, 0)
        board.set_piece(square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        for pos in range(1, 7):
            assert Square.at(8 - pos, pos) in moves

    @staticmethod
    def test_bishop_can_move_all_diagonals():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.BLACK)
        square = Square.at(4, 4)
        board.set_piece(square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(3, 5) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(5, 3) in moves
        assert Square.at(5, 5) in moves
