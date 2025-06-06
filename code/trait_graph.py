- /code/: Simulation logic and pseudocode
- These files implement core components of the Unified Intelligence Model (Appendix AK):

| Module            | Description                                                              |
|-------------------|--------------------------------------------------------------------------|
| trait_graph.py       | Identity modeling and trait stability tracking     |

import numpy as np
from collections import defaultdict

class TraitGraph:
    def __init__(self, initial_traits=None):
        self.nodes = initial_traits or {"honesty": 0.82, "curiosity": 0.71, "empathy": 0.65}
        self.edges = defaultdict(dict)
        self.damping_factor = 0.1
        self.weight_history = {trait: [w] for trait, w in self.nodes.items()}
        self.max_history = 100

    def update_weight(self, trait, delta):
        if trait not in self.nodes:
            raise ValueError(f"Trait {trait} not found in graph")
        current = self.nodes[trait]
        new_weight = current + self.damping_factor * delta
        self.nodes[trait] = max(0.0, min(1.0, new_weight))
        self.weight_history[trait].append(self.nodes[trait])
        if len(self.weight_history[trait]) > self.max_history:
            self.weight_history[trait].pop(0)
        return self.nodes[trait]

    def detect_entropy_spike(self, window=10):
        entropy = 0.0
        for trait, history in self.weight_history.items():
            recent = history[-min(window, len(history)):] or [0.5]
            probs = np.array(recent) / (sum(recent) + 1e-10)
            entropy += -sum(p * np.log2(p + 1e-10) for p in probs if p > 0)
        return entropy > 2.0

    def central_attractor(self):
        return max(self.nodes.items(), key=lambda x: x[1])[0]

    def central_attractor_score(self, input_data):
        return np.random.uniform(0, 1)  # Placeholder
