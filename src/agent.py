import sys
from langchain_community.chat_models import ChatOllama
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
from tools import get_tools
import config


def initialize_agent():
    print("⏳ Initializing Mistral (Ollama)...")

    try:
        llm = ChatOllama(model="mistral", temperature=0)
    except Exception as e:
        print(f"Critical Error: Could not connect to Ollama. {e}")
        sys.exit(1)
        return None

    tools = get_tools()
    tools = get_tools()

    template = config.AGENT_TEMPLATE

    prompt = PromptTemplate.from_template(template)

    agent = create_react_agent(llm, tools, prompt)

    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=5,
    )
