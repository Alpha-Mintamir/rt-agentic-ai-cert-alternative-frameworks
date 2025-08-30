from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="AIAssistant",
    instructions="You are a clear, helpful assistant for AI/ML concepts. Keep your answers brief.",
    model="gpt-4o-mini",
)


# Run the agent synchronously
result = Runner.run_sync(agent, "Can you explain what an AI agent is in simple terms?")
print(result.final_output)
