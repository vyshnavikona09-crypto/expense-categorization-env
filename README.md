# Expense Categorization OpenEnv

## Overview
This environment simulates a real-world task where an agent categorizes financial transactions into categories such as Food, Transport, Bills, Shopping, and Other.

## Motivation
Expense tracking is a common real-world task used in finance apps. This environment allows training and evaluation of AI agents for automatic categorization.

## Observation Space
- transaction (string): description of expense
- amount (float): transaction amount
- step (int): current step in episode

## Action Space
- category (string): one of Food, Transport, Bills, Shopping, Other

## Tasks
- Easy: clear transactions
- Medium: moderately ambiguous
- Hard: highly ambiguous

## Reward System
- Correct: +1.0
- Partially correct: +0.5
- Wrong: -1.0

## Setup
```bash
pip install -r requirements.txt
python inference.py


## Example Interaction

[START] Running task: easy

[STEP] Transaction: Swiggy order ₹200 | Amount: 200
[STEP] AI chose: Food
[STEP] Reward: 1.0 | Reason: correct

[STEP] Transaction: Uber ride ₹150 | Amount: 150
[STEP] AI chose: Transport
[STEP] Reward: 1.0 | Reason: correct

[END] Final Score (0–1): 1.0


## Real-World Impact

Expense categorization is a core feature in many financial applications such as budgeting tools, banking apps, and personal finance trackers.

This environment simulates how users manually categorize transactions, enabling AI agents to learn and automate this process.

Potential applications include:
- Automatic expense tracking in finance apps
- Smart budgeting assistants
- Financial insights and analytics systems

By training agents in this environment, developers can build more intelligent and user-friendly financial tools.