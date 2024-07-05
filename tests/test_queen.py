from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Queen


class TestQueen:

    @staticmethod
    def test_queen_can_move_up():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(0, 0)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        for pos in range(1, 8):
            assert Square.at(pos, 0) in moves

    @staticmethod
    def test_queen_can_move_down():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(7, 0)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        for pos in range(0, 7):
            assert Square.at(pos, 0) in moves

    @staticmethod
    def test_queen_can_move_right():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(0, 0)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        for pos in range(1, 8):
            assert Square.at(0, pos) in moves

    @staticmethod
    def test_queen_can_move_left():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(0, 7)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        for pos in range(0, 7):
            assert Square.at(0, pos) in moves

    @staticmethod
    def test_queen_can_move_all_directions():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(4, 4)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(5, 4) in moves
        assert Square.at(3, 4) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(4, 3) in moves

    @staticmethod
    def test_queen_can_move_up_right_diagonal():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(0, 0)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        for pos in range(1, 7):
            assert Square.at(pos, pos) in moves

    @staticmethod
    def test_queen_can_move_up_left_diagonal():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(0, 7)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        for pos in range(1, 7):
            assert Square.at(pos, 7 - pos) in moves

    @staticmethod
    def test_queen_can_move_down_right_diagonal():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(7, 7)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        for pos in range(1, 7):
            assert Square.at(7 - pos, 7 - pos) in moves

    @staticmethod
    def test_queen_can_move_down_left_diagonal():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(7, 0)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        for pos in range(1, 7):
            assert Square.at(7 - pos, pos) in moves

    @staticmethod
    def test_queen_can_move_all_diagonals():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(4, 4)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)
        print(moves)

        # Assert
        assert Square.at(3, 5) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(5, 3) in moves
        assert Square.at(5, 5) in moves

    @staticmethod
    def test_queen_cannot_move_past_piece_same_color():
        # Arrange
        board = Board.empty()

        queen = Queen(Player.BLACK)
        piece_to_take = Queen(Player.BLACK)

        square = Square.at(4, 4)
        square_to_take = Square.at(5, 4)

        board.set_piece(square, queen)
        board.set_piece(square_to_take, piece_to_take)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(5, 4) not in moves
        assert Square.at(6, 4) not in moves
        assert Square.at(7, 4) not in moves

        assert Square.at(3, 4) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(4, 3) in moves

    @staticmethod
    def test_queen_cannot_move_past_piece_different_color():
        # Arrange
        board = Board.empty()

        queen = Queen(Player.BLACK)
        piece_to_take = Queen(Player.WHITE)

        square = Square.at(4, 4)
        square_to_take = Square.at(5, 4)

        board.set_piece(square, queen)
        board.set_piece(square_to_take, piece_to_take)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(5, 4) in moves
        assert Square.at(6, 4) not in moves
        assert Square.at(7, 4) not in moves

        assert Square.at(4, 3) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(5, 4) in moves

    @staticmethod
    def test_queen_cannot_move_out_corner_top_left():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(7, 0)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(8, 0) not in moves
        assert Square.at(7, -1) not in moves

    @staticmethod
    def test_queen_cannot_move_out_corner_top_right():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(7, 7)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(8, 7) not in moves
        assert Square.at(7, 8) not in moves

    @staticmethod
    def test_queen_cannot_move_out_corner_bottom_left():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(0, 0)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(-1, 0) not in moves
        assert Square.at(0, -1) not in moves

    @staticmethod
    def test_queen_cannot_move_out_corner_bottom_right():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(0, 7)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(-1, 7) not in moves
        assert Square.at(0, 8) not in moves

    @staticmethod
    def test_queen_cannot_move_out_corner_top_left_diag():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(7, 0)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(8, -1) not in moves
        assert Square.at(8, 1) not in moves
        assert Square.at(6, -1) not in moves

    @staticmethod
    def test_queen_cannot_move_out_corner_top_right_diag():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(7, 7)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(8, 8) not in moves
        assert Square.at(8, 6) not in moves
        assert Square.at(6, 8) not in moves

    @staticmethod
    def test_queen_cannot_move_out_corner_bottom_left_diag():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(0, 0)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(-1, -1) not in moves
        assert Square.at(-1, 1) not in moves
        assert Square.at(1, -1) not in moves

    @staticmethod
    def test_queen_cannot_move_out_corner_bottom_right_diag():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(0, 7)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(-1, 8) not in moves
        assert Square.at(-1, 6) not in moves
        assert Square.at(1, 8) not in moves
