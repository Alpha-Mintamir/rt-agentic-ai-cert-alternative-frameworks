# example_agents_as_tools.py
from agents import Agent, Runner
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

# Define an orchestrator agent that can call the translators as tools
orchestrator_agent = Agent(
    name="Orchestrator",
    model="gpt-4o-mini",
    instructions=(
        "You are a translation assistant. "
        "Use the available tools to translate text into the requested language. "
        "Just return the translated text. Do not explain or repeat the original."
    ),
    tools=[
        spanish_agent.as_tool("translate_to_spanish", "Translate to Spanish"),
        french_agent.as_tool("translate_to_french", "Translate to French"),
    ],
)

# Run the orchestrator synchronously
result = Runner.run_sync(
    orchestrator_agent, input="Translate 'Good morning, everyone!' to French."
)
print(result.final_output)
