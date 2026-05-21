# Roadmap - Shah Mat Juego de Estrategia

Este documento define la planificación evolutiva del proyecto, organizada por fases de desarrollo.

# Fase 0 - Preparación del proyecto

## Version Inicial - 0.0.0 Base conceptual del proyecto

### Objetivo
Definir requisitos, alcance del proyecto, metodología y diseño.

### Estado
- Definir requisitos y alcance.
- Diseño del juego.
- Definir reglas.
- Definición de arquitectura y diseño.
---
# Fase 1 — MVP (Minimum Viable Product)

## 0.1.0 — Estructura base (Non-functional)

### Objetivo
Establecer la base del proyecto y su arquitectura.

### Funcionalidades

- Estructura modular por capas
- Configuración inicial del proyecto
- Documentación base
- README.md principal
- Configuración de GitHub y GitHub Actions

### Enfoque técnico

- Preparación del entorno de desarrollo
- Separación inicial de capas (UI / Application / Domain / Storage)
- Base para CI/CD

---
## 0.2.0 — Núcleo de interfaz y tablero (Non-functional)

### Objetivo
Iniciar la interacción básica del usuario con el sistema.

### Funcionalidades

- Menú principal
- Inicialización de partidas
- Creación de tablero

### Enfoque técnico

- Implementación inicial de UI Layer
- Estructura de GameService básica
- Representación inicial del estado del juego

---

## 0.3.0 — Lógica de juego base (Non-functional)

### Objetivo
Implementar la lógica fundamental del juego.

### Funcionalidades

- Sistema de turnos
- Movimiento de piezas
- Validación de reglas básicas

### Enfoque técnico

- Implementación de Domain Layer
- Control de estado del tablero
- Validaciones de movimientos
- Alternancia de jugadores

---

## 0.4.0 — Persistencia del sistema (Non-functional)

### Objetivo
Agregar almacenamiento local de partidas.

### Funcionalidades

- Guardado de partidas
- Cargar partidas

### Enfoque técnico

- Implementación de Storage Layer
- Serialización de estado del juego
- Persistencia en archivos locales (TXT)

---

## 0.5.0 — Testing y validación (Non-functional)

### Objetivo
Asegurar la estabilidad del sistema.

### Funcionalidades

- Validación de componentes críticos
- Pruebas funcionales globales

### Enfoque técnico

- Uso de pytest
- Testing de Domain Layer
- Validación de GameService y reglas del juego
- Refactorización basada en resultados de tests

---

# Versión 1.0.0 — Sistema funcional (MVP completo)

## Objetivo
Consolidar el sistema como un juego completamente funcional.

### Funcionalidades

- Juego funcional completo (MVP)
- Arquitectura consolidada
- Documentación final

### Enfoque técnico

- Integración completa de capas
- Flujo completo del sistema:
  UI → Application → Domain → Storage
- Sistema estable y jugable
- Base lista para futuras expansiones

---

# Evolución futura (Post 1.0.0)

Aunque no forma parte del MVP, el sistema está diseñado para crecer hacia:

- IA para modo jugador vs computador
- Interfaz gráfica (GUI)
- Sistema de progresión y desbloqueos
- Nuevos tipos de unidades
- Expansión de reglas estratégicas
- Mejora de experiencia visual

---

# Nota de arquitectura

Cada versión incremental está diseñada para mantener:

- Bajo acoplamiento
- Alta cohesión
- Separación estricta de capas
- Evolución controlada del dominio del juego