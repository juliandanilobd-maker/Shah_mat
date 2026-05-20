# Arquitectura del proyecto - Sitrang

## Diagrama de arquitectura

Flujo de datos en arquitectura

1. [JUGADOR] ---Entrada de datos---> [UI]
2. [UI] ---captura el evento---> [Domain] 
                                      └──[GameController] ---> procesa los datos
3. [Board] ---actualiza estado---> [CombatSystem]
4. [CombatSystem] ---calcula el daño---> [Storage]
5. [Storage] ---guarda datos---> [UI] ---> genera los cambios en el tablero y piezas

Estructura Principal
Sitrang/
│
├── .github/
├── app/
│   ├── .venv/
│   ├── ui/
│   ├── application/
│   ├── domain/
│   ├── storage/
│   ├── audiovisual/
│   └── assets/
│
├── docs/
├── tests/
├── README.md
├── requirements.txt
└── main.py

### Capas principales

#### Capa UI
Esta capa se encarga de la itneracción del usuario con la interfaz.

**RESPONSABILIDADES:**
- Muestra menues.
- Captura las entradas/inputs.
- Muestra tableros, resultados, los movimientos e interacciones de piezas.
- Gestiona la navegación en la interfaz.

##### Componentes
- MenuManager
- Gamerender
- InputHandler

#### Capa de Aplicación
Es la capa que coordina el flujo de la aplicación.

**RESPONSABILIDADES:**
- Gestiona las partidas.
- Coordina las acciones de los jugadores.
- Controla los turnos.
- Contecta la UI con la capa Dominio.

##### Componentes
- GameService
- TurnManager
- MatchController

#### Capa de Dominio
Contiene todas las clases de piezas, reglas, la lógica que comanda el centro del juego, y las interacciones que tendrán las piezas entre si y con el terreno.

**RESPONSABILIDADES:**
- Reglas del juego.
- Movimiento de piezas.
- Validación de interacciones.
- Estado del tablero.

##### Componentes
- Board.
- AI.
- Combat.
- Match.
- Units.
- Terrain.

#### Capa de Almacenamiento
Se encarga del guardado de los datos de mejores jugadores y sus puntajes.

**RESPONSABILIDADES:**
- Guarda los resultados.
- Carga partida.
- Maneja los archivos txt.

##### Componentes
- SaveManager.
- FileRepository.
- Serializer.

#### Capa de Recursos
Contiene los recursos del proyecto, animaciones, imagenes, audios.
