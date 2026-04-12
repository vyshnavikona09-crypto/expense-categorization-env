from fastapi import FastAPI
from env.environment import ExpenseEnv
from env.models import Action

app = FastAPI()

def main():
    env = ExpenseEnv(difficulty="easy")

    obs = env.reset()
    done = False

    while not done:
        print(f"Transaction: {obs.transaction}, Amount: {obs.amount}")

        text = obs.transaction.lower()

        if "swiggy" in text or "zomato" in text or "grocery" in text:
            category = "Food"
        elif "uber" in text or "petrol" in text:
            category = "Transport"
        elif "bill" in text or "recharge" in text:
            category = "Bills"
        elif "amazon" in text or "flipkart" in text or "order" in text:
            category = "Shopping"
        else:
            category = "Other"

        action = Action(category=category)

        obs, reward, done, _ = env.step(action)

        print(f"Reward: {reward.value}, Reason: {reward.reason}")

    return "done"

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/run")
def run():
    return {"result": main()}

@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "transaction": obs.transaction,
        "amount": obs.amount
    }

if __name__ == "__main__":
    main()
