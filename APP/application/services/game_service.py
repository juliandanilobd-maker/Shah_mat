from app.domain.match.match import Match
from app.application.controllers.match_controller import MatchController
from app.UI.menu.menu_manager import MenuManager


class GameService:

    def __init__(self):
        self.menu = MenuManager()

    def start(self):
        print("=== THRONE & TREASON INICIADO ===")

        running = True

        while running:

            option = self.menu.show_main_menu()

            if option == "1":
                self.start_match(mode="AI")

            elif option == "2":
                self.start_match(mode="PVP")

            elif option == "3":
                self.show_config()

            elif option == "0":
                running = False

    def start_match(self, mode):
        controller = MatchController(mode)
        controller.start()

    def show_config(self):
        print("Configuración del juego (en desarrollo)")
