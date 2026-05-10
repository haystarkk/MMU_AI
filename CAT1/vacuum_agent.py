import random

class VacuumEnvironment:
    def __init__(self, dirty_prob=0.5):
        self.status = {'A': 'dirty' if random.random() < dirty_prob else 'clean',
                       'B': 'dirty' if random.random() < dirty_prob else 'clean'}
        self.agent_location = random.choice(['A', 'B'])

    def perceive(self):
        return (self.agent_location, self.status[self.agent_location])

    def act(self, action):
        if action == 'clean':
            self.status[self.agent_location] = 'clean'
        elif action == 'left' and self.agent_location == 'B':
            self.agent_location = 'A'
        elif action == 'right' and self.agent_location == 'A':
            self.agent_location = 'B'

    def is_clean_all(self):
        return all(s == 'clean' for s in self.status.values())

class VacuumAgent:
    def decide_action(self, percept):
        location, state = percept
        if state == 'dirty':
            return 'clean'
        else:
            return 'left' if location == 'B' else 'right'

def run_agent(env, agent, max_steps=100):
    for step in range(max_steps):
        percept = env.perceive()
        action = agent.decide_action(percept)
        env.act(action)
        print(f"Step {step+1}: Agent at {env.agent_location}, Action: {action}, Status: {env.status}")
        if env.is_clean_all():
            print(f"All clean after {step+1} steps!")
            return True
    print("Max steps reached without cleaning all.")
    return False

if __name__ == "__main__":
    env = VacuumEnvironment(dirty_prob=0.7)
    agent = VacuumAgent()
    print("Initial status:", env.status)
    run_agent(env, agent)