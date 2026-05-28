# Diagrama de flujo de datos

![Diagrama_de_flujo_de_datos](/Images/DIAGRAMA_DE_FLUJO_SHAH_MAT.JPEG)

                  [ INPUT ]
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
┌──────────────┐            ┌────────────────────────────────┐
│ Dispositivos │            │       Datos Ingresados         │
│  de Entrada  │            ├────────────────────────────────┤
├──────────────┤            │ • Selección de modo de juego   │
│ • Teclado    │            │ • Iniciales del jugador        │
│ • Ratón      │            │ • Comandos de movimiento       │
└──────────────┘            │ • Acciones (atacar, defender)  │
                            │ • Ajustes de accesibilidad     │
                            └────────────────────────────────┘
                                            │
                                            ▼
                             [ PROCESAMIENTO INTERNO ]
                                            │
             ┌──────────────────────────────┼──────────────────────────────┐
             ▼                              ▼                              ▼
┌────────────────────────┐    ┌────────────────────────┐    ┌────────────────────────┐
│    Gestión de Menú     │    │   Gestión de Partida   │    │  Sistema de Puntuación │
├────────────────────────┤    ├────────────────────────┤    ├────────────────────────┤
│ • Muestra opciones     │    │ • Inicializa tablero   │    │ • Verifica victorias   │
│ • Valida selección     │    │ • Carga piezas/turnos  │    │   y derrotas           │
│ • Redirige secciones   │    │ • Ejecuta reglas IA    │    │ • Organiza el ranking  │
└────────────────────────┘    └────────────────────────┘    └────────────────────────┘
                                            │
                                            ▼
                                  [ ALMACENAMIENTO ]
                                            │
                    ┌───────────────────────┴───────────────────────┐
                    ▼                                               ▼
┌──────────────────────────────────────┐        ┌──────────────────────────────────────┐
│          Archivos TXT Local          │        │         Logs Administrativos         │
├──────────────────────────────────────┤        ├──────────────────────────────────────┤
│ • Ranking de mejores jugadores       │        │ • Modificaciones del sistema         │
│ • Iniciales y mejor puntuación       │        │   (Solo usuario creador)             │
└──────────────────────────────────────┘        └──────────────────────────────────────┘
                                            │
                                            ▼
                                       [ OUTPUT ]
                                            │
             ┌──────────────────────────────┼──────────────────────────────┐
             ▼                              ▼                              ▼
┌────────────────────────┐    ┌────────────────────────┐    ┌────────────────────────┐
│   Durante la Partida   │    │    Final de Partida    │    │     Configuración      │
├────────────────────────┤    ├────────────────────────┤    ├────────────────────────┤
│ • Renderizado voxel    │    │ • Pantalla de Victoria │    │ • Despliegue de reglas │
│ • Mensajes de combate  │    │   o Derrota            │    │ • Comandos y tutorial  │
│ • Estado de turnos     │    │ • Despliegue del top   │    │   básico inicial       │
└────────────────────────┘    └────────────────────────┘    └────────────────────────┘


┌────────────────────────────────┐
│ JUGADOR INICIALIZA APLICACIÓN  │
└───────────────┬────────────────┘
                ▼
┌────────────────────────────────┐
│   Se muestra Interfaz Inicial  │◀──────────────────────────────────┐
│       (Menú Principal)         │                                   │
└───────────────┬────────────────┘                                   │
                ▼                                                    │
┌────────────────────────────────┐                                   │
│   Entrada (Teclado / Ratón)    │                                   │
└───────────────┬────────────────┘                                   │
                ▼                                                    │
       ¿Jugar una Partida? ───[NO]───► ¿Ver Configuración? ───[SI]──► Carga Reglamento,
                │                               │                     Comandos y Tutorial
              [SI]                            [NO]                            │
                │                               │                             ▼
                ▼                               ▼                    [ Volver al Menú ]
┌────────────────────────────────┐       ¿Desea Salir? ───[SI]───► [ FIN DEL PROGRAMA ]
│      Carga Motor de Juego      │
└───────────────┬────────────────┘
                ▼
┌────────────────────────────────┐
│       INICIA LA PARTIDA        │
├────────────────────────────────┤
│ • Inicializa tablero 10X10     │
│ • Posiciona piezas (voxel art) │
└───────────────┬────────────────┘
                ▼
┌────────────────────────────────┐
│       CICLO DE JUEGO           │◀─────────────────────────────────┐
├────────────────────────────────┤                                   │
│ • Asignación de Turno          │                                   │
│ • Input de comando / movimiento│                                   │
│ • Procesamiento de Reglas      │                                   │
│ • Output: Mensajes de combate  │                                   │
└───────────────┬────────────────┘                                   │
                ▼                                                    │
    ¿Cumple Criterio de Fin?                                         │
    (Rey Eliminado / Rendición)                                      │
                │                                                    │
         ┌──────┴──────┐                                             │
        [SI]          [NO] ──────────────────────────────────────────┘
         │
         ▼
┌────────────────────────────────┐
│       FIN DE LA PARTIDA        │
├────────────────────────────────┤
│ • Detiene procesamiento        │
│ • Calcula puntaje final        │
└───────────────┬────────────────┘
                ▼
┌────────────────────────────────┐
│      SISTEMA DE PERSISTENCIA   │
├────────────────────────────────┤
│ • Compara puntaje con el Top   │
│ • ¿Entra al Ranking?           │
│   ├── [SI] Pide iniciales      │
│   └── [NO] Continua            │
│ • Escribe archivo .txt local   │
└───────────────┬────────────────┘
                │                                         [REGRESO A MENU PRINCIPAL]
                └────────────────────────────────────────────────────┘

### ESTE ES UN MODELO DEL DIAGRAMA DE FLUJO, PARA VISUALIZAR EL DIAGRAMA COMPLETO, REFERIRSE A IMAGEN DEL INICIO