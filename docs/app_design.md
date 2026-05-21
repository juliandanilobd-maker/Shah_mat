# Diseño del sistema

En este archivo se encuentran las decisiones de diseño, planificacion previa a la escritura del código

# Objetivo general
Crear un sistema de estrategia interactivo, que usa como base el juego de mesa persa 'Shatranj', usando una lógica e ideas propias del desarrollador.

# Objetivos especificos

- Desarrollo del ciclo de vida de software.
- Implementar arquitectura modular por capas.
- Implementar Programación Orientada a Objetos.
- Desarrollar la lógica del sistema.
- Separación de responsabilidades.
- Uso de buenas prácticas de desarrollo de software.
- Aplicación de principios de Integración continua.
- Simular un juego estructurado, atractivo para el usuario.

# Principios de Diseño

## Arquitectura modular por capas
Se presenta una arquitectura por capas, con separación de responsabilidades, donde se presenta:

- Capa de aplicación (app).
- Capa de presentación (UI).
- Capa de dominio (Domain).
- Capa audiovisual (Rendering/Assets).
- Capa de almacenamiento (Storage). 

---
### Organización por módulos
La misma que se combina con una arquitectura por módulos:
- UI, módulos: menu, screens, HUD, tutorial, config, animations.
- Aplicacion, módulos: game_flow, controllers, services, managers.
- Dominio, módulos: board, units, combat, progression, AI, rules, terrain, match.
- Almacenamiento/persistencia, módulos: repositories, serializers, local_storage, logs.
- Audiovisual, módulos: rendering, assets, animation, audio.

---
## Programación Orientada a Objetos
Un diseño de programación orientada a objetos.

### Clases Principales

- **GAME:** controla el flujo de la partida.

- **BOARD:** representa el tablero del juego.

- **PLAYER:** representa a cada jugador.

- **UNIT:** clase base de las piezas o unidades.

- **MOVEMENTRULES:** gestiona la validez del movimiento.

- **TURNCONTROLLER:** controla el cambio de turnos.

---
## Encapsulamiento
Agrupacion de los datos en una sola unidad ---> CLASES. Asegurando la protección del estado interno del sistema.

---
## Abstracción
Se exponen unicamente los detalles esenciales de los objetos, su lógica interna se mantiene oculta.

---
## Herencia
Las unidades de juego se conforman sobre una base, heredan funciones de una pieza madre, permitiendo reutilización y extensión de comportamientos.

---
## Polimorfismo
Todas las piezas tendrán un mismo metodo, una misma acción en común, el polimorfismo se refiere a funciones, metodos generales que se pueden reutilizar en diferentes niveles.

---
## Separación de responsabilidades
Cada capa, archivo, carpeta se encarga de una función, en conjunto permiten una experiencia armoniosa y un troubleshooting más sencillo.

---
## Bajo acoplamiento
Si se van construyendo dinámicas de dependencia en secuencia, generamos una estructura debil, si falla una sola de las previas, se cae todo el proyecto, un bajo acoplamiento, permite cambios y modificaciones en varios niveles sin dañar todo el proyecto.

---
## Alta cohesión
Cada módulo programado agrupa elementos, todas las clases y objetos tienen un propósito definido.

---
# Patrones de Diseño
Se exponen varios patrones que se usaron de forma complementaria a la arquitectura y diseño general de la aplicación, se usaran y tomarán ideas, formas de trabajo de estos patrones para ciertos casos.

---
## Factory Pattern
Para la creación dinámica de unidades de combate (las piezas del juego).

---
## MVC
Modelo-Vista-Controlador, permite separar la interfaz de usuario, con la lógica del juego y los datos

---
## Service Layer
Es patrón sirve para establecer el límite entre la interfaz del usuario y la lógica interna.

---
## Repository Pattern
Es una capa que abstrae la lógica del juego de la capa de datos.

---
## Singleton
Garantiza el uso de una clase con una única instancia para toda la aplicación.
Principalmente para casos específicos, como Gamemanager o Audiomanager.

---
## Strategy Pattern
Este patrón aisla el código y las dependencias de ciertos algoritmos del resto del código, especificamente para el desarrollo de la IA vs Jugador, modalidad Easy, Medium, Hard.

---
## Escalabilidad

La arquitectura está diseñada para permitir extensión del sistema, sin modificaciones estructurales profundas.

---
# Ideas futuras

- Nuevos tipos de unidades.
- IA contra jugador.
- Interfaz gráfica.
- Nuevas reglas de juego, terreno y objetos usables en la partida.
