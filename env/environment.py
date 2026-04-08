from env.models import Observation, Action, Reward
from env.tasks import TASKS

class ExpenseEnv:
    def __init__(self, difficulty="easy"):
        self.tasks = TASKS[difficulty]
        self.current_step = 0
        self.total_steps = len(self.tasks)

    def reset(self):
        self.current_step = 0
        task = self.tasks[self.current_step]

        return Observation(
            transaction=task["text"],
            amount=task["amount"],
            step=self.current_step
        )

    def step(self, action: Action):
        task = self.tasks[self.current_step]
        correct = task["label"]

        # reward logic
        SIMILAR = {
            "Food": ["Shopping"],
            "Shopping": ["Food"],
            "Bills": ["Other"],
            "Transport": ["Other"],
        }

        user_cat = action.category.strip().lower()
        correct_cat = correct.lower()

        if user_cat == correct_cat:
            reward_value = 1.0
            reason = "correct"

        elif correct in SIMILAR and action.category.capitalize() in SIMILAR[correct]:
            reward_value = 0.5
            reason = "partially correct"

        else:
            reward_value = -1.0
            reason = f"wrong (expected {correct})"
        
        # --- move to next step ---
        self.current_step += 1
        done = self.current_step >= self.total_steps

        if not done:
            next_task = self.tasks[self.current_step]
            observation = Observation(
                transaction=next_task["text"],
                amount=next_task["amount"],
                step=self.current_step
            )
        else:
            observation = None

        return observation, Reward(value=reward_value, reason=reason), done, {}
    
    def state(self):
        return {
            "current_step": self.current_step,
            "total_steps": self.total_steps
        }
