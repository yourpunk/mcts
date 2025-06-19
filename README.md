# 🧠 MCTS Tic-Tac-Toe Bot 🎮

An AI-powered agent that plays Tic-Tac-Toe using **Monte Carlo Tree Search** (MCTS) — simulating thousands of possible game outcomes to make informed decisions.

Unlike rule-based or brute-force bots, this one *thinks probabilistically*, learns from simulated experience, and adapts its decisions dynamically based on rollout outcomes.

---

## 🤖 What It Actually Does

The MCTSBot competes in Tic-Tac-Toe by:

- Exploring the game tree through **random simulations**
- Selecting moves using the **UCB1 algorithm**
- Updating win probabilities through **backpropagation**
- Making near-optimal choices under a time constraint

MCTS isn't overkill here — it's a fun testbed to visualize **intelligent behavior emerging from random simulations**.

---

## 🧠 Key Highlights

- 📂 Core logic lives in `mcts.py` — cleanly structured with `Node` and `MCTSBot` classes
- ⏱ Supports dynamic time budgeting per move (e.g., "think for 100ms")
- 📊 Real-time learning: bot improves mid-game as tree builds up
- 🧪 Comes with test functions & debugging tools to validate behavior

---

## 📦 Project Layout

```text
tictactoe-mcts/
├── mcts.py     # ⭐ My work: MCTS logic, selection, backprop
├── ox.py       # Game loop & simple UI engine
└── README.md
```

---

## 🚀 Run It

```bash
python3 ox.py
```
You can configure player types (e.g., bot vs. bot, or bot vs. human) in ox.py.
The MCTSBot will simulate hundreds of games per move — and win more often than not.

--- 

## 🛠 Tech Stack

- **Language**: Python 3
- **Core Concepts**:
  - Monte Carlo Tree Search
  - Upper Confidence Bound (UCB1)
  - Tree traversal and rollout-based learning
- **Design**: OOP (agent-based), game engine abstraction

---

## 💡 What I Explored

This project taught me to:
- Structure a state-action tree from scratch
- Balance randomness with deterministic planning
- Debug AI behavior when outcomes are probabilistic
Make trade-offs between computation time and move quality

---

## 🌱 Next Steps

-Extend to 4x4 boards with pruning
- Add graphical interface (pygame or tkinter)
- Train rollout policy on human-style mistakes
- Record bot vs. human sessions for behavior analysis

---

## 📜 License

MIT. Use it, break it, rewrite it — just don’t turn it in as your own assignment.

--- 

## 👤 Author
🦾 Crafted by Aleksandra Kenig (aka [yourpunk](https://github.com/yourpunk)).<br>
> "Make simple games — teach them to think."
