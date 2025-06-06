| rvm.py               | Recursive Validation Mode (RVM): contradiction detection and alignment  |

  from sentence_transformers import SentenceTransformer
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
