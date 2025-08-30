# function_tools.py
from agents import Agent, Runner, function_tool
from dotenv import load_dotenv

load_dotenv()


# Define a function tool
@function_tool
def calculate_accuracy(correct: int, total: int) -> str:
    """Calculate accuracy given correct predictions and total samples."""
    accuracy = (correct / total) * 100
    return f"Accuracy: {accuracy:.2f}%"


# Create an agent that can use the tool
agent = Agent(
    name="ML Assistant",
    model="gpt-4o-mini",
    instructions=(
        "You answer machine learning questions clearly. "
        "If a calculation is needed, use the available tools. "
        "Always explain results briefly and clearly."
    ),
    tools=[calculate_accuracy],
)

# Run the agent with a specific task
result = Runner.run_sync(
    agent, input="A model got 504 correct out of 576 samples. What’s the accuracy?"
)
print(result.final_output)
