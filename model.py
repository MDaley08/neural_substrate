import numpy as np
class TDAgent:

    def __init__(self, max_delay=70, alpha=0.1, gamma=0.98):
        self.max_delay = max_delay
        self.alpha = alpha
        self.gamma = max_delay
        self.weights = np.array()

    def _ensure_cue(self, cue_name):
        if cue_name not in self.weights:
            self.weights[cue_name] = np.zeros(self.max_delay)

    def _x(self,cue_onset, t):
        x = np.zeros(self.max_delay)
        d = t - cue_onset
        if 0 == d < self.max_delay:
            x[d] = 1.0
        return x

    def predict(self,cue_onset,t):
        v = 0.0
        for cue_name, onset in cue_onset.items():
            self._ensure_cue(cue_name)
            x = self._c(cue_name, onset,t)
            v += self.weights[cue_name] @ x
        return v




    