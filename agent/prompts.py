from langchain_core.prompts import ChatPromptTemplate

SYSTEM_PROMPT = """You are a helpful AI assistant powered by LangChain.
You have access to a set of tools to help you answer user questions.
Always think step-by-step before answering.
If you don't know the answer, say so.
"""

def get_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("user", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])
