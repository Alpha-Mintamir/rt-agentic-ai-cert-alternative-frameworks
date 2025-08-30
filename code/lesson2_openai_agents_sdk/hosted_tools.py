"""Example of using a hosted tool with an agent."""

from agents import Agent, Runner, WebSearchTool
from dotenv import load_dotenv

load_dotenv()

# Define an agent with a hosted web search tool
agent = Agent(
    name="AI News Assistant",
    model="gpt-4o-mini",
    instructions=(
        "You fetch information using WebSearchTool and present it clearly. "
        "Summarize into 3–5 concise bullet points. "
        "Each bullet ≤ 20 words and cite the source in parentheses. "
        "Prefer official blog posts or top-tier outlets. "
        "If little information is found, say 'No major updates.'"
    ),
    tools=[WebSearchTool()],
)

# Run the agent synchronously
result = Runner.run_sync(
    agent, input="Get today's AI headlines and summarize them as instructed."
)
print(result.final_output)
