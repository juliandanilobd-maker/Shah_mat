# Inicio de la aplicación

INICIA PROGRAMA

crear GameService
cargar configuraciones
cargar recursos 
cargar storage

Llama  GameService empieza


# Capa de aplicación

Funcion start

    Mostrar el menu principal

    Mientras el juego este activo

        Opcion -> Menu, obtener selecciones del Menu

        Si la opcion es 'Nueva Partida VS IA'
            Inicia partida con IA

        Si la opcion es 'Nueva Partida 1 vs 1'
            Inicia partida 1 vs 1

        Si la opcion es 'Configuracion'
            Mostrar configuración

        Si la opcion es 'Salir'
            Salir del Juego

Fin de la funcion

# Iniciar Partida

Funcion Iniciar Partida:

    crear MatchController
    crear Board
    crear Players
    crear TurnManager
    crear CombatSystem

    Inicia el juego

    llama a Loop de partida

Fin de la funcion

# Loop de partida

Funcion Loop de partida:

    Mientras la partida no termine

        jugador actual -> TurnManager jugador actual

        UI muestra el estado del trablero

        accion del jugador -> UI recibe input

        resultado -> aplicacion procesa accion

        Si el resultado es 'ATAQUE'
            daño -> CombatSystem calcula el daño
            Capa Domain -> Board aplica el daño

        Si el resultado es 'HABILIDAD'
            Capa Domain -> aplica la habilidad

        
        actualizar la UI

        verificar si se cumplen las condiciones de fin de turno

        cambiar el turno

    FIN del turno

    FIN DE PARTIDA

Fin de la funcion

# Capa Dominio

## Board

Funcion mover unidad, argumentos: desde donde, a donde

    Si el movimiento es valido
        mueve la pieza

    Si no
        Error: 'La pieza no se puede mover ahi'

Fin de la funcion

## Estados de vida de piezas

Funcion estado de vida(estado blindado, estado saludable, estado herido, estado eliminacion)

        Si pieza esta en estado blindado -> Escudo y salud completos

        Si pieza esta en estado saludable -> Escudo eliminado y salud compelta

        Si pieza esta en estado herido -> Salud a mitad

        Si pieza esta en estado eliminacion -> Pieza eliminada 

## CombatSystem

Funcion calcular el daño(propio, otra pieza)

    atacante -> unidad atacante ataca
    otra pieza (defensor) -> unidad recibe ataque

        SI el daño base > Defensa = - 1 estado

            si ya no hay estados -> Pieza eliminada

        devolver estado final de la pieza

Fin de la funcion

## AI computadora vs jugador

Funcion decidir accion(tablero)

    computadora revisa estado:

        tablero
        piezas
        posicion

        Si la dificultad es 'EASY'
            se elige un movimiento al azar

        Si la dificultad es 'MEDIUM'
            se elige el mejor ataque

        Si la dificultad es 'HARD'
            se analizan todas las jugadas posibles y se escoge la mejor

    devuelve accion

Fin de la funcion

# Capa de Aplicación

## Procesar acción

Funcion procesar accion

    Si la accion es 'MOVIMIENTO'
        Validar con capa Domain

    Si la accion es 'ATAQUE'
        Validar rango y reglas

    Si la accion es 'HABILIDAD'
        Validar la disponibilidad

    devolver resultado

Fin de la funcion

# Capa de Almacenamiento

## Fin de partida

Funcion fin de partida

    calcular puntajes

    Si el jugador entra en el ranking
        Almacenamiento guarda ranking -> Iniciales y puntaje

    Almacenamiento guarda estadisticas

    UI muestra la pantalla final

    'VOLVER AL MENU'

Fin de la funcion

## SaveManager

Funcion guardar ranking

    leer el archivo ranking.txt

    agregar nuevo puntaje e iniciales

    ordenar el ranking de mayor a menor

    guardar

Fin de la funcion

# Capa UI

## InputHandler

Funcion recibir Input

    Esperar el clic o teclado

    Traducir Input a una acción

    devolver accion traducida

Fin de la funcion

## Render

Funcion mostrar el estado del tablero

    dibujar el tablero

    dibujar unidades

    mostrar estadisticas al jugador

    mostrar turno actual

Fin de la funcion

## Fin del juego

Funcion verificar condiciones de fin de partida

    Si el jugador 1 pierde su rey
        Partida termina

    Si el jugador 2 pierde su rey
        Partida termina

Fin de la funcion



    