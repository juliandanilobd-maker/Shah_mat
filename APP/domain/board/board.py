class Board:

    def __init__(self):

        self.grid = self.create_board()

    def create_board(self):
        return [[None for _ in range(10)] for _ in range(10)]
    
    def setup_initial_state(self):
        print("Tablero inicializado")

    def render(self):
        print("\nTABLERO:")
        for row in self.grid:
            print(row)

    def validate_move(self, action):

        print("Validando movimiento...")

        return {
            "type": "MOVE_OK",
            "data": action
        }
    
    def apply_damages(self, result):
        print("Aplicando daño...")