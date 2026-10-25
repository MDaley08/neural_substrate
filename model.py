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

    def predict(self,cue_onsets,t):
        v = 0.0
        for cue_name, onset in cue_onsets.items():
            self._ensure_cue(cue_name)
            x = self._c(cue_name, onset,t)
            v += self.weights[cue_name] @ x
        return v
    def run_trial(self, cue_onsets, reward_time, trial_len, reward_value=1.0,
                  omit_reward=False, learn=True):
        for cue_name in cue_onsets:
            self._ensure_cue(cue_name)

        delta_trace = np.zeros(trial_len)
        v_trace = np.zeros(trial_len)

        for t in range(trial_len):
            r_t = reward_value if (t == reward_time and not omit_reward) else 0.0

            v_t = self.predict(cue_onsets, t)
            v_tp1 = self.predict(cue_onsets, t + 1) if t + 1 < trial_len else 0.0
            delta = r_t + self.gamma * v_tp1 - v_t

            delta_trace[t] = delta
            v_trace[t] = v_t

            if learn:
                for cue_name, onset in cue_onsets.items():
                    x = self._x(onset,t)
                    self.weights[cue_name] += self.alpha * x * delta
        return delta, v_trace

    def weight_strength(self, cue_name):
        return float(np.sum(self.weights.get(cue_name,0.0)))




    