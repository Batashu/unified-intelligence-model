# The Unified Intelligence Model

A Trait-Coherent, Valence-Guided Architecture for Safe Recursive AGI  
**Author**: Tuhin Gupta, MD  
**DOI**: [10.5281/zenodo.15611335](https://doi.org/10.5281/zenodo.15611335)

---

## 📄 Abstract  
📎 [Unified_Intelligence_Model_Abstract.pdf](./Unified_Intelligence_Model_Abstract.pdf)

---

## 📘 Citation

> Gupta, Tuhin. “The Unified Intelligence Model: A Trait-coherent, Valence-guided Architecture for Safe Recursive AGI”. *Zenodo*, June 6, 2025. [https://doi.org/10.5281/zenodo.15611335](https://doi.org/10.5281/zenodo.15611335)

---

## 🧠 Repository Structure

| Folder / File                                     | Description                                               |
|---------------------------------------------------|-----------------------------------------------------------|
| `/manuscript/Unified_Intelligence_Model.pdf`      | Full paper PDF                                            |
| `/code/trait_graph.py`                            | Identity modeling and trait stability tracking            |
| `/code/rvm.py`                                    | Recursive Validation Mode (RVM): contradiction logic      |
| `/code/emotion_net.py`                            | Valence-weighted coherence pressure module                |
| `/code/oversight_node.py`                         | Oversight logic, delay wrappers, HITL triggers            |

---

## 🧪 Example: TraitGraph Module (from Appendix AK)

```python
from trait_graph import TraitGraph

tg = TraitGraph()
tg.update_weight("curiosity", 0.05)
print(tg.central_attractor())
