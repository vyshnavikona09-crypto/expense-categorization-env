import os
from openai import OpenAI

from env.environment import ExpenseEnv
from env.models import Action
from env.grader import grade

# Initialize OpenAI client (with required env variables)
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("API_BASE_URL", "https://api.openai.com/v1")
)

MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")


def get_ai_action(transaction_text):
    prompt = f"""
Classify the following expense into one of these categories:
Food, Transport, Bills, Shopping, Other

Transaction: {transaction_text}

Return ONLY the category name.
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        category = response.choices[0].message.content.strip()
        
        # Clean output (just in case model returns extra text)
        category = category.split()[0]
        return category

    except Exception as e:
        print(f"[STEP] API error: {e}")
        print("[STEP] Using fallback logic...")

        # Fallback rule-based system
        text = transaction_text.lower()

        if "swiggy" in text or "zomato" in text or "grocery" in text:
            return "Food"
        elif "uber" in text or "petrol" in text:
            return "Transport"
        elif "bill" in text or "recharge" in text:
            return "Bills"
        elif "amazon" in text or "flipkart" in text or "order" in text:
            return "Shopping"
        else:
            return "Other"


def run_environment(difficulty="easy"):
    env = ExpenseEnv(difficulty=difficulty)

    obs = env.reset()
    done = False
    results = []

    print(f"\n[START] Running task: {difficulty}\n")

    while not done:
        print(f"[STEP] Transaction: {obs.transaction} | Amount: {obs.amount}")

        # AI decides action
        ai_category = get_ai_action(obs.transaction)
        print(f"[STEP] AI chose: {ai_category}")

        action = Action(category=ai_category)

        obs, reward, done, _ = env.step(action)

        print(f"[STEP] Reward: {reward.value} | Reason: {reward.reason}\n")

        results.append(reward.reason)

    score = grade(results)

    print(f"[END] Final Score (0–1): {score}\n")

    return score


if __name__ == "__main__":
    total_score = 0

    for level in ["easy", "medium", "hard"]:
        score = run_environment(difficulty=level)
        total_score += score

    avg_score = total_score / 3
    print(f"Overall Average Score: {avg_score}")