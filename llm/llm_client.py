import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class LLMClient:

    _client = None

    @classmethod
    def get_client(cls):

        if cls._client is None:

            token = os.getenv(
                "HF_TOKEN"
            )

            if not token:

                raise ValueError(
                    "HF_TOKEN not found"
                )

            cls._client = OpenAI(
                base_url=(
                    "https://router.huggingface.co/v1"
                ),
                api_key=token
            )

        return cls._client

    @classmethod
    def generate(
        cls,
        prompt: str
    ):

        try:

            client = cls.get_client()

            completion = (
                client.chat.completions.create(
                    model=os.getenv(
                        "HF_MODEL"
                    ),
                    messages=[
                        {
                            "role": "system",
                            "content":
                            (
                                "Answer only using "
                                "the provided context. "
                                "If the answer is not "
                                "found, say "
                                "'I could not find the "
                                "answer in the knowledge "
                                "base.'"
                            )
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    max_tokens=300,
                    temperature=0.2
                )
            )

            return (
                completion
                .choices[0]
                .message
                .content
            )

        except Exception as e:

            return (
                f"LLM Error: {str(e)}"
            )