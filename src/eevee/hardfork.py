import functools
from typing import cast

from lazyopenai import generate
from pydantic import BaseModel
from pydantic import Field


class Hardfork(BaseModel):
    hardfork: bool = Field(..., description="Whether this is a hardfork")
    confidence: float = Field(..., description="Confidence in the prediction, between 0 and 1")
    explanation: str = Field(..., description="Explanation why this is a hardfork or not in Traditional Chinese")

    def to_markdown(self) -> str:
        hardfork_emoji = "🔴" if self.hardfork else "🟢"
        lines = [
            f"- {hardfork_emoji} Hardfork: {self.hardfork}",
            f"- 📊 Confidence: {self.confidence * 100}%",
            f"- 📝 Explanation: {self.explanation}",
        ]
        return "\n".join(lines)


@functools.cache
def predict_hardfork(text: str) -> Hardfork:
    return cast(Hardfork, generate(text, response_format=Hardfork))
