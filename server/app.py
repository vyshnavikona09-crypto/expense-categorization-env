from fastapi import FastAPI
from env.environment import ExpenseEnv
from env.models import Action

app = FastAPI()

env = ExpenseEnv(difficulty="easy")


@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "transaction": obs.transaction,
        "amount": obs.amount,
        "step": obs.step
    }


@app.post("/step")
def step(action: dict):
    act = Action(category=action["category"])
    obs, reward, done, info = env.step(act)

    if obs is None:
        return {
            "transaction": None,
            "amount": None,
            "step": None,
            "reward": reward.value,
            "reason": reward.reason,
            "done": done
        }

    return {
        "transaction": obs.transaction,
        "amount": obs.amount,
        "step": obs.step,
        "reward": reward.value,
        "reason": reward.reason,
        "done": done
    }


@app.get("/state")
def state():
    return env.state()
