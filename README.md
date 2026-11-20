# Juegos mentales (Brain Games)

[![hexlet-check](https://github.com/samir-3435/python-project-140/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/samir-3435/python-project-140/actions)

«Juegos mentales» es una colección de cinco juegos matemáticos de consola interactivos. Cada juego realiza tres preguntas consecutivas al usuario. Si el usuario responde correctamente todas las preguntas, gana la partida; si comete un error, el juego termina inmediatamente.

Proyecto de aprendizaje de [Códica](https://app.codica.la/programs/python).

---

## Requisitos mínimos

* **Python:** Versión `3.10` o superior.
* **Gestor de paquetes:** [`uv`](https://docs.astral.sh/uv/) (recomendado).

---

## Instalación

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/samir-3435/python-project-140.git
   cd python-project-140
   ```

2. Compila el paquete:
   ```bash
   uv build
   ```

3. Instala el paquete globalmente con `uv tool`:
   ```bash
   uv tool install dist/*.whl --force
   ```

---

## Juegos disponibles y ejecución

Una vez instalado el paquete, puedes ejecutar cualquiera de los comandos directamente en tu terminal (sin necesidad de escribir `uv run`):

| Comando | Juego | Descripción |
| :--- | :--- | :--- |
| `brain-games` | **Saludo inicial** | Da la bienvenida y saluda al usuario por su nombre. |
| `brain-even` | **Par o impar** | Determina si un número aleatorio es par (`yes`) o impar (`no`). |
| `brain-calc` | **Calculadora** | Calcula el resultado de expresiones matemáticas aritméticas (+, -, *). |
| `brain-gcd` | **MCD** | Encuentra el máximo común divisor de dos números enteros. |
| `brain-progression` | **Progresión aritmética** | Adivina el número faltante en una secuencia aritmética. |
| `brain-prime` | **Número primo** | Determina si el número presentado es primo (`yes` o `no`). |

---

## Demostraciones (Asciinema)

A continuación puedes ver grabaciones de ejemplo de la ejecución de cada juego con casos de éxito y fallo:

* **Juego "Par o impar":** [![asciicast](https://asciinema.org/a/GVIW794B1dHOk9Hx.svg)](https://asciinema.org/a/GVIW794B1dHOk9Hx)
* **Juego "Calculadora":** [![asciicast](https://asciinema.org/a/qQ9YnmZFU6lITwPs.svg)](https://asciinema.org/a/qQ9YnmZFU6lITwPs)
* **Juego "Máximo común divisor":** [![asciicast](https://asciinema.org/a/FXMsghvzYVbU90N8.svg)](https://asciinema.org/a/FXMsghvzYVbU90N8)
* **Juego "Progresión aritmética":** [![asciicast](https://asciinema.org/a/a3T4H3irzYkIuZWu.svg)](https://asciinema.org/a/a3T4H3irzYkIuZWu)
* **Juego "Número primo":** [![asciicast](https://asciinema.org/a/K2sl40Wg7Oisg3Lc.svg)](https://asciinema.org/a/K2sl40Wg7Oisg3Lc)

---

<details>
<summary>Pruebas automáticas de Códica</summary>

Las pruebas se ejecutan en cada commit. El archivo `.github/workflows/hexlet-check.yml` es el responsable de ejecutarlas: no lo elimine ni lo renombre, y no cambie el nombre del repositorio.

</details>

## Acerca de Códica

[Códica](https://app.codica.la/) es una escuela de programación: programas de aprendizaje propios con práctica, apoyo de mentores y proyectos reales que quedan en su currículum. Este repositorio es uno de esos proyectos.
