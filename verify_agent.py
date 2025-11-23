import os
import dotenv
from agent.bot import build_agent

dotenv.load_dotenv()

def test_agent():
    if not os.getenv("OPENAI_API_KEY"):
        print("SKIPPING TEST: OPENAI_API_KEY not found.")
        return

    print("Building agent...")
    try:
        agent = build_agent()
        print("Agent built successfully.")
        
        print("Running test query: 'What is 5 + 7?'")
        # Invoke the agent with a simple math question to trigger the tool
        response = agent.invoke({"messages": [("user", "What is 5 + 7?")]})
        
        last_message = response["messages"][-1]
        print(f"Agent Response: {last_message.content}")
        
        if "12" in last_message.content:
            print("SUCCESS: Agent calculated correctly.")
        else:
            print("WARNING: Agent response did not contain expected answer '12'.")

    except Exception as e:
        print(f"FAILED: {e}")

if __name__ == "__main__":
    test_agent()
