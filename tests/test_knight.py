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

    @staticmethod
    def test_knight_cannot_move_top_board_on_edge():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(7, 4)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(9, 3) not in moves
        assert Square.at(9, 5) not in moves
        assert Square.at(8, 2) not in moves
        assert Square.at(8, 6) not in moves

    @staticmethod
    def test_knight_cannot_move_top_board_one_before_edge():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(6, 4)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(8, 3) not in moves
        assert Square.at(8, 5) not in moves

    @staticmethod
    def test_knight_cannot_move_bottom_board_on_edge():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(0, 4)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(-2, 3) not in moves
        assert Square.at(-2, 5) not in moves
        assert Square.at(-1, 2) not in moves
        assert Square.at(-1, 6) not in moves

    @staticmethod
    def test_knight_cannot_move_bottom_board_one_before_edge():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(0, 4)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(-1, 3) not in moves
        assert Square.at(-1, 5) not in moves

    @staticmethod
    def test_knight_cannot_move_right_board_on_edge():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(4, 7)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(3, 9) not in moves
        assert Square.at(5, 9) not in moves
        assert Square.at(2, 8) not in moves
        assert Square.at(6, 8) not in moves

    @staticmethod
    def test_knight_cannot_move_right_board_one_before_edge():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(4, 6)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(3, 8) not in moves
        assert Square.at(5, 8) not in moves

    @staticmethod
    def test_knight_cannot_move_left_board_on_edge():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(4, 0)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(3, -2) not in moves
        assert Square.at(5, -2) not in moves
        assert Square.at(2, -1) not in moves
        assert Square.at(6, -1) not in moves

    @staticmethod
    def test_knight_cannot_move_left_board_one_before_edge():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(4, 0)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(3, -1) not in moves
        assert Square.at(5, -1) not in moves

    @staticmethod
    def test_knight_cannot_take_same_color():
        # Arrange
        board = Board.empty()

        knight = Knight(Player.BLACK)
        knight_to_take = Knight(Player.BLACK)

        square = Square.at(4, 4)
        square_to_take = Square.at(5, 6)

        board.set_piece(square, knight)
        board.set_piece(square_to_take, knight_to_take)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(5, 6) not in moves

    @staticmethod
    def test_knight_can_take_other_color():
        # Arrange
        board = Board.empty()

        knight = Knight(Player.BLACK)
        knight_to_take = Knight(Player.WHITE)

        square = Square.at(4, 4)
        square_to_take = Square.at(5, 6)

        board.set_piece(square, knight)
        board.set_piece(square_to_take, knight_to_take)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(5, 6) in moves







