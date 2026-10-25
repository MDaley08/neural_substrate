class ClassicalConditioning:
    """
     A simulated Pavlovian classical conditioning environment
    """
    def __init__(self, n_steps:int, reward_magnitude:float, reward_time:int):
        """
        Parameters:
        - n_steps : int
            total number of discrete time steps in a single trial
        -n
        - 
        """
        # Task variables
        self.n_steps = n_steps
        self.n_actions = 0
        self.cs_time = int(n_steps/4) -1 #conditioned stimulus time, tends to be Q1 of time step

        # Reward variables
        self.reward_state = [0,0]
        self.reward_magnitude = None
        self.reward_probability = None
        self.reward_time = None

        # Time step at which the conditioned stimulus is presented
        self.set_reward(reward_magnitude, reward_time)

        # Create a state dictionary
        self.state_dict = self._create_state_dict()

    def set_reward(self, reward_magniture, reward_time):
        '''
        Determine reward state and magnitude of reward
        '''
        if reward_time >= self.n_steps - self.cs_time:
            self.reward_magnitude = 0
        else:
            self.reward_magnitude = self.reward_magnitude
            self.reward_state = [1,reward_time]

    def get_outcome(self, current_state):
        '''
        Determine next state and reward
        '''
        #update state
        next_state = 0
        if current_state < self.n_steps - 1:
            next_state = current_state + 1

        #check for reward
        if self.reward_state == self.state_dict[current_state]

    def _create_state_dict(self):
        state_dict = {}
        delay = 0

        for s in range(self.n_steps):
            if s <= self.cs_time:
                state_dict[s] = [0,0]
            else:
                delay += 1 #time in delay
                state_dict[s] = [1,delay]
        return state_dict