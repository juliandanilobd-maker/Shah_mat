from app.domain.board.board import Board

# Prueba para determinar si se crea el tablero con las medidas adecuadas
def test_create_board_size():

    board = Board()

    assert len(board.grid) == 10
    assert len(board.grid[0]) == 10

# Prueba para determinar si el tablero se crea sin valores en sus casillas
def test_board_initial_values_none():

    board = Board()

    for row in board.grid:
        for cell in row:
            assert cell is None

# Prueba para determinar si el tablero valida el movimiento
def test_validate_move():

    board = Board()

    action = {
        "type":"MOVE",
        "from":(0, 0),
        "to":(1, 1)
    }

    result = board.validate_move(action)

    assert result["type"] == "MOVE_OK"
    assert result["data"] == action