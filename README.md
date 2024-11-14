### **Efficient-N-Queens-GA**
An optimized implementation of the N-Queens problem using a Genetic Algorithm (GA) to find valid solutions for various board sizes efficiently.

---

### 📝 Table of Contents
- Features
- Prerequisites
- Usage
- Algorithm Overview
- Technical Implementation

---

### ✨ Features
- **Scalable Solution:** Supports customizable N×N board sizes.
- **Genetic Algorithm Optimization:**
  - Implements selection, crossover, and mutation techniques.
  - Prioritizes valid solutions with minimal computation.
- **Visual Output:** Displays the solved board in a clear and interactive format.
- **Efficient Execution:** Designed for performance, capable of handling larger board sizes effectively.

---

### 📋 Prerequisites
- Python 3.7 or higher
- NumPy
- Matplotlib (for visualization)

---

### 💻 Usage
Run the program to solve the N-Queens problem:
```bash
python n_queens_ga.py
```

Follow the prompts to:
1. Set the board size (e.g., `N = 8` for an 8x8 chessboard).
2. Choose Genetic Algorithm parameters (mutation rate, population size, etc.).

Output:
- Prints the solved board in a matrix format.
- Displays a graphical representation (if enabled).

---

### 🔧 Algorithm Overview
- **Selection:** Chooses the fittest individuals based on a fitness function that minimizes conflicts.
- **Crossover:** Combines parent solutions to produce offspring.
- **Mutation:** Introduces randomness to explore diverse solutions.
- **Fitness Evaluation:** Calculates the number of conflicts for each solution and prioritizes the least conflicting ones.

---

### 🔬 Technical Implementation
**Key Functions:**
- **Initialization:**
  ```python
  def initialize_population(size, n):
      return [random_permutation(n) for _ in range(size)]
  ```
- **Fitness Function:**
  Evaluates the number of queens attacking each other.
  ```python
  def calculate_fitness(board):
      # Counts row, column, and diagonal conflicts
  ```
- **Crossover and Mutation:**
  Introduces variety and combines solutions to find optimal configurations.
