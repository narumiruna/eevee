import functools
from typing import cast

from lazyopenai import generate
from pydantic import BaseModel
from pydantic import Field


class Hardfork(BaseModel):
    hardfork: bool = Field(..., description="Indicates if this is a hardfork.")
    confidence: float = Field(..., description="Confidence in the hardfork prediction, between 0 and 1.")
    explanation: str = Field(..., description="Explanation of why this is a hardfork or not, in Traditional Chinese.")
    block_number: int | None = Field(
        None, description="The specific block number associated with the hardfork or breaking change."
    )
    must_upgrade: bool = Field(
        ..., description="Indicates if the release note explicitly mentions 'Must Upgrade' or 'Must Update'."
    )
    testnet_names: list[str] = Field(..., description="List of testnet names referenced in the release tag or note.")
    upgrade_deadline: str | None = Field(
        None, description="The specific date and time by which the upgrade must be completed (ISO8601 format)."
    )
    breaking_change: bool = Field(..., description="Indicates if this is a breaking change.")
    impact_score: float = Field(..., description="Indicates the impact score of the change, from 0 to 1.")

    def to_markdown(self) -> str:
        hardfork_emoji = "🔴" if self.hardfork else "🟢"
        lines = [
            f"- {hardfork_emoji} Hardfork: {self.hardfork}",
            f"- 📊 Confidence: {self.confidence * 100}%",
            f"- 📝 Explanation: {self.explanation}",
            f"- 🔢 Block Number: {self.block_number}",
            f"- ⬆️ Must Upgrade: {self.must_upgrade}",
            f"- 🌐 Testnet Names: {', '.join(self.testnet_names)}",
            f"- 📅 Upgrade Deadline: {self.upgrade_deadline}",
            f"- ⚠️ Breaking Change: {self.breaking_change}",
            f"- 💥 Impact Score: {self.impact_score * 100}%",
        ]
        return "\n".join(lines)

    def to_slack(self) -> str:
        hardfork_emoji = "🔴" if self.hardfork else "🟢"
        lines = [
            f"- {hardfork_emoji} *Hardfork*: {self.hardfork}",
            f"- 📊 *Confidence*: {self.confidence * 100}%",
            f"- 📝 *Explanation*: {self.explanation}",
            f"- 🔢 *Block Number*: {self.block_number}",
            f"- ⬆️ *Must Upgrade*: {self.must_upgrade}",
            f"- 🌐 *Testnet Names*: {', '.join(self.testnet_names)}",
            f"- 📅 *Upgrade Deadline*: {self.upgrade_deadline}",
        ]
        return "\n".join(lines)


@functools.cache
def predict_hardfork(text: str) -> Hardfork:
    return cast(Hardfork, generate(text, response_format=Hardfork))
