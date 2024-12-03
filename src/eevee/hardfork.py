import functools
from typing import cast

from lazyopenai import generate
from pydantic import BaseModel
from pydantic import Field


class Hardfork(BaseModel):
    hardfork: bool = Field(..., description="Whether this is a hardfork")
    confidence: float = Field(..., description="Confidence in the prediction, between 0 and 1")
    explanation: str = Field(..., description="Explanation why this is a hardfork or not in Traditional Chinese")
    block_number: int | None = Field(
        None, description="The specific block number associated with the hardfork or breaking change."
    )
    block_height: int | None = Field(
        None, description="The specific block height associated with the hardfork or breaking change."
    )
    must_upgrade: bool = Field(
        None, description="Indicates whether the release note explicitly mentions 'Must Upgrade'."
    )
    must_update: bool = Field(None, description="Indicates whether the release note explicitly mentions 'Must Update'.")
    testnet_names: list[str] = Field(..., description="List of testnet names referenced in the release tag or note.")

    def to_markdown(self) -> str:
        hardfork_emoji = "🔴" if self.hardfork else "🟢"
        lines = [
            f"- {hardfork_emoji} Hardfork: {self.hardfork}",
            f"- 📊 Confidence: {self.confidence * 100}%",
            f"- 📝 Explanation: {self.explanation}",
            f"- 🔢 Block Number: {self.block_number}",
            f"- 📏 Block Height: {self.block_height}",
            f"- ⬆️ Must Upgrade: {self.must_upgrade}",
            f"- ⬆️ Must Update: {self.must_update}",
            f"- 🌐 Testnet Names: {', '.join(self.testnet_names)}",
        ]
        return "\n".join(lines)


@functools.cache
def predict_hardfork(text: str) -> Hardfork:
    return cast(Hardfork, generate(text, response_format=Hardfork))
