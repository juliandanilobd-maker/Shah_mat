from unittest.mock import patch

from app.application.services.game_service import GameService


# Prueba para determinar que se inicia el menú
@patch("app.application.services.game_service.MenuManager")
def test_game_service_initializes_menu(mock_menu):

    service = GameService()

    mock_menu.assert_called_once()
    assert service.menu == mock_menu.return_value


# Prueba para determinar si se inicia correctamente el controlador del juego, llamado PVP
@patch("app.application.services.game_service.MatchController")
def test_start_match_creates_controller(mock_controller):

    service = GameService()

    service.start_match("PVP")

    mock_controller.assert_called_once_with("PVP")


# Prueba para determinar si se abre la opcion config
@patch("builtins.print")
def test_show_config_prints_message(mock_print):

    service = GameService()

    service.show_config()

    mock_print.assert_called_once()
