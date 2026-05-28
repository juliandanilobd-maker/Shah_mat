# Shah Mat Juego de Estrategia
---
# INTRODUCCION
En este proyecto consiste en el desarrollo de un sistema de simulación estratégica basada en el juego de mesa, antecesor persa del ajedrez 'Shah Mat', se desarrolla como proyecto academico con principios de programación de buenas practicas de programación y desarrollo.

---
# OBJETIVO
El sistema tiene como objetivo el desarrollo de una aplicación de computadora que simula el juego de mesa 'Shah Mat'. El diseño se basa en principios escalabilidad, mantenimiento y separación de responsabilidades.

El sistema permite gestionar partidas, movimientos, validaciones de reglas, turnos de jugador, representación de mecánicas del sistema.

---
# VISTA PRINCIPAL
![Logo del Sistema](/Images/LOGO.png)
![Menú de inicio](/Images/MENU_INICIAL.png)

---
# ARQUITECTURA
Sistema ha sido desarrollado bajo arquitectura modular por capas, aplicando principios de Programación Orientada a Objetos, Clean Architecture, y SOLID, con la finalidad de garantizar la escalabilidad, mantenibilidad y bajo acoplamiento.

El proyecto está estructurado en capas insertadas principalmente en una carpeta app:

- 'app/': contiene las capas y módulos.
- 'docs/': contiene la documentación del proyecto.
- 'tests/': contiene las pruebas unitarias del proyecto.
- '.github/': contiene el workflow.

La arquitectura específica se encuentra detallada en architecture.md

---
# TECNOLOGIAS
- Python 3.11.
- GitHub y Git Actions.
- Pygame.
- JSON/txt.
- Pytest.
- Black.
- Flake8.
- Rich.

---
# FUNCIONALIDADES
- Inicio de partida
- Manejo de turnos
- Movimiento de piezas
- Validación de reglas y lógica interna
- Sistema de juego
- Menú interactivo

---
# REQUISITOS FUNCIONALES

## Requisitos de Actores
- El sistema está diseñado a usuarios individuales en entorno local sin distinciones de roles administrativos dentro de la aplicación.

---
## Requisitos de Interfaz
### Interacción del Usuario
- Aplicación de escritorio con ejecución local.
- Inputs mediante teclado y ratón.

---
### Pantallas del Sistema
- Menú Principal:
    - Iniciar Partida:
        - Jugador 1 vs Jugador 2
        - Jugador vs CPU
    - Mejores Puntuaciones
    - Configuración:
        - Tutorial
        - Reglamento
        - Comandos del sistema
- Pantalla de sistema.

---
### Navegación

Menú Principal --> Modo de Juego --> Partida --> Turnos --> Fin de la Partida --> Menú Principal

---
### Accesibilidad
- Textos Subtitulados.
- Tamaño de texto ajustable.
- Interfaz en Español.

---
### Diseño visual
- Estetica Voxel Art.
- Paleta de colores terrosa.
- Tipografía estilo arcade.

---
## Requisitos de Sistema
### Mecánicas
- Sistema estratégico por turnos.
- Sistema progresivo.
- Eliminar unidades enemigas.
- Opción de rendirse.
- Obstáculos en el mapa.

---
### Estadísticas de Unidades
Cada unidad incluye:
* Vida
* Ataque
* Defensa
* Alcance
 ---
### Modos de Juego
- Jugador vs Jugador
- Jugador vs CPU

---
## Requisitos de Procesamiento
### Input
-  Interacción mediante dispositivos de entrada (mouse y teclado).
- Entradas del teclado.
- Nombre del jugador.
- Seleccionar acciones.
- Resultado de partida.
 ---
### Procesamiento interno
- Gestión de turnos.
- Validar movimientos.
- Procesar ataques y defensas.
- Actualizar estado del tablero.
- Eliminar unidades derrotadas.
- Calcular puntaje.
- Registrar estadísticas.
- Compara puntuaciones con el ranking.
- Gestionar desbloqueos progresivos.

---
### Output
- Resultados de combate.
- Mensajes de ataque y defensa.
- Ranking de puntuaciones.
- Estadísticas de partida.
- Estado actualizado del tablero.

## Requisitos de persistencia
- Ranking de puntuaciones.
- Iniciales de jugadores.
- Estadísticas de victorias y derrotas.
- Dificultades superadas.
- Unidades desbloqueadas.

