| emotion_net.py       | Valence-weighted coherence pressure module           |

 class EmotionNet:
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
