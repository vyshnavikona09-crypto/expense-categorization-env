from pydantic import BaseModel, Field
from typing import Optional, Literal


# Observation
class Observation(BaseModel):
    transaction: str = Field(..., description="Transaction description text")
    amount: float = Field(..., description="Transaction amount in INR")
    step: int = Field(..., description="Current step in the episode")


# Action
class Action(BaseModel):
    category: Literal["Food", "Transport", "Bills", "Shopping", "Other"] = Field(
        ..., description="Predicted category for the transaction"
    )


# Reward
class Reward(BaseModel):
    value: float = Field(..., description="Reward score between -1 and 1")
    reason: Optional[str] = Field(None, description="Reason for the reward")
