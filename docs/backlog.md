# Backlog

## Prioridades usadas:
- Alta: Fundamental para el funcionamiento.
- Media: Mejoras importantes.
- Baja: Funcionalidades de diseño, o para futuras fases.

## Estados de actividades:
- Completado: Actividad terminada.
- En curso: En desarrollo.
- Pendiente: En espera, falta desarrollar.
- Futuro: Proximas funcionalidades.

## DOD (Definition of Done): Definicion de completado:
Una actividad se considera completada cuando:

- El código funciona.
- Cumple los criterios de aceptación.
- No hay errores o bugs.
- Se integra en la arquitectura.
- Se prueba manualmente.
- Mantiene estilo modular por capas o estilos de diseño de la app.


# EPICA 1 - Sistema base del juego

## Objetivo
Construir la base del juego

## Historia 1.1 - Base inicial

### Prioridad: ALTA.
### Estado: EN CURSO.

#### Descripción
Como jugador lo primero es iniciar una partida, para comenzar el juego.

### Criterios de aceptación
- [] Crear menú principal.
- [] Crear inicialización de partida.
- [] Configurar tablero inicial.

## Historia 1.2 - Configurar tablero

### Prioridad: ALTA.
### Estado: EN CURSO.

#### Descripción
Como jugador, necesito ver el tablero para entender el juego.

### Criterios de aceptación
- [] Renderizar tablero.
- [] Mostrar posiciones.
- [] Actualizar el tablero.

# EPICA 2 - Sistema de turnos

## Objetivo
Crear el sistema que maneja los turnos, cuando inician, cuando se acaban, pasa al siguiente turno.

## Historia 2.1 - Base del turno

### Prioridad: ALTA.
### Estado: EN CURSO.

#### Descripción
Como jugador, necesito moverme por turnos

### Criterios de aceptación
- [] Implementar control de turnos.
- [] Validar el jugador activo.
- [] Alternar entre jugadores.

# EPICA 3 - Movimiento y reglas

## Objetivo
Generar la lógica y manejo de los movimientos de las piezas en el juego.

## Historia 3.1 - Primeros movimientos

### Prioridad: ALTA.
### Estado: EN CURSO.

#### Descripción
Como jugador, es necesario para jugar el juego, que las piezas se muevan en base a reglas.

### Criterios de aceptación
- [] Validar movimientos.
- [] Detectar posiciones invalidas.
- [] Actualizar el estado del tablero despues de un movimiento.

## Historia 3.2 - Interacciones de piezas

### Prioridad: ALTA.
### Estado: EN CURSO.

#### Descripción
Como desarrollador es necesario validar las reglas del juego, para mantener la coherencia con las interacciones.

### Criterios de aceptación
- [] Detectar colisiones entre piezas (dos piezas una al lado).
- [] Verificar los limites de daño, movilidad, alcance.
- [] Aplica las reglas en las interacciones de las piezas.

# EPICA 4 - Persistencia

## Objetivo
Crear persistencia de datos que asegure el mantenimiento de la partida y el registro de los mejores puntajes y el nombre de los jugadores propietarios de ese puntaje en archivos txt locales.

## Historia 4.1 - Almacenamiento de datos

### Prioridad: ALTA.
### Estado: EN CURSO.

#### Descripción
Como jugador me gustaria poder continuar una partida que deje a medias, y que se guarden los mejores puntajes

### Criterios de aceptación
- [] Crear serialización.
- [] Guardar estado.
- [] Cargar partida.
- [] Guarda mejores puntajes.

# EPICA 5 - Testing

## Objetivo
Crear funciones de testing que permitan valorar el correcto funcionamiento de objetos, capas y funciones.

## Historia 5.1 - Pruebas unitarias

### Prioridad: ALTA.
### Estado: EN CURSO.

#### Descripción
Como desarrollador, es fundamental pruebas unitarias para validar el funcionamiento.

### Criterios de aceptación
- [] Testing de movimientos.
- [] Testing de turnos.
- [] Testing de reglas.

