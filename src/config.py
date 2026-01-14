import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

MODEL_NAME = "mistral"
TEMPERATURE = 0

AGENT_TEMPLATE = """Answer the following questions as best you can. You have access to the following tools:

{tools}

RULES:
1. Calculator input: ONLY numbers/operators.
2. Weather input: ONLY city name.
3. If you can answer without a tool (e.g. "Who is Einstein?"), output "Final Answer:" immediately. Do NOT output "Action:".
4. Do NOT make up tools. Only use [Calculator, Weather].
5. IMPORTANT: After you receive an Observation from a tool, your NEXT output MUST start with "Final Answer:". Do not think or explain anymore. Just give the answer.

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}] (OPTIONAL: skip if no tool is needed)
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}"""
