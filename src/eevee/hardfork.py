import functools
from typing import Literal
from typing import cast

from lazyopenai import generate
from pydantic import BaseModel
from pydantic import Field


class ThoughtStep(BaseModel):
    context: str = Field(..., description="The specific context or condition being evaluated in this step.")
    reasoning: str = Field(..., description="Explanation of the reasoning process at this step.")
    conclusion: str = Field(..., description="Intermediate conclusion reached at this step.")


class ChainOfThought(BaseModel):
    steps: list[ThoughtStep] = Field(..., description="A list of reasoning steps leading to the final conclusion.")
    final_conclusion: str = Field(..., description="The final conclusion reached after all reasoning steps.")


class HardforkAnalysis(BaseModel):
    chain_of_thought: ChainOfThought = Field(
        ..., description="The chain of thought leading to the hardfork analysis."
    )
    hardfork: Literal["yes", "no", "unknown"] = Field(..., description="Indicates if this is a hardfork.")
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

    @property
    def hardfork_emoji(self) -> str:
        match self.hardfork:
            case "yes":
                return "🔴"
            case "no":
                return "🟢"
            case "unknown":
                return "🟡"
            case _:
                raise ValueError(f"Invalid hardfork value: {self.hardfork}")

    def to_markdown(self) -> str:
        lines = [
            f"- {self.hardfork_emoji} Hardfork: {self.hardfork}",
            f"- 📊 Confidence: {self.confidence * 100}%",
            f"- 📝 Explanation: {self.explanation}",
            f"- 🔢 Block Number: {self.block_number}",
            f"- ⬆️ Must Upgrade: {self.must_upgrade}",
            f"- 🌐 Testnet Names: {', '.join(self.testnet_names)}",
            f"- 📅 Upgrade Deadline: {self.upgrade_deadline}",
        ]
        return "\n".join(lines)

    def to_slack(self) -> str:
        lines = [
            f"- {self.hardfork_emoji} *Hardfork*: {self.hardfork}",
            f"- 📊 *Confidence*: {self.confidence * 100}%",
            f"- 📝 *Explanation*: {self.explanation}",
        ]

        if self.block_number is not None:
            lines += [f"- 🔢 *Block Number*: {self.block_number}"]

        lines += [f"- ⬆️ *Must Upgrade*: {self.must_upgrade}"]

        if self.testnet_names:
            lines += [f"- 🌐 *Testnet Names*: {', '.join(self.testnet_names)}"]

        if self.upgrade_deadline is not None:
            lines += [f"- 📅 *Upgrade Deadline*: {self.upgrade_deadline}"]

        return "\n".join(lines)


@functools.cache
def predict_hardfork(text: str) -> HardforkAnalysis:
    return cast(HardforkAnalysis, generate(text, response_format=HardforkAnalysis))
