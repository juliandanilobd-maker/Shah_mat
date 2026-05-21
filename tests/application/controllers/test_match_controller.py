from unittest.mock import patch

from app.application.controllers.match_controller import MatchController


# Prueba para determinar que se crea la partida
@patch("app.application.controllers.match_controller.Match")
def test_controller_creates_match(mock_match):

    MatchController("PVP")

    mock_match.assert_called_once_with("PVP")


# Prueba para determinar que funciona correctamente el game loop y el juego se mantienen
# iniciado mientras haya condiciones de juego
@patch.object(MatchController, "game_loop")
@patch("builtins.print")
def test_start_initializes_match(mock_print, mock_game_loop):

    controller = MatchController("PVP")

    controller.match.initialize = lambda: None

    controller.start()

    mock_game_loop.assert_called_once()
