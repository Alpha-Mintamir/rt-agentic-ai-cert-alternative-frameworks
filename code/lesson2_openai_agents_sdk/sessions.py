from agents import Agent, Runner, SQLiteSession
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="DSAssistant",
    instructions=(
        "You are a helpful assistant for data scientists. "
        "Keep responses short (under 50 words) and relevant."
    ), 
    model="gpt-4o-mini",
)

session = SQLiteSession("project123")  # Conversation memory


# First question
question1 = "What’s a good metric for imbalanced classification?"
result1 = Runner.run_sync(
    agent,
    question1, 
    session=session
)
print("-" * 80)
print("Question 1: ", question1)
print(f"Answer: {result1.final_output}")
print("-" * 80)

# Follow-up question
question2 = "Can I use SkLearn to calculate it?"
print("Question 2 :", question2)
result2 = Runner.run_sync(
    agent,
    question2,
    session=session
)
print(f"Answer: {result2.final_output}")
print("-" * 80)
