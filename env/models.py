from pydantic import BaseModel
from typing import Optional

# Observation (what agent sees)
class Observation(BaseModel):
    transaction: str
    amount: float
    step: int

# Action (what agent does)
class Action(BaseModel):
    category: str  # Food, Transport, Bills, Shopping, Other

# Reward
class Reward(BaseModel):
    value: float
    reason: Optional[str] = None