---
### Persistencia local
- Almacenamiento local en archivos .txt.
- Sin base de datos remota.
- Datos guardados de forma local.

---
## Requisitos de Gestión y Administración
- Solo usuarios autorizados pueden modificar el código.
- No se pueden modificar rankings o estadísticas.
- No existen herramientas de administración accesibles desde la UI.

---
# Requisitos no funcionales
## Disponibilidad
- Sistema disponible para ejecución local.
- No depende de servicios externos o red internet.

---
## Rendimiento
- Respuesta inmediata a acciones del usuario.
- Fluidez en actualización de gráficos y estados.
- Procesamiento local optimizado.

---
## Calidad
El sistema debe ser:
- Modular.
- Escalable.
- Comprensible.
- Refactorizable.
- Mantenible.
- Documentado.

El sistema deberá ejecutarse sin errores críticos, con una experiencia fluida y estable.

---
## Seguridad
- Solo usuarios autorizados acceden a código fuente.
- Modificación interna restringida.

---
## Trazabilidad
- Control de versiones por GitHub.
- Historial de cambios.
- Registro de modificaciones del sistema.

---
## Escalabilidad
- Nuevos modos de juego.
- Nuevas unidades.
- Expansión del mapa.
- Mejoras visuales.
- Nuevos sistemas estratégicos.

---
# Requisitos del Sistema
Descripción de los requisitos técnicos y de entorno necesarios para la ejecución del sistema 'Shah Mat Juego de Estategia'

## Arquitectura del Sistema
Se compone de los siguientes módulos:

- **Módulo de dominio:** contiene la lógica del juego, reglas, entidades y comportamientos del sistema.
- **Módulo de interfaz:** gestiona la interacción del sistema con el usuario y la presentación del estado del sistema.
- **Módulo de persistencia:** administra el almacenamiento local de datos y estadísticas.
- **Módulo audiovisual:** gestiona los recursos gráficos y elementos audiovisuales del sistema.

---
## Requisitos de Software
El sistema deberá ejecutarse bajo las siguientes condiciones:
- Sistema Operativo: Windows 10 o superior.
- Lenguaje de Programación: Python 3.10 o superior.
- Entorno de Ejecución: Local (Offline).
- El sistema no depende de servicios externos o servidores remotos.

---
## Requisitos de Hardware
Mínimos recomendables, el sistema está diseñado para ser ejecutado en equipos de gama básica:
| Componente | Requerimento |
| --- | --- |
| CPU | 1.5 GHz |
| RAM | 2 GB |
| Disco Duro | 200 MB |
| GPU | No requerida |

---
## Requisitos de Ejecución
- El sistema deberá ejecutarse en entornos locales.
- La interacción se realiza mediante teclado y mouse.
- El rendimiento dependerá directamente del hardware del usuario.

---
## Requisitos de Contingencia
- Si el programa cierra inesperadamente durante una partida, solo se perderá el progreso actual.
- Las estadísticas y rankings previamente guardados, permanecen como tal.

---
## Restricciones del sistema
- El sistema no cuenta con conexión en red.
- No se permite Multijugador Online, LAN o Bluetooth.
- No existe sincronización entre dispositivos.
- No se implementa guardado automático.
- No se implementa modificación avanzada de piezas.
- No se implementa audio avanzado o mods externos.
- No se permite compatibilidad con periféricos.
- No se permite acceso WEB.

---
## Supuestos del Sistema
- El usuario dispone de un computador con sistema operativo compatible.
- El usuario cuenta con permisos para ejecución local.
- El entorno de ejecución es estable y sin restricciones de seguridad.
- El hardware cumple con los criterios mínimos.

---
## Escalabilidad del Sistema
El diseño permite futuras extensiones, tales como:
- Incorporación de IA avanzada.
- Implementación de Interfaz gráfica mejorada.
- Expansión del sistema de unidades y reglas.
- Adición de nuevos modos de juego.
- Integración de efectos visuales y sonido.

---
# UML
![Diagrama de Clase](/Images/DIAGRAMA_DE_CLASES.png)
![Diagrama de Caso de Uso](/Images/DIAGRAMA_DE_CASO_DE_USO.png)
![Diagrama de Componentes](/Images/DIAGRAMA_DE_COMPONENTES.png)
![Diagrama de Secuencia](/Images/DIAGRAMA_DE_SECUENCIA.png)

