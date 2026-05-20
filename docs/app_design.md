# Diseño de la app

En este archivo se encuentran las decisiones de diseñ, planificacion previa a la escritura del código

## Objetivo general
Crear un juego de estrategia interactivo, que usa como base el juego de mesa de fantasía Sitrang, usando una lógica e ideas propias del desarrollador.

## Objetivos especificos

- Desarrollo del ciclo de vida de software.
- Implementar arquitectura modular por capas.
- Implementar desarrollo orientado a objetos.
- Desarrollar la lógica de juego.
- Separación de responsabilidades.
- Uso de buenas prácticas.
- Aplicación de principios de Integración continua.
- Simular un juego estructurado, atractivo para el usuario.

## Principios de Diseño

### Arquitectura modular por capas
Se presenta una arquitectura por capas, con separación de responsabilidades, donde se presenta:
- Capa de aplicación.
- Capa de presentación.
- Capa de dominio.
- Capa audiovisual.
- Capa de assets.
- Capa de almacenamiento.

La misma que se combina con una arquitectura por módulos:
- UI, módulos: menu, screens, HUD, tutorial, config, animations.
- Aplicacion, módulos: game_flow, controllers, services, managers.
- Dominio, módulos: board, units, combat, progression, AI, rules, terrain, match.
- Almacenamiento/persistencia, módulos: repositories, serializers, local_storage, logs.
- Audiovisual, módulos: rendering, assets, animation, audio.


### Programación Orientada a Objetos
Un diseño de programación orientada a objetos.

#### Clases Principales

##### GAME
Controla el flujo de la partida.

##### BOARD
Presenta el tablero del juego.

##### PLAYER
Presenta a cada jugador.

##### UNIT
Clase básica de piezas o unidades.

##### REGLAS DE MOVIMIENTO
Gestiona la validez del movimiento.

##### CONTROLADOR DE TURNO
Controla el cambio de turnos.


### Encapsulamiento
Agrupacion de los datos en una sola unidad ---> CLASES.
 
### Abstracción
Se usan los detalles esenciales de los objetos, su lógica interna se mantiene oculta.

### Herencia
Las clases de piezas se conforman sobre una base, heredan funciones de una pieza madre.

### Polimorfismo
Todas las piezas tendrán un mismo metodo, una misma acción en común, el polimorfismo se refiere a funciones, metodos generales que se pueden reutilizar en diferentes niveles.

### Separación de responsabilidades
Cada capa, archivo, carpeta se encarga de una función, en conjunto permiten una experiencia armoniosa y un troubleshooting más sencillo.

### Bajo acoplamiento
Si se van construyendo dinámicas de dependencia en secuencia, generamos una estructura debil, si falla una sola de las previas, se cae todo el proyecto, un bajo acoplamiento, permite cambios y modificaciones en varios niveles sin dañar todo el proyecto.

### Alta cohesión
Todo lo que se programa, todas las clases y objetos tienen un propósito definido.


## Patrones de Diseño
Se exponen varios patrones que se usaron de forma complementaria a la arquitectura y diseño general de la aplicación, se usaran y tomarán ideas, formas de trabajo de estos patrones para ciertos casos.

### Patrones Creacionales

#### Factory
Para la creación dinámica de unidades de combate (las piezas del juego).

### MVC
Modelo-Vista-Controlador, permite separar la interfaz de usuario, con la lógica del juego y los datos

### Capa de Servicios
Es patrón sirve para establecer el límite entre la interfaz del usuario y la lógica interna.

### Capa de Repositorio
Es una capa que abstrae la lógica del juego de la capa de datos.

### Singleton
Garantiza el uso de una clase con una única instancia para toda la aplicación.
Principalmente para casos específicos, como Gamemanager o Audiomanager.

### Strategy
Este patrón aisla el código y las dependencias de ciertos algoritmos del resto del código, especificamente para el desarrollo de la IA vs Jugador, modalidad Easy, Medium, Hard.

## Escalabilidad

La arquitectura está diseñada para escalabilidad.

## Ideas futuras

- Nuevos tipos de unidades.
- IA contra jugador.
- Interfaz gráfica.
- Nuevas reglas de juego, terreno y objetos usables en la partida.
