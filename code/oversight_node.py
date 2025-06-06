| `/code/oversight_node.py`                       | Oversight logic and HITL trigger enforcement                       |

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
