import functools

from lazyopenai import generate
from pydantic import BaseModel
from pydantic import Field


class Hardfork(BaseModel):
    hardfork: bool = Field(..., description="Whether this is a hardfork")
    confidence: float = Field(..., description="Confidence in the prediction, between 0 and 1")
    explanation: str = Field(..., description="Explanation why this is a hardfork or not in Traditional Chinese")

    def __str__(self) -> str:
        hardfork_emoji = "🔴" if self.hardfork else "🟢"
        return (
            f"\n{hardfork_emoji} Hardfork: {self.hardfork}\n"
            f"📊 Confidence: {self.confidence * 100:.1f}%\n"
            f"📝 Explanation:\n{self.explanation}\n"
        )


@functools.cache
def predict_hardfork(text: str) -> Hardfork:
    return generate(text, response_format=Hardfork)
