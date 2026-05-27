from ollama import Message, chat


def addition(a: float, b: float) -> float:
    """Returns the sum of two numbers."""

    return a + b


def multiplication(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b


OUTILS = {
    "addition": addition,
    "multiplication": multiplication
}

TOOL_LIST = [addition, multiplication]


def call_model(messages: list[dict]) -> Message:
    """Calls the model with the given messages and returns the response."""
    response = chat(
        model="llama3.1:8b",
        messages=messages,
        tools=TOOL_LIST,
        stream=False,
    )
    return response.message


def loop(question: str, max_tours: int = 6) -> tuple[str, list[str]]:
    """
        Fait tourner la boucle Reason -> Act -> Observe jusqu'à ce que le modèle donne une réponse finale ou que le nombre maximum de tours soit atteint.
    """

    _memory = [
        {
            "role": "system",
            "content": "You are a helpful assistant that can perform basic arithmetic operations. You can use the following tools: addition(a, b) and multiplication(a, b)."
        },
        {
            "role": "user",
            "content": question
        }
    ]

    trace = []

    for _ in range(max_tours):
        response = call_model(_memory)
        _memory.append(response.model_dump(exclude_none=True))

        tool_calls = response.tool_calls
        if not tool_calls:
            # If there are no tool calls, we assume the model has given a final answer
            return response.content or "", trace

        for call in tool_calls:
            tool_name = call.function.name  # voir documentation ollama
            args = call.function.arguments

            result = OUTILS[tool_name](**args)
            trace.append(
                f"Tool call: {tool_name} with arguments {args} returned {result}"
            )
            _memory.append(
                {
                    "role": "tool",
                    "name": tool_name,
                    "content": str(result)
                }
            )
    return "Max tours reached without a final answer.", trace


if __name__ == "__main__":
    question = "What is the result of 2 + 3*4?"
    answer, trace = loop(question)
    print(f"=" * 20)
    print("Trace:")
    print(f"-" * 20)
    for step in trace:
        print(step)
    print(f"=" * 20)
    print("Answer:", answer)
    print(f"=" * 20)
