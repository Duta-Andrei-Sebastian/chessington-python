from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Pawn, Knight, Bishop, Rook, Queen, King


class TestPawns:

    @staticmethod
    def test_white_pawns_can_move_up_one_square():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(2, 4) in moves

    @staticmethod
    def test_black_pawns_can_move_down_one_square():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(6, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(5, 4) in moves

    @staticmethod
    def test_white_pawn_can_move_up_two_squares_if_not_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) in moves

    @staticmethod
    def test_black_pawn_can_move_down_two_squares_if_not_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(6, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) in moves

    @staticmethod
    def test_white_pawn_cannot_move_up_two_squares_if_already_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        starting_square = Square.at(1, 4)
        board.set_piece(starting_square, pawn)

        intermediate_square = Square.at(2, 4)
        pawn.move_to(board, intermediate_square)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) not in moves

    @staticmethod
    def test_black_pawn_cannot_move_down_two_squares_if_already_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        starting_square = Square.at(6, 4)
        board.set_piece(starting_square, pawn)

        intermediate_square = Square.at(5, 4)
        pawn.move_to(board, intermediate_square)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) not in moves

    @staticmethod
    def test_white_pawn_cannot_move_if_piece_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(5, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_pawn_cannot_move_if_piece_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(3, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_pawn_cannot_move_two_squares_if_piece_two_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(1, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(3, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert obstructing_square not in moves

    @staticmethod
    def test_black_pawn_cannot_move_two_squares_if_piece_two_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(6, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(4, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert obstructing_square not in moves

    @staticmethod
    def test_white_pawn_cannot_move_two_squares_if_piece_one_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(1, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(2, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) not in moves

    @staticmethod
    def test_black_pawn_cannot_move_two_squares_if_piece_one_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(6, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(5, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) not in moves

    @staticmethod
    def test_white_pawn_cannot_move_at_top_of_board():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(7, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_pawn_cannot_move_at_bottom_of_board():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(0, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_pawns_can_capture_diagonally():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        enemy1 = Pawn(Player.BLACK)
        enemy1_square = Square.at(4, 5)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.BLACK)
        enemy2_square = Square.at(4, 3)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves

    @staticmethod
    def test_black_pawns_can_capture_diagonally():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        enemy1 = Pawn(Player.WHITE)
        enemy1_square = Square.at(2, 5)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.WHITE)
        enemy2_square = Square.at(2, 3)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves

    @staticmethod
    def test_white_pawns_cannot_move_diagonally_except_to_capture():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        friendly = Pawn(Player.WHITE)
        friendly_square = Square.at(4, 5)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 3) not in moves
        assert Square.at(4, 5) not in moves

    @staticmethod
    def test_black_pawns_cannot_move_diagonally_except_to_capture():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        friendly = Pawn(Player.BLACK)
        friendly_square = Square.at(2, 5)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) not in moves
        assert Square.at(2, 5) not in moves

    @staticmethod
    def test_white_knight_all_moves():

        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        knight_square = Square.at(3, 4)
        board.set_piece(knight_square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(1, 3) in moves
        assert Square.at(1, 5) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(2, 6) in moves
        assert Square.at(4, 2) in moves
        assert Square.at(4, 6) in moves
        assert Square.at(5, 3) in moves
        assert Square.at(5, 5) in moves

    @staticmethod
    def test_black_knight_all_moves():

        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        knight_square = Square.at(3, 4)
        board.set_piece(knight_square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(1, 3) in moves
        assert Square.at(1, 5) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(2, 6) in moves
        assert Square.at(4, 2) in moves
        assert Square.at(4, 6) in moves
        assert Square.at(5, 3) in moves
        assert Square.at(5, 5) in moves

    @staticmethod
    def test_white_knight_capture_enemy():

        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        knight_square = Square.at(3, 4)
        board.set_piece(knight_square, knight)

        enemy = Pawn(Player.BLACK)

        enemy_square1 = Square.at(1, 3)
        board.set_piece(enemy_square1, enemy)

        enemy_square2 = Square.at(1, 5)
        board.set_piece(enemy_square2, enemy)

        enemy_square3 = Square.at(2, 2)
        board.set_piece(enemy_square3, enemy)

        enemy_square4 = Square.at(2, 6)
        board.set_piece(enemy_square4, enemy)

        enemy_square5 = Square.at(4, 2)
        board.set_piece(enemy_square5, enemy)

        enemy_square6 = Square.at(4, 6)
        board.set_piece(enemy_square6, enemy)

        enemy_square7 = Square.at(5, 3)
        board.set_piece(enemy_square7, enemy)

        enemy_square8 = Square.at(5, 5)
        board.set_piece(enemy_square8, enemy)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(1, 3) in moves
        assert Square.at(1, 5) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(2, 6) in moves
        assert Square.at(4, 2) in moves
        assert Square.at(4, 6) in moves
        assert Square.at(5, 3) in moves
        assert Square.at(5, 5) in moves

    @staticmethod
    def test_black_knight_capture_enemy():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        knight_square = Square.at(3, 4)
        board.set_piece(knight_square, knight)

        enemy = Pawn(Player.WHITE)

        enemy_square1 = Square.at(1, 3)
        board.set_piece(enemy_square1, enemy)

        enemy_square2 = Square.at(1, 5)
        board.set_piece(enemy_square2, enemy)

        enemy_square3 = Square.at(2, 2)
        board.set_piece(enemy_square3, enemy)

        enemy_square4 = Square.at(2, 6)
        board.set_piece(enemy_square4, enemy)

        enemy_square5 = Square.at(4, 2)
        board.set_piece(enemy_square5, enemy)

        enemy_square6 = Square.at(4, 6)
        board.set_piece(enemy_square6, enemy)

        enemy_square7 = Square.at(5, 3)
        board.set_piece(enemy_square7, enemy)

        enemy_square8 = Square.at(5, 5)
        board.set_piece(enemy_square8, enemy)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(1, 3) in moves
        assert Square.at(1, 5) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(2, 6) in moves
        assert Square.at(4, 2) in moves
        assert Square.at(4, 6) in moves
        assert Square.at(5, 3) in moves
        assert Square.at(5, 5) in moves

    @staticmethod
    def test_white_knight_doesnt_capture_friendly():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        knight_square = Square.at(3, 4)
        board.set_piece(knight_square, knight)

        friendly = Pawn(Player.WHITE)

        friendly_square1 = Square.at(1, 3)
        board.set_piece(friendly_square1, friendly)

        friendly_square2 = Square.at(1, 5)
        board.set_piece(friendly_square2, friendly)

        friendly_square3 = Square.at(2, 2)
        board.set_piece(friendly_square3, friendly)

        friendly_square4 = Square.at(2, 6)
        board.set_piece(friendly_square4, friendly)

        friendly_square5 = Square.at(4, 2)
        board.set_piece(friendly_square5, friendly)

        friendly_square6 = Square.at(4, 6)
        board.set_piece(friendly_square6, friendly)

        friendly_square7 = Square.at(5, 3)
        board.set_piece(friendly_square7, friendly)

        friendly_square8 = Square.at(5, 5)
        board.set_piece(friendly_square8, friendly)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(1, 3) not in moves
        assert Square.at(1, 5) not in moves
        assert Square.at(2, 2) not in moves
        assert Square.at(2, 6) not in moves
        assert Square.at(4, 2) not in moves
        assert Square.at(4, 6) not in moves
        assert Square.at(5, 3) not in moves
        assert Square.at(5, 5) not in moves

    @staticmethod
    def test_black_knight_doesnt_capture_friendly():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        knight_square = Square.at(3, 4)
        board.set_piece(knight_square, knight)

        friendly = Pawn(Player.BLACK)

        friendly_square1 = Square.at(1, 3)
        board.set_piece(friendly_square1, friendly)

        friendly_square2 = Square.at(1, 5)
        board.set_piece(friendly_square2, friendly)

        friendly_square3 = Square.at(2, 2)
        board.set_piece(friendly_square3, friendly)

        friendly_square4 = Square.at(2, 6)
        board.set_piece(friendly_square4, friendly)

        friendly_square5 = Square.at(4, 2)
        board.set_piece(friendly_square5, friendly)

        friendly_square6 = Square.at(4, 6)
        board.set_piece(friendly_square6, friendly)

        friendly_square7 = Square.at(5, 3)
        board.set_piece(friendly_square7, friendly)

        friendly_square8 = Square.at(5, 5)
        board.set_piece(friendly_square8, friendly)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(1, 3) not in moves
        assert Square.at(1, 5) not in moves
        assert Square.at(2, 2) not in moves
        assert Square.at(2, 6) not in moves
        assert Square.at(4, 2) not in moves
        assert Square.at(4, 6) not in moves
        assert Square.at(5, 3) not in moves
        assert Square.at(5, 5) not in moves

    @staticmethod
    def test_white_knight_moves_mixed():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        knight_square = Square.at(3, 4)
        board.set_piece(knight_square, knight)

        friendly = Pawn(Player.WHITE)
        enemy = Pawn(Player.BLACK)

        friendly_square1 = Square.at(1, 5)
        board.set_piece(friendly_square1, friendly)

        friendly_square2 = Square.at(4, 2)
        board.set_piece(friendly_square2, friendly)

        enemy_square = Square.at(5, 3)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(1, 3) in moves
        assert Square.at(1, 5) not in moves
        assert Square.at(2, 2) in moves
        assert Square.at(2, 6) in moves
        assert Square.at(4, 2) not in moves
        assert Square.at(4, 6) in moves
        assert Square.at(5, 3) in moves
        assert Square.at(5, 5) in moves

    @staticmethod
    def test_black_knight_moves_mixed():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        knight_square = Square.at(3, 4)
        board.set_piece(knight_square, knight)

        friendly = Pawn(Player.BLACK)
        enemy = Pawn(Player.WHITE)

        friendly_square1 = Square.at(1, 5)
        board.set_piece(friendly_square1, friendly)

        friendly_square2 = Square.at(4, 2)
        board.set_piece(friendly_square2, friendly)

        enemy_square = Square.at(5, 3)
        board.set_piece(enemy_square, enemy)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(1, 3) in moves
        assert Square.at(1, 5) not in moves
        assert Square.at(2, 2) in moves
        assert Square.at(2, 6) in moves
        assert Square.at(4, 2) not in moves
        assert Square.at(4, 6) in moves
        assert Square.at(5, 3) in moves
        assert Square.at(5, 5) in moves

    @staticmethod
    def test_white_knight_jumps_over_pieces():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        knight_square = Square.at(3, 4)
        board.set_piece(knight_square, knight)

        friendly = Pawn(Player.WHITE)
        enemy = Pawn(Player.BLACK)

        friendly_square1 = Square.at(2, 3)
        board.set_piece(friendly_square1, friendly)

        enemy_square1 = Square.at(2,4)
        board.set_piece(enemy_square1, enemy)

        friendly_square2 = Square.at(2, 5)
        board.set_piece(friendly_square2, friendly)

        enemy_square2 = Square.at(3,3)
        board.set_piece(enemy_square2, enemy)

        friendly_square3 = Square.at(3, 5)
        board.set_piece(friendly_square3, friendly)

        enemy_square3 = Square.at(4,3)
        board.set_piece(enemy_square3, enemy)

        friendly_square4 = Square.at(4, 4)
        board.set_piece(friendly_square4, friendly)

        enemy_square4 = Square.at(4, 5)
        board.set_piece(enemy_square4, enemy)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(1, 3) in moves
        assert Square.at(1, 5) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(2, 6) in moves
        assert Square.at(4, 2) in moves
        assert Square.at(4, 6) in moves
        assert Square.at(5, 3) in moves
        assert Square.at(5, 5) in moves
        assert Square.at(2, 4) not in moves
        assert Square.at(3, 3) not in moves
        assert Square.at(4, 3) not in moves
        assert Square.at(4, 5) not in moves

    @staticmethod
    def test_black_knight_jumps_over_pieces():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        knight_square = Square.at(3, 4)
        board.set_piece(knight_square, knight)

        friendly = Pawn(Player.BLACK)
        enemy = Pawn(Player.WHITE)

        friendly_square1 = Square.at(2, 3)
        board.set_piece(friendly_square1, friendly)

        enemy_square1 = Square.at(2, 4)
        board.set_piece(enemy_square1, enemy)

        friendly_square2 = Square.at(2, 5)
        board.set_piece(friendly_square2, friendly)

        enemy_square2 = Square.at(3, 3)
        board.set_piece(enemy_square2, enemy)

        friendly_square3 = Square.at(3, 5)
        board.set_piece(friendly_square3, friendly)

        enemy_square3 = Square.at(4, 3)
        board.set_piece(enemy_square3, enemy)

        friendly_square4 = Square.at(4, 4)
        board.set_piece(friendly_square4, friendly)

        enemy_square4 = Square.at(4, 5)
        board.set_piece(enemy_square4, enemy)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(1, 3) in moves
        assert Square.at(1, 5) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(2, 6) in moves
        assert Square.at(4, 2) in moves
        assert Square.at(4, 6) in moves
        assert Square.at(5, 3) in moves
        assert Square.at(5, 5) in moves
        assert Square.at(2, 4) not in moves
        assert Square.at(3, 3) not in moves
        assert Square.at(4, 3) not in moves
        assert Square.at(4, 5) not in moves

    @staticmethod
    def test_white_bishop_all_moves():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(3, 4)
        board.set_piece(bishop_square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) in moves
        assert Square.at(1, 2) in moves
        assert Square.at(0, 1) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 6) in moves
        assert Square.at(0, 7) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(5, 2) in moves
        assert Square.at(6, 1) in moves
        assert Square.at(7, 0) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(5, 6) in moves
        assert Square.at(6, 7) in moves

    @staticmethod
    def test_black_bishop_all_moves():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.BLACK)
        bishop_square = Square.at(3, 4)
        board.set_piece(bishop_square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) in moves
        assert Square.at(1, 2) in moves
        assert Square.at(0, 1) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 6) in moves
        assert Square.at(0, 7) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(5, 2) in moves
        assert Square.at(6, 1) in moves
        assert Square.at(7, 0) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(5, 6) in moves
        assert Square.at(6, 7) in moves

    @staticmethod
    def test_white_bishop_capture_enemy():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(3, 4)
        board.set_piece(bishop_square, bishop)

        enemy = Pawn(Player.BLACK)

        enemy_square1 = Square.at(2, 3)
        board.set_piece(enemy_square1, enemy)

        enemy_square2 = Square.at(1, 6)
        board.set_piece(enemy_square2, enemy)

        enemy_square3 = Square.at(7, 0)
        board.set_piece(enemy_square3, enemy)

        enemy_square4 = Square.at(5, 6)
        board.set_piece(enemy_square4, enemy)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) in moves
        assert Square.at(1, 2) not in moves
        assert Square.at(0, 1) not in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 6) in moves
        assert Square.at(0, 7) not in moves
        assert Square.at(4, 3) in moves
        assert Square.at(5, 2) in moves
        assert Square.at(6, 1) in moves
        assert Square.at(7, 0) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(5, 6) in moves
        assert Square.at(6, 7) not in moves

    @staticmethod
    def test_black_bishop_capture_enemy():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.BLACK)
        bishop_square = Square.at(3, 4)
        board.set_piece(bishop_square, bishop)

        enemy = Pawn(Player.WHITE)

        enemy_square1 = Square.at(2, 3)
        board.set_piece(enemy_square1, enemy)

        enemy_square2 = Square.at(1, 6)
        board.set_piece(enemy_square2, enemy)

        enemy_square3 = Square.at(7, 0)
        board.set_piece(enemy_square3, enemy)

        enemy_square4 = Square.at(5, 6)
        board.set_piece(enemy_square4, enemy)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) in moves
        assert Square.at(1, 2) not in moves
        assert Square.at(0, 1) not in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 6) in moves
        assert Square.at(0, 7) not in moves
        assert Square.at(4, 3) in moves
        assert Square.at(5, 2) in moves
        assert Square.at(6, 1) in moves
        assert Square.at(7, 0) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(5, 6) in moves
        assert Square.at(6, 7) not in moves

    @staticmethod
    def test_white_bishop_doesnt_capture_friendly():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(3, 4)
        board.set_piece(bishop_square, bishop)

        friendly = Pawn(Player.WHITE)

        friendly_square1 = Square.at(2, 3)
        board.set_piece(friendly_square1, friendly)

        friendly_square2 = Square.at(1, 6)
        board.set_piece(friendly_square2, friendly)

        friendly_square3 = Square.at(7, 0)
        board.set_piece(friendly_square3, friendly)

        friendly_square4 = Square.at(5, 6)
        board.set_piece(friendly_square4, friendly)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) not in moves
        assert Square.at(1, 2) not in moves
        assert Square.at(0, 1) not in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 6) not in moves
        assert Square.at(0, 7) not in moves
        assert Square.at(4, 3) in moves
        assert Square.at(5, 2) in moves
        assert Square.at(6, 1) in moves
        assert Square.at(7, 0) not in moves
        assert Square.at(4, 5) in moves
        assert Square.at(5, 6) not in moves
        assert Square.at(6, 7) not in moves

    @staticmethod
    def test_black_bishop_doesnt_capture_friendly():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.BLACK)
        bishop_square = Square.at(3, 4)
        board.set_piece(bishop_square, bishop)

        friendly = Pawn(Player.BLACK)

        friendly_square1 = Square.at(2, 3)
        board.set_piece(friendly_square1, friendly)

        friendly_square2 = Square.at(1, 6)
        board.set_piece(friendly_square2, friendly)

        friendly_square3 = Square.at(7, 0)
        board.set_piece(friendly_square3, friendly)

        friendly_square4 = Square.at(5, 6)
        board.set_piece(friendly_square4, friendly)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) not in moves
        assert Square.at(1, 2) not in moves
        assert Square.at(0, 1) not in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 6) not in moves
        assert Square.at(0, 7) not in moves
        assert Square.at(4, 3) in moves
        assert Square.at(5, 2) in moves
        assert Square.at(6, 1) in moves
        assert Square.at(7, 0) not in moves
        assert Square.at(4, 5) in moves
        assert Square.at(5, 6) not in moves
        assert Square.at(6, 7) not in moves

    @staticmethod
    def test_white_rook_all_moves():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(3, 4)
        board.set_piece(rook_square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(7, 4) in moves
        assert Square.at(6, 4) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(4, 4) in moves
        assert Square.at(2, 4) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(0, 4) in moves
        assert Square.at(3, 7) in moves
        assert Square.at(3, 6) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(3, 1) in moves
        assert Square.at(3, 0) in moves

    @staticmethod
    def test_black_rook_all_moves():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        rook_square = Square.at(3, 4)
        board.set_piece(rook_square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(7, 4) in moves
        assert Square.at(6, 4) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(4, 4) in moves
        assert Square.at(2, 4) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(0, 4) in moves
        assert Square.at(3, 7) in moves
        assert Square.at(3, 6) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(3, 1) in moves
        assert Square.at(3, 0) in moves

    @staticmethod
    def test_white_rook_capture_enemy():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(3, 4)
        board.set_piece(rook_square, rook)

        enemy = Pawn(Player.BLACK)

        enemy_square1 = Square.at(3, 2)
        board.set_piece(enemy_square1, enemy)

        enemy_square2 = Square.at(3,  7)
        board.set_piece(enemy_square2, enemy)

        enemy_square3 = Square.at(2, 4)
        board.set_piece(enemy_square3, enemy)

        enemy_square4 = Square.at(6, 4)
        board.set_piece(enemy_square4, enemy)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(7, 4) not in moves
        assert Square.at(6, 4) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(4, 4) in moves
        assert Square.at(2, 4) in moves
        assert Square.at(1, 4) not in moves
        assert Square.at(0, 4) not in moves
        assert Square.at(3, 7) in moves
        assert Square.at(3, 6) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(3, 1) not in moves
        assert Square.at(3, 0) not in moves

    @staticmethod
    def test_black_rook_capture_enemy():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        rook_square = Square.at(3, 4)
        board.set_piece(rook_square, rook)

        enemy = Pawn(Player.WHITE)

        enemy_square1 = Square.at(3, 2)
        board.set_piece(enemy_square1, enemy)

        enemy_square2 = Square.at(3, 7)
        board.set_piece(enemy_square2, enemy)

        enemy_square3 = Square.at(2, 4)
        board.set_piece(enemy_square3, enemy)

        enemy_square4 = Square.at(6, 4)
        board.set_piece(enemy_square4, enemy)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(7, 4) not in moves
        assert Square.at(6, 4) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(4, 4) in moves
        assert Square.at(2, 4) in moves
        assert Square.at(1, 4) not in moves
        assert Square.at(0, 4) not in moves
        assert Square.at(3, 7) in moves
        assert Square.at(3, 6) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(3, 1) not in moves
        assert Square.at(3, 0) not in moves

    @staticmethod
    def test_white_rook_doesnt_capture_friendly():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(3, 4)
        board.set_piece(rook_square, rook)

        friendly = Pawn(Player.WHITE)

        friendly_square1 = Square.at(3, 2)
        board.set_piece(friendly_square1, friendly)

        friendly_square2 = Square.at(3, 7)
        board.set_piece(friendly_square2, friendly)

        friendly_square3 = Square.at(2, 4)
        board.set_piece(friendly_square3, friendly)

        friendly_square4 = Square.at(6, 4)
        board.set_piece(friendly_square4, friendly)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(7, 4) not in moves
        assert Square.at(6, 4) not in moves
        assert Square.at(5, 4) in moves
        assert Square.at(4, 4) in moves
        assert Square.at(2, 4) not in moves
        assert Square.at(1, 4) not in moves
        assert Square.at(0, 4) not in moves
        assert Square.at(3, 7) not in moves
        assert Square.at(3, 6) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 2) not in moves
        assert Square.at(3, 1) not in moves
        assert Square.at(3, 0) not in moves

    @staticmethod
    def test_black_rook_doesnt_capture_friendly():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        rook_square = Square.at(3, 4)
        board.set_piece(rook_square, rook)

        friendly = Pawn(Player.BLACK)

        friendly_square1 = Square.at(3, 2)
        board.set_piece(friendly_square1, friendly)

        friendly_square2 = Square.at(3, 7)
        board.set_piece(friendly_square2, friendly)

        friendly_square3 = Square.at(2, 4)
        board.set_piece(friendly_square3, friendly)

        friendly_square4 = Square.at(6, 4)
        board.set_piece(friendly_square4, friendly)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(7, 4) not in moves
        assert Square.at(6, 4) not in moves
        assert Square.at(5, 4) in moves
        assert Square.at(4, 4) in moves
        assert Square.at(2, 4) not in moves
        assert Square.at(1, 4) not in moves
        assert Square.at(0, 4) not in moves
        assert Square.at(3, 7) not in moves
        assert Square.at(3, 6) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 2) not in moves
        assert Square.at(3, 1) not in moves
        assert Square.at(3, 0) not in moves

    @staticmethod
    def test_white_queen_all_moves():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        queen_square = Square.at(3, 4)
        board.set_piece(queen_square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        # Rook-like moves
        assert Square.at(7, 4) in moves
        assert Square.at(6, 4) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(4, 4) in moves
        assert Square.at(2, 4) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(0, 4) in moves
        assert Square.at(3, 7) in moves
        assert Square.at(3, 6) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(3, 1) in moves
        assert Square.at(3, 0) in moves

        # Bishop-like moves
        assert Square.at(2, 3) in moves
        assert Square.at(1, 2) in moves
        assert Square.at(0, 1) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 6) in moves
        assert Square.at(0, 7) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(5, 2) in moves
        assert Square.at(6, 1) in moves
        assert Square.at(7, 0) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(5, 6) in moves
        assert Square.at(6, 7) in moves

    @staticmethod
    def test_black_queen_all_moves():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        queen_square = Square.at(3, 4)
        board.set_piece(queen_square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        # Rook-like moves
        assert Square.at(7, 4) in moves
        assert Square.at(6, 4) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(4, 4) in moves
        assert Square.at(2, 4) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(0, 4) in moves
        assert Square.at(3, 7) in moves
        assert Square.at(3, 6) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(3, 1) in moves
        assert Square.at(3, 0) in moves

        # Bishop-like moves
        assert Square.at(2, 3) in moves
        assert Square.at(1, 2) in moves
        assert Square.at(0, 1) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 6) in moves
        assert Square.at(0, 7) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(5, 2) in moves
        assert Square.at(6, 1) in moves
        assert Square.at(7, 0) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(5, 6) in moves
        assert Square.at(6, 7) in moves

    @staticmethod
    def test_white_queen_capture_enemy():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        queen_square = Square.at(3, 4)
        board.set_piece(queen_square, queen)

        enemy = Pawn(Player.BLACK)

        enemy_square1 = Square.at(5, 4)
        board.set_piece(enemy_square1, enemy)

        enemy_square2 = Square.at(2, 4)
        board.set_piece(enemy_square2, enemy)

        enemy_square3 = Square.at(3, 1)
        board.set_piece(enemy_square3, enemy)

        enemy_square4 = Square.at(3, 6)
        board.set_piece(enemy_square4, enemy)

        enemy_square5 = Square.at(2, 3)
        board.set_piece(enemy_square5, enemy)

        enemy_square6 = Square.at(1, 6)
        board.set_piece(enemy_square6, enemy)

        enemy_square7 = Square.at(5, 2)
        board.set_piece(enemy_square7, enemy)

        enemy_square8 = Square.at(6, 7)
        board.set_piece(enemy_square8, enemy)


        # Act
        moves = queen.get_available_moves(board)

        # Assert
        # Rook-like moves
        assert Square.at(7, 4) not in moves
        assert Square.at(6, 4) not in moves
        assert Square.at(5, 4) in moves
        assert Square.at(4, 4) in moves
        assert Square.at(2, 4) in moves
        assert Square.at(1, 4) not in moves
        assert Square.at(0, 4) not in moves
        assert Square.at(3, 7) not in moves
        assert Square.at(3, 6) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(3, 1) in moves
        assert Square.at(3, 0) not in moves

        # Bishop-like moves
        assert Square.at(2, 3) in moves
        assert Square.at(1, 2) not in moves
        assert Square.at(0, 1) not in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 6) in moves
        assert Square.at(0, 7) not in moves
        assert Square.at(4, 3) in moves
        assert Square.at(5, 2) in moves
        assert Square.at(6, 1) not in moves
        assert Square.at(7, 0) not in moves
        assert Square.at(4, 5) in moves
        assert Square.at(5, 6) in moves
        assert Square.at(6, 7) in moves

    @staticmethod
    def test_black_queen_capture_enemy():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        queen_square = Square.at(3, 4)
        board.set_piece(queen_square, queen)

        enemy = Pawn(Player.WHITE)

        enemy_square1 = Square.at(5, 4)
        board.set_piece(enemy_square1, enemy)

        enemy_square2 = Square.at(2, 4)
        board.set_piece(enemy_square2, enemy)

        enemy_square3 = Square.at(3, 1)
        board.set_piece(enemy_square3, enemy)

        enemy_square4 = Square.at(3, 6)
        board.set_piece(enemy_square4, enemy)

        enemy_square5 = Square.at(2, 3)
        board.set_piece(enemy_square5, enemy)

        enemy_square6 = Square.at(1, 6)
        board.set_piece(enemy_square6, enemy)

        enemy_square7 = Square.at(5, 2)
        board.set_piece(enemy_square7, enemy)

        enemy_square8 = Square.at(6, 7)
        board.set_piece(enemy_square8, enemy)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        # Rook-like moves
        assert Square.at(7, 4) not in moves
        assert Square.at(6, 4) not in moves
        assert Square.at(5, 4) in moves
        assert Square.at(4, 4) in moves
        assert Square.at(2, 4) in moves
        assert Square.at(1, 4) not in moves
        assert Square.at(0, 4) not in moves
        assert Square.at(3, 7) not in moves
        assert Square.at(3, 6) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(3, 1) in moves
        assert Square.at(3, 0) not in moves

        # Bishop-like moves
        assert Square.at(2, 3) in moves
        assert Square.at(1, 2) not in moves
        assert Square.at(0, 1) not in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 6) in moves
        assert Square.at(0, 7) not in moves
        assert Square.at(4, 3) in moves
        assert Square.at(5, 2) in moves
        assert Square.at(6, 1) not in moves
        assert Square.at(7, 0) not in moves
        assert Square.at(4, 5) in moves
        assert Square.at(5, 6) in moves
        assert Square.at(6, 7) in moves

    @staticmethod
    def test_white_queen_doesnt_capture_friendly():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        queen_square = Square.at(3, 4)
        board.set_piece(queen_square, queen)

        friendly = Pawn(Player.WHITE)

        friendly_square1 = Square.at(5, 4)
        board.set_piece(friendly_square1, friendly)

        friendly_square2 = Square.at(2, 4)
        board.set_piece(friendly_square2, friendly)

        friendly_square3 = Square.at(3, 1)
        board.set_piece(friendly_square3, friendly)

        friendly_square4 = Square.at(3, 6)
        board.set_piece(friendly_square4, friendly)

        friendly_square5 = Square.at(2, 3)
        board.set_piece(friendly_square5, friendly)

        friendly_square6 = Square.at(1, 6)
        board.set_piece(friendly_square6, friendly)

        friendly_square7 = Square.at(5, 2)
        board.set_piece(friendly_square7, friendly)

        friendly_square8 = Square.at(6, 7)
        board.set_piece(friendly_square8, friendly)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        # Rook-like moves
        assert Square.at(7, 4) not in moves
        assert Square.at(6, 4) not in moves
        assert Square.at(5, 4) not in moves
        assert Square.at(4, 4) in moves
        assert Square.at(2, 4) not in moves
        assert Square.at(1, 4) not in moves
        assert Square.at(0, 4) not in moves
        assert Square.at(3, 7) not in moves
        assert Square.at(3, 6) not in moves
        assert Square.at(3, 5) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(3, 1) not in moves
        assert Square.at(3, 0) not in moves

        # Bishop-like moves
        assert Square.at(2, 3) not in moves
        assert Square.at(1, 2) not in moves
        assert Square.at(0, 1) not in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 6) not in moves
        assert Square.at(0, 7) not in moves
        assert Square.at(4, 3) in moves
        assert Square.at(5, 2) not in moves
        assert Square.at(6, 1) not in moves
        assert Square.at(7, 0) not in moves
        assert Square.at(4, 5) in moves
        assert Square.at(5, 6) in moves
        assert Square.at(6, 7) not in moves

    @staticmethod
    def test_black_queen_doesnt_capture_friendly():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        queen_square = Square.at(3, 4)
        board.set_piece(queen_square, queen)

        friendly = Pawn(Player.BLACK)

        friendly_square1 = Square.at(5, 4)
        board.set_piece(friendly_square1, friendly)

        friendly_square2 = Square.at(2, 4)
        board.set_piece(friendly_square2, friendly)

        friendly_square3 = Square.at(3, 1)
        board.set_piece(friendly_square3, friendly)

        friendly_square4 = Square.at(3, 6)
        board.set_piece(friendly_square4, friendly)

        friendly_square5 = Square.at(2, 3)
        board.set_piece(friendly_square5, friendly)

        friendly_square6 = Square.at(1, 6)
        board.set_piece(friendly_square6, friendly)

        friendly_square7 = Square.at(5, 2)
        board.set_piece(friendly_square7, friendly)

        friendly_square8 = Square.at(6, 7)
        board.set_piece(friendly_square8, friendly)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        # Rook-like moves
        assert Square.at(7, 4) not in moves
        assert Square.at(6, 4) not in moves
        assert Square.at(5, 4) not in moves
        assert Square.at(4, 4) in moves
        assert Square.at(2, 4) not in moves
        assert Square.at(1, 4) not in moves
        assert Square.at(0, 4) not in moves
        assert Square.at(3, 7) not in moves
        assert Square.at(3, 6) not in moves
        assert Square.at(3, 5) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(3, 1) not in moves
        assert Square.at(3, 0) not in moves

        # Bishop-like moves
        assert Square.at(2, 3) not in moves
        assert Square.at(1, 2) not in moves
        assert Square.at(0, 1) not in moves
        assert Square.at(2, 5) in moves
        assert Square.at(1, 6) not in moves
        assert Square.at(0, 7) not in moves
        assert Square.at(4, 3) in moves
        assert Square.at(5, 2) not in moves
        assert Square.at(6, 1) not in moves
        assert Square.at(7, 0) not in moves
        assert Square.at(4, 5) in moves
        assert Square.at(5, 6) in moves
        assert Square.at(6, 7) not in moves

    @staticmethod
    def test_white_king_all_moves():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(3, 4)
        board.set_piece(king_square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) in moves
        assert Square.at(2, 4) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(4, 4) in moves
        assert Square.at(4, 5) in moves

    @staticmethod
    def test_black_king_all_moves():
        # Arrange
        board = Board.empty()
        king = King(Player.BLACK)
        king_square = Square.at(3, 4)
        board.set_piece(king_square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) in moves
        assert Square.at(2, 4) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(4, 4) in moves
        assert Square.at(4, 5) in moves

    @staticmethod
    def test_white_king_capture_enemy1():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(3, 4)
        board.set_piece(king_square, king)

        enemyPawn = Pawn(Player.BLACK)

        enemy_square1 = Square.at(2, 3)
        board.set_piece(enemy_square1, enemyPawn)

        enemy_square3 = Square.at(2, 5)
        board.set_piece(enemy_square3, enemyPawn)

        enemy_square6 = Square.at(4, 3)
        board.set_piece(enemy_square6, enemyPawn)

        enemy_square8 = Square.at(4, 5)
        board.set_piece(enemy_square8, enemyPawn)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(4, 5) in moves

    @staticmethod
    def test_white_king_capture_enemy2():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(3, 4)
        board.set_piece(king_square, king)

        enemyHorsey = Knight(Player.BLACK)

        enemy_square2 = Square.at(2, 4)
        board.set_piece(enemy_square2, enemyHorsey)

        enemy_square4 = Square.at(3, 3)
        board.set_piece(enemy_square4, enemyHorsey)

        enemy_square5 = Square.at(3, 5)
        board.set_piece(enemy_square5, enemyHorsey)

        enemy_square7 = Square.at(4, 4)
        board.set_piece(enemy_square7, enemyHorsey)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(2, 4) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(4, 4) in moves

    @staticmethod
    def test_black_king_capture_enemy1():
        # Arrange
        board = Board.empty()
        king = King(Player.BLACK)
        king_square = Square.at(3, 4)
        board.set_piece(king_square, king)

        enemyPawn = Pawn(Player.WHITE)

        enemy_square1 = Square.at(2, 3)
        board.set_piece(enemy_square1, enemyPawn)

        enemy_square3 = Square.at(2, 5)
        board.set_piece(enemy_square3, enemyPawn)

        enemy_square6 = Square.at(4, 3)
        board.set_piece(enemy_square6, enemyPawn)

        enemy_square8 = Square.at(4, 5)
        board.set_piece(enemy_square8, enemyPawn)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(4, 5) in moves

    @staticmethod
    def test_black_king_capture_enemy2():
        # Arrange
        board = Board.empty()
        king = King(Player.BLACK)
        king_square = Square.at(3, 4)
        board.set_piece(king_square, king)

        enemyHorsey = Knight(Player.WHITE)

        enemy_square2 = Square.at(2, 4)
        board.set_piece(enemy_square2, enemyHorsey)

        enemy_square4 = Square.at(3, 3)
        board.set_piece(enemy_square4, enemyHorsey)

        enemy_square5 = Square.at(3, 5)
        board.set_piece(enemy_square5, enemyHorsey)

        enemy_square7 = Square.at(4, 4)
        board.set_piece(enemy_square7, enemyHorsey)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(2, 4) in moves
        assert Square.at(3, 3) in moves
        assert Square.at(3, 5) in moves
        assert Square.at(4, 4) in moves

    @staticmethod
    def test_white_king_doesnt_capture_friendly():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(3, 4)
        board.set_piece(king_square, king)

        friendly = Pawn(Player.WHITE)

        friendly_square1 = Square.at(2, 3)
        board.set_piece(friendly_square1, friendly)

        friendly_square2 = Square.at(2, 4)
        board.set_piece(friendly_square2, friendly)

        friendly_square3 = Square.at(2, 5)
        board.set_piece(friendly_square3, friendly)

        friendly_square4 = Square.at(3, 3)
        board.set_piece(friendly_square4, friendly)

        friendly_square5 = Square.at(3, 5)
        board.set_piece(friendly_square5, friendly)

        friendly_square6 = Square.at(4, 3)
        board.set_piece(friendly_square6, friendly)

        friendly_square7 = Square.at(4, 4)
        board.set_piece(friendly_square7, friendly)

        friendly_square8 = Square.at(4, 5)
        board.set_piece(friendly_square8, friendly)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) not in moves
        assert Square.at(2, 4) not in moves
        assert Square.at(2, 5) not in moves
        assert Square.at(3, 3) not in moves
        assert Square.at(3, 5) not in moves
        assert Square.at(4, 3) not in moves
        assert Square.at(4, 4) not in moves
        assert Square.at(4, 5) not in moves

    @staticmethod
    def test_black_king_doesnt_capture_friendly():
        # Arrange
        board = Board.empty()
        king = King(Player.BLACK)
        king_square = Square.at(3, 4)
        board.set_piece(king_square, king)

        friendly = Pawn(Player.BLACK)

        friendly_square1 = Square.at(2, 3)
        board.set_piece(friendly_square1, friendly)

        friendly_square2 = Square.at(2, 4)
        board.set_piece(friendly_square2, friendly)

        friendly_square3 = Square.at(2, 5)
        board.set_piece(friendly_square3, friendly)

        friendly_square4 = Square.at(3, 3)
        board.set_piece(friendly_square4, friendly)

        friendly_square5 = Square.at(3, 5)
        board.set_piece(friendly_square5, friendly)

        friendly_square6 = Square.at(4, 3)
        board.set_piece(friendly_square6, friendly)

        friendly_square7 = Square.at(4, 4)
        board.set_piece(friendly_square7, friendly)

        friendly_square8 = Square.at(4, 5)
        board.set_piece(friendly_square8, friendly)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) not in moves
        assert Square.at(2, 4) not in moves
        assert Square.at(2, 5) not in moves
        assert Square.at(3, 3) not in moves
        assert Square.at(3, 5) not in moves
        assert Square.at(4, 3) not in moves
        assert Square.at(4, 4) not in moves
        assert Square.at(4, 5) not in moves