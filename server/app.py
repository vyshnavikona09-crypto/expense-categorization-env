from fastapi import FastAPI
from env.environment import ExpenseEnv
from env.models import Action

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

env = ExpenseEnv(difficulty="easy")


@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "transaction": obs.transaction,
        "amount": obs.amount
    }


@app.post("/step")
def step(action: dict):
    act = Action(category=action["category"])
    obs, reward, done, _ = env.step(act)

    if obs is None:
        return {
            "transaction": None,
            "amount": None,
            "reward": reward.value,
            "done": done
        }

    return {
        "transaction": obs.transaction,
        "amount": obs.amount,
        "reward": reward.value,
        "done": done
    }


@app.get("/state")
def state():
    return env.state()
