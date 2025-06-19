import random
import time
import math
import ox
 
class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state  # ox.Board instance
        self.parent = parent
        self.action = action
        self.children = []
        self.visits = 0
        self.value = 0.0
        self.untried_actions = list(state.get_actions())
 
    def ucb_score(self, c=1.4):
        if self.visits == 0:
            return float('inf')
        return self.value / self.visits + c * math.sqrt(math.log(self.parent.visits) / self.visits)
 
    def best_child(self, c=1.4):
        return max(self.children, key=lambda child: child.ucb_score(c))
 
    def expand(self):
        action = self.untried_actions.pop()
        next_state = self.state.clone()
        next_state.apply_action(action)
        child_node = Node(next_state, parent=self, action=action)
        self.children.append(child_node)
        return child_node
 
    def is_fully_expanded(self):
        return len(self.untried_actions) == 0
 
    def is_terminal(self):
        return self.state.is_terminal()
 
    def rollout_policy(self, actions):
        return random.choice(list(actions))
 
    def rollout(self):
        current_state = self.state.clone()
        while not current_state.is_terminal():
            action = self.rollout_policy(current_state.get_actions())
            current_state.apply_action(action)
        return current_state.get_rewards()
 
    def backpropagate(self, reward, player_id):
        self.visits += 1
        self.value += reward[player_id]  # reward[0] if bot is x, reward[1] if bot is o
        if self.parent:
            self.parent.backpropagate(reward, player_id)
 
class MCTSBot:
    def __init__(self, play_as: int, time_limit: float):
        self.play_as = play_as
        self.time_limit = time_limit * 0.9
 
    def play_action(self, board):
        root = Node(board.clone())
        start_time = time.time()
 
        while time.time() - start_time < self.time_limit:
            node = root
 
            # Selection
            while not node.is_terminal() and node.is_fully_expanded():
                node = node.best_child()
 
            # Expansion
            if not node.is_terminal() and not node.is_fully_expanded():
                node = node.expand()
 
            # Simulation
            result = node.rollout()
 
            # Backpropagation
            node.backpropagate(result, self.play_as)
 
        # Return the best action based on most visits
        best = max(root.children, key=lambda child: child.visits)
        return best.action
