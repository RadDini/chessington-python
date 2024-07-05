import unittest

from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Rook


class TestRook:

    @staticmethod
    def test_rook_can_move_up():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        square = Square.at(0, 0)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        for pos in range(1, 8):
            assert Square.at(pos, 0) in moves

    @staticmethod
    def test_rook_can_move_down():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        square = Square.at(7, 0)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        for pos in range(0, 7):
            assert Square.at(pos, 0) in moves

    @staticmethod
    def test_rook_can_move_right():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        square = Square.at(0, 0)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        for pos in range(1, 8):
            assert Square.at(0, pos) in moves


    @staticmethod
    def test_rook_can_move_left():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        square = Square.at(0, 7)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        for pos in range(0, 7):
            assert Square.at(0, pos) in moves

    @staticmethod
    def test_rook_can_move_all_directions():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        square = Square.at(4, 4)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(5, 4) in moves
        assert Square.at(3, 4) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(4, 3) in moves

    @staticmethod
    def test_rook_cannot_move_past_piece_same_color():
        # Arrange
        board = Board.empty()

        rook = Rook(Player.BLACK)
        piece_to_take = Rook(Player.BLACK)

        square = Square.at(4, 4)
        square_to_take = Square.at(5, 4)

        board.set_piece(square, rook)
        board.set_piece(square_to_take, piece_to_take)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(5, 4) not in moves
        assert Square.at(6, 4) not in moves
        assert Square.at(7, 4) not in moves

        assert Square.at(3, 4) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(4, 3) in moves

    @staticmethod
    def test_rook_cannot_move_past_piece_different_color():
        # Arrange
        board = Board.empty()

        rook = Rook(Player.BLACK)
        piece_to_take = Rook(Player.WHITE)

        square = Square.at(4, 4)
        square_to_take = Square.at(5, 4)

        board.set_piece(square, rook)
        board.set_piece(square_to_take, piece_to_take)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(5, 4) in moves
        assert Square.at(6, 4) not in moves
        assert Square.at(7, 4) not in moves

        assert Square.at(4, 3) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(5, 4) in moves

    @staticmethod
    def test_rook_cannot_move_out_corner_top_left():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        square = Square.at(7, 0)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(8, 0) not in moves
        assert Square.at(7, -1) not in moves

    @staticmethod
    def test_rook_cannot_move_out_corner_top_right():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        square = Square.at(7, 7)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(8, 7) not in moves
        assert Square.at(7, 8) not in moves

    @staticmethod
    def test_rook_cannot_move_out_corner_bottom_left():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        square = Square.at(0, 0)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(-1, 0) not in moves
        assert Square.at(0, -1) not in moves

    @staticmethod
    def test_rook_cannot_move_out_corner_bottom_right():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        square = Square.at(0, 7)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(-1, 7) not in moves
        assert Square.at(0, 8) not in moves