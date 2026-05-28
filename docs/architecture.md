# Arquitectura del proyecto - Throne & Treason

## Diagrama de arquitectura

Flujo de datos en arquitectura

1. [JUGADOR]
       ↓
2. [UI(View)]
       ↓ eventos
3. [APPLICATION (Controllers/Services)]
       ↓ llamadas
4. [DOMAIN (Rules, Board, Units, Combat, AI)]
       ↓ resultados
5. [APPLICATION]
       ↓ decide persistencia
6. [STORAGE]

Estructura Principal
Sitrang/
│
├── .github/
├── app/
│   ├── ui/
│   ├── application/
│   ├── domain/
│   ├── infraestructure/
│   └── assets/
├── .venv/
├── docs/
├── tests/
├── README.md
├── requirements.txt
└── main.py

### Capas principales

#### Capa UI
Esta capa se encarga de la itneracción del usuario con la interfaz.

**RESPONSABILIDADES:**
- Navegación de menues.
- Captura las entradas/inputs.
- Muestra tableros, resultados, los movimientos e interacciones de piezas.
- Gestiona la navegación en la interfaz.

##### Componentes
- Animations
- Config
- HUD
- Menu
- Rendering
- Screens
- Tutorial

#### Capa de Aplicación
Es la capa que coordina el flujo de la aplicación.

**RESPONSABILIDADES:**
- Gestiona las partidas.
- Coordina las acciones de los jugadores.
- Controla los turnos.
- Contecta la UI con la capa Dominio.

##### Componentes
- Controllers
- Manager
- Services

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
- Player.
- Terrain.
- Turn.
- Rules.

#### Capa de Infraestructura
Se encarga del guardado de los datos de mejores jugadores y sus puntajes.

**RESPONSABILIDADES:**
- Guarda los resultados.
- Carga partida.
- Maneja los archivos txt.

##### Componentes
- Local_storage.
- Logs.
- Repositories.
- Serializers.


┌─────────────────────────────────────────────────────────────────────┐
│                           CAPA UI                                   │
│─────────────────────────────────────────────────────────────────────│
│ Responsabilidad:                                                    │
│ Interacción con el usuario y representación visual del juego.       │
│                                                                     │
│ Componentes:                                                        │
│  • Animations                                                       │
│  • Config                                                           │
│  • HUD                                                              │
│  • Menu                                                             │
│  • Rendering                                                        │
│  • Screens                                                          │
│  • Tutorial                                                         │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                │ Inputs / Eventos
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    CAPA DE APLICACIÓN                               │
│─────────────────────────────────────────────────────────────────────│
│ Responsabilidad:                                                    │
│ Coordinar el flujo general del juego y conectar UI con Dominio.     │
│                                                                     │
│ Componentes:                                                        │
│  • Controllers                                                      │
│  • Manager                                                          │
│  • Services                                                         │
│                                                                     │
│ Funciones principales:                                              │
│  • Gestionar partidas                                               │
│  • Coordinar acciones                                               │
│  • Controlar turnos                                                 │
│  • Ejecutar servicios de movimiento y reglas                        │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                │ Lógica / Casos de uso
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      CAPA DE DOMINIO                                │
│─────────────────────────────────────────────────────────────────────│
│ Responsabilidad:                                                    │
│ Contener toda la lógica central y reglas del juego.                 │
│                                                                     │
│ Componentes:                                                        │
│  • Board                                                            │
│  • AI                                                               │
│  • Combat                                                           │
│  • Match                                                            │
│  • Units                                                            │
│  • Terrain                                                          │
│  • Player                                                           │
│  • Turn                                                             │
│  • Rules                                                            │
│                                                                     │
│ Funciones principales:                                              │
│  • Reglas del juego                                                 │
│  • Movimiento de piezas                                             │
│  • Validación de interacciones                                      │
│  • Estado del tablero                                               │
│  • Combate y turnos                                                 │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                │ Persistencia / Datos
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                  CAPA DE INFRAESTRUCTURA                           │
│─────────────────────────────────────────────────────────────────────│
│ Responsabilidad:                                                    │
│ Manejar almacenamiento y persistencia de datos.                    │
│                                                                     │
│ Componentes:                                                        │
│  • Local_storage                                                    │
│  • Logs                                                             │
│  • Repositories                                                     │
│  • Serializers                                                      │
│                                                                     │
│ Funciones principales:                                              │
│  • Guardar resultados                                               │
│  • Cargar partidas                                                  │
│  • Manejar archivos txt                                             │
│  • Serializar datos                                                 │
└─────────────────────────────────────────────────────────────────────┘

