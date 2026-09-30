# Simple Calculator (Tkinter GUI)

A lightweight, dark-themed desktop calculator built using Python and Tkinter. This application offers a straightforward visual interface for carrying out everyday arithmetic operations without extra complexity or dependencies.

---

## Overview

The **Simple Calculator** is an event-driven graphical application built using Python's native `tkinter` library. It uses an expression-based string evaluator to process calculations dynamically, providing instant visual feedback on a monospace screen field. Designed with an intentional focus on simplicity, it handles essential arithmetic functions and includes built-in exception handling to recover cleanly from evaluation errors.

---

## Features

- **Essential Arithmetic Operations:** Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **Dark-Themed Layout:** Modern dark background with high-contrast text and custom button coloring for clear visibility.
- **Dynamic Expression Screen:** Real-time visual updates on the display entry as on-screen buttons are pressed.
- **Fault-Tolerant Error Handling:** Gracefully handles invalid syntax or math errors (e.g., division by zero) by displaying `error` instead of crashing.
- **Chained Calculations:** Retains evaluation results so users can continue operating on previous answers seamlessly.
- **One-Click Clear:** Dedicated **Clear** button to reset internal state and wipe the screen instantly.

---

## Current Scope & Constraints

- **Input Constraints:** Input is strictly bound to on-screen button clicks. *Physical keyboard and numpad keybindings are currently not supported.*
- **No Decimal Support:** Inputs are currently restricted to whole integers and operator selections.
- **Basic Functions Only:** Scientific functions, parentheses, memory functions ($M+$, $M-$), and calculation history are outside the current version's scope.

---

## Technologies Used

| Technology / Tool | Role in Project |
| :--- | :--- |
| **Python 3.x** | Core language handling expression state and runtime logic. |
| **Tkinter** | Standard GUI framework used to build widgets, window configuration, and grid layout management. |

---

## Installation & Setup

### Prerequisites

Ensure you have Python 3 installed on your machine. Check your Python version by running:

```bash
python --version
```
*(On macOS or Linux, run `python3 --version`)*

### Running the Application

1. **Clone or Download:** Save the project repository or script file (`main.py`) to your computer.
2. **Open Terminal / Command Prompt:** Navigate to the folder containing the file:
   ```bash
   cd path/to/your/calculator-directory
   ```
3. **Launch the Program:** Execute the script using Python:
   ```bash
   python main.py
   ```

*(Note for Linux users: If `tkinter` is missing, install it via `sudo apt-get install python3-tkinter`)*

---

## Usage Guide

1. **Enter Calculations:** Click the digit buttons (`0–9`) and operator keys (`+`, `-`, `*`, `/`) using your mouse to construct an algebraic expression.
2. **Compute Result:** Click the `=` button to evaluate the expression on the display screen.
3. **Reset Display:** Click the **Clear** button at any time to wipe the display and start a new expression.

---

## Manual Testing Cases

| Test Scenario | Action Sequence | Expected Display |
| :--- | :--- | :--- |
| **Addition** | Click `1` $\rightarrow$ `+` $\rightarrow$ `2` $\rightarrow$ `=` | `3` |
| **Operator Hierarchy** | Click `2` $\rightarrow$ `+` $\rightarrow$ `3` $\rightarrow$ `*` $\rightarrow$ `4` $\rightarrow$ `=` | `14` |
| **Division by Zero** | Click `5` $\rightarrow$ `/` $\rightarrow$ `0` $\rightarrow$ `=` | `error` |
| **Invalid Syntax** | Click `5` $\rightarrow$ `+` $\rightarrow$ `*` $\rightarrow$ `2` $\rightarrow$ `=` | `error` |
| **Clear Display** | Click `9` $\rightarrow$ `+` $\rightarrow$ `Clear` | *(Blank screen)* |
| **Chained Calculations** | Click `4` $\rightarrow$ `+` $\rightarrow$ `4` $\rightarrow$ `=` $\rightarrow$ `*` $\rightarrow$ `2` $\rightarrow$ `=` | `16` |

---

## Potential Roadmap & Enhancements

- [ ] Add hardware keyboard listener (`<Key>` bindings) for numpad support.
- [ ] Implement a decimal point (`.`) button for floating-point calculations.
- [ ] Refactor application logic from functional global variables into an Object-Oriented Class structure (`class CalculatorGUI`).
- [ ] Add backspace/delete button functionality to erase single characters.