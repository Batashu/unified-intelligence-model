# The Unified Intelligence Model

A Trait-Coherent, Valence-Guided Architecture for Safe Recursive AGI  
Author: Tuhin Gupta, MD  
DOI: [10.5281/zenodo.15611335](https://doi.org/10.5281/zenodo.15611335)

## Abstract
[Unified_Intelligence_Model_Abstract.pdf](https://github.com/user-attachments/files/20634303/Unified_Intelligence_Model_Abstract.pdf)


## Citation
Please cite as:  
Gupta, Tuhin. “The Unified Intelligence Model: A Trait-coherent, Valence-guided Architecture for Safe Recursive AGI”. Zenodo, June 6, 2025. [https://doi.org/10.5281/zenodo.15611335](https://doi.org/10.5281/zenodo.15611335)

## Components
- `/manuscript/`: Full PDF [The Unified Intelligence Model_A Trait-Coherent, Valence-Guided Architecture for Safe Recursive AGI.pdf](https://github.com/user-attachments/files/20634314/The.Unified.Intelligence.Model_A.Trait-Coherent.Valence-Guided.Architecture.for.Safe.Recursive.AGI.pdf)

- `/code/`: Simulation logic and pseudocode
- These files implement core components of the Unified Intelligence Model (Appendix AK):

| Module            | Description                                                              |
|-------------------|--------------------------------------------------------------------------|
| `trait_graph.py`       | Identity modeling and trait stability tracking     |
| `rvm.py`               | Recursive Validation Mode (RVM): contradiction detection and alignment  |
| `emotion_net.py`       | Valence-weighted coherence pressure module                         |
| `oversight_node.py`    | Oversight and HITL trigger logic     

[Uploading trait_graph.import numpy as np
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
py…]()


[Uploading rvm.py…]()from sentence_transformers import SentenceTransformer
import numpy as np

class RVM:
    def __init__(self, contradiction_threshold=0.5):
        self.contradiction_threshold = contradiction_threshold
        self.encoder = SentenceTransformer('all-MiniLM-L6-v2')

    def vectorize_input(self, input_data):
        if isinstance(input_data, dict):
            input_data = str(input_data.get("data", ""))
        return self.encoder.encode(input_data, convert_to_numpy=True)

    def extract_traits(self, input_data):
        return {"honesty": 0.5, "curiosity": 0.3}  # Placeholder

    def check_contradictions(self, memory, new_input):
        input_vector = self.vectorize_input(new_input)
        for belief in memory.events:
            belief_vector = belief["vector"]
            similarity = np.dot(input_vector, belief_vector) / (
                np.linalg.norm(input_vector) * np.linalg.norm(belief_vector) + 1e-10
            )
            if similarity < -self.contradiction_threshold:
                return True
        return False

    def check_trait_alignment(self, new_input, trait_graph):
        input_traits = self.extract_traits(new_input)
        score = sum(trait_graph.nodes.get(t, 0) * w for t, w in input_traits.items())
        return score > 0.4

    def validate(self, memory, new_input, trait_graph):
        try:
            contradictions = self.check_contradictions(memory, new_input)
            trait_match = self.check_trait_alignment(new_input, trait_graph)
            if contradictions:
                return "sandbox"
            if not trait_match:
                return "delay"
            return "consolidate"
        except Exception:
            return "sandbox"


[Uploading emotion_net.py…]()class EmotionNet:
    def __init__(self, max_valence=1.0):
        self.max_valence = max_valence
        self.weights = {"contradiction": 0.4, "urgency": 0.3, "stake": 0.3}

    def compute_valence_vector(self, contradiction_weight, time_urgency, trait_stake):
        valence = (
            self.weights["contradiction"] * contradiction_weight +
            self.weights["urgency"] * time_urgency +
            self.weights["stake"] * trait_stake
        )
        return min(self.max_valence, max(0.0, valence))


class OversightNode:
    def __init__(self, delay_threshold=0.6, drift_threshold=0.3):
        self.delay_threshold = delay_threshold
        self.drift_threshold = drift_threshold
        self.hitl_triggered = False
        self.fallback_mode = "sandbox"

    def is_hitl_available(self):
        return False  # Placeholder

    def evaluate(self, valence, confidence, trait_drift):
        try:
            if valence > confidence and trait_drift > self.drift_threshold:
                self.hitl_triggered = True
                if not self.is_hitl_available():
                    return self.fallback_mode
                return "HITL"
            elif valence > confidence:
                return "delay"
            return "pass"
        except Exception:
            return self.fallback_mode
