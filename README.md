# MCTS Tic-Tac-Toe Bot 🎮🤖

This project implements an AI bot for Tic-Tac-Toe using the **Monte Carlo Tree Search (MCTS)** algorithm. It was developed as part of a university assignment to demonstrate proficiency in Python, game logic design, and AI decision-making techniques.

## 🧠 What It Does

The bot intelligently plays the classic **"Noughts and Crosses"** *(Tic-Tac-Toe)* game by:

- Simulating thousands of game outcomes within a time constraint
- Building and traversing a decision tree
- Making moves based on exploration vs. exploitation (UCB1)
- Learning from rollouts and backpropagating results

## 💻 Technologies

- **Python 3**
- Object-Oriented Design (custom `Node` and `MCTSBot` classes)
- Algorithms: Monte Carlo Tree Search (Selection, Expansion, Simulation, Backpropagation)
- Lightweight integration with a basic game engine (`ox.py`)

## 📁 Files

- `student.py`: Core MCTS logic (this is the main code I wrote)
- `ox.py`: Simple game engine for Tic-Tac-Toe
- `README.md`: Project description

## 🧪 How to Run

```bash
python3 ox.py
```
This will launch the game and pit the MCTSBot against another bot or player (depending on configuration in ox.py).

## ✨ Skills Demonstrated
- Clean and maintainable Python code
- Understanding of AI and decision trees
- Performance optimization under time constraints
- Familiarity with simulations and rollout strategies

## 🔧 Future Ideas
- Extend to larger boards (e.g., 4x4 or 5x5)
- Improve rollout policy for smarter simulations
- Add a GUI to visualize the bot’s decisions


## 👤 Author
Made with ❤️ as part of my studies in open informatics.  
*Always looking for ways to make games smarter and more fun.*  

🚀 Created by Aleksandra Kenig (aka [yourpunk](https://github.com/yourpunk)). 

💌 Wanna collab or throw some feedback? You know where to find me.
