# test_hf.py

from llm.llm_client import (
    LLMClient
)

response = (
    LLMClient.generate(
        "What is the capital of France?"
    )
)

print(response)