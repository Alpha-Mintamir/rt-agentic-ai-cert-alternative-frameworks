from agents import Agent, Runner, handoff
from dotenv import load_dotenv

load_dotenv()

# Define specialized agents
spanish_agent = Agent(
    name="SpanishAgent",
    model="gpt-4o-mini",
    instructions="Translate any input text into Spanish.",
)

french_agent = Agent(
    name="FrenchAgent",
    model="gpt-4o-mini",
    instructions="Translate any input text into French.",
)

# Create handoffs (no name argument!)
spanish_handoff = handoff(spanish_agent)
french_handoff = handoff(french_agent)

# Define orchestrator agent with handoffs
orchestrator_agent = Agent(
    name="Orchestrator",
    model="gpt-4o-mini",
    instructions=(
        "You are a translation assistant. "
        "Use the available handoffs to translate input text into the requested language."
    ),
    handoffs=[spanish_handoff, french_handoff],
)

# Run the orchestrator synchronously
result = Runner.run_sync(
    orchestrator_agent, input="Translate 'Good night, everyone!' to Spanish."
)
print(result.final_output)
