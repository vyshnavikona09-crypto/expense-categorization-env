import os
from openai import OpenAI

from env.environment import ExpenseEnv
from env.models import Action
from env.grader import grade

# Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    client = OpenAI(
        api_key=api_key,
        base_url=os.getenv("API_BASE_URL", "https://api.openai.com/v1")
    )
else:
    client = None

MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")


def normalize_category(text):
    text = text.strip().lower()

    if "food" in text:
        return "Food"
    elif "transport" in text:
        return "Transport"
    elif "bill" in text:
        return "Bills"
    elif "shop" in text:
        return "Shopping"
    else:
        return "Other"


def fallback_logic(transaction_text):
    text = transaction_text.lower()

    if any(x in text for x in ["swiggy", "zomato", "restaurant", "food", "snack"]):
        return "Food"

    if any(x in text for x in ["uber", "ola", "petrol", "fuel", "ride"]):
        return "Transport"

    if any(x in text for x in ["electricity", "bill", "recharge", "subscription", "netflix"]):
        return "Bills"

    if any(x in text for x in ["amazon", "flipkart", "purchase", "order", "item"]):
        return "Shopping"

    return "Other"


def get_ai_action(transaction_text):

    # Fallback mode
    if client is None:
        return fallback_logic(transaction_text)

    prompt = f"""
Classify the following expense into one of these categories:
Food, Transport, Bills, Shopping, Other
Transaction: {transaction_text}
Return ONLY one word from the list.
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        raw_output = response.choices[0].message.content.strip()
        return normalize_category(raw_output)

    except Exception:
        return fallback_logic(transaction_text)


def run_environment(difficulty="easy"):
    env = ExpenseEnv(difficulty=difficulty)

    obs = env.reset()
    done = False
    results = []

    print(f"[START] Running task: {difficulty}")

    while not done:
        print(f"[STEP] Transaction: {obs.transaction} | Amount: {obs.amount}")

        ai_category = get_ai_action(obs.transaction)

        action = Action(category=ai_category)

        obs, reward, done, _ = env.step(action)

        print(f"[STEP] Reward: {reward.value} | Reason: {reward.reason}")

        results.append(reward.reason)

    score = grade(results)

    print(f"[END] Final Score: {score}")

    return score


if __name__ == "__main__":
    total_score = 0

    for level in ["easy", "medium", "hard"]:
        score = run_environment(difficulty=level)
        total_score += score

    avg_score = total_score / 3
    print(f"[END] Overall Average Score: {avg_score}")
