from unittest.mock import patch, MagicMock
from src.agent import initialize_agent
import src.config as config


# --- Happy Path Test ---
@patch("src.agent.ChatOllama")
@patch("src.agent.create_react_agent")
@patch("src.agent.AgentExecutor")
@patch("src.agent.get_tools")
def test_initialize_agent_success(
    mock_get_tools, mock_agent_executor, mock_create_react_agent, mock_chat_ollama
):
    """
    Verifies that the agent initializes correctly with the expected parameters
    and returns an Executor instance.
    """
    # 1. Setup mocks
    mock_tools = [MagicMock(name="Calculator"), MagicMock(name="Weather")]
    mock_get_tools.return_value = mock_tools

    # 2. Execution
    executor = initialize_agent()

    # 3. Assertions (Validations)

    # Check if LLM was initialized with correct config
    mock_chat_ollama.assert_called_once_with(model="mistral", temperature=0)

    # Check if tools were loaded
    mock_get_tools.assert_called()

    # Check if the agent was created using the config template
    # We verify if the prompt object passed to create_react_agent was created from our template
    args, _ = mock_create_react_agent.call_args
    # args[2] corresponds to the 'prompt' argument in create_react_agent(llm, tools, prompt)
    # We check if the prompt template string matches our config
    assert args[2].template == config.AGENT_TEMPLATE

    # Check if the function returns the executor
    assert executor == mock_agent_executor.return_value


# --- Error Handling Test ---
@patch("src.agent.ChatOllama")
@patch("sys.exit")
def test_initialize_agent_ollama_failure(mock_sys_exit, mock_chat_ollama):
    """
    Verifies that the system exits gracefully (sys.exit(1)) if Ollama
    is not reachable, instead of crashing with a raw stacktrace.
    """
    # 1. Setup: Simulate a Connection Error
    mock_chat_ollama.side_effect = Exception("Connection refused")

    # 2. Execution
    initialize_agent()

    # 3. Assertions
    # Ensure sys.exit(1) was called
    mock_sys_exit.assert_called_once_with(1)
