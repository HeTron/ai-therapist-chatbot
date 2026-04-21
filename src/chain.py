import os
from typing import Generator
import anthropic


def load_therapist_prompt() -> str:
    prompt_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "therapist.txt")
    with open(prompt_path, "r") as f:
        return f.read()


class TherapistChain:
    """Manages conversation history and streams responses via the Anthropic API."""

    MODEL = "claude-haiku-4-5"

    def __init__(self):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise EnvironmentError(
                "ANTHROPIC_API_KEY is not set. Add it to your .env file or Streamlit secrets."
            )
        self.client = anthropic.Anthropic(api_key=api_key)
        self.system_prompt = load_therapist_prompt()
        self.messages: list[dict] = []

    def stream_response(self, user_input: str) -> Generator[str, None, None]:
        """Stream Sage's response token by token, updating message history."""
        self.messages.append({"role": "user", "content": user_input})

        full_response = ""
        with self.client.messages.stream(
            model=self.MODEL,
            max_tokens=1024,
            system=[
                {
                    "type": "text",
                    "text": self.system_prompt,
                    "cache_control": {"type": "ephemeral"},
                }
            ],
            messages=self.messages,
        ) as stream:
            for text in stream.text_stream:
                full_response += text
                yield text

        self.messages.append({"role": "assistant", "content": full_response})


def create_chain() -> TherapistChain:
    return TherapistChain()
