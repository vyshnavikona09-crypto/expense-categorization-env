# Expense Categorization OpenEnv Environment

## Overview
This project implements a real-world OpenEnv environment for expense categorization, where an AI agent classifies financial transactions into categories such as Food, Transport, Bills, Shopping, and Other.

The environment follows the OpenEnv specification with structured Observation, Action, and Reward models, along with step(), reset(), and state() APIs.

---

## Motivation
Expense categorization is a fundamental feature in modern financial applications such as banking apps, budgeting tools, and expense trackers.

This environment simulates how users interpret and categorize transactions, enabling AI agents to learn and automate this process efficiently.

---

## Real-World Impact
This environment can be used to train agents for:

- Automated expense tracking systems  
- Smart financial assistants  
- Budget analysis and insights  
- Transaction classification in banking apps  

It provides a realistic simulation of how financial data is processed in real-world systems.

---

## Environment Design

### Observation Space
- `transaction` (str): description of the expense  
- `amount` (float): transaction value  
- `step` (int): current step in episode  

---

### Action Space
- `category` (str): one of  
  `Food, Transport, Bills, Shopping, Other`

---

### API Endpoints
- `POST /reset` → Initialize environment  
- `POST /step` → Perform action  
- `GET /state` → Retrieve current state  

---

## Task Design

The environment includes three difficulty levels:

### Easy
- Clear and unambiguous transactions  
- Example: “Uber ride to office”  

### Medium
- Slight ambiguity (e.g., platform-based purchases)  
- Example: “Amazon purchase - headphones”  

### Hard
- Highly ambiguous transactions requiring contextual reasoning  
- Example: “Google Play recharge for game purchase”  

This progression ensures increasing complexity and realistic agent evaluation.

---

## Reward Design

The reward system provides continuous feedback:

- **+1.0** → Correct classification  
- **+0.5** → Partially correct (similar category)  
- **-1.0** → Incorrect classification  

This allows agents to learn progressively instead of relying on binary success signals.

---

## Baseline Agent

The provided inference script uses:

- OpenAI API (if available)  
- Rule-based fallback logic (ensures reproducibility)  

This guarantees consistent baseline performance even without external dependencies.

---

## Setup

```bash
pip install -r requirements.txt
python inference.py
