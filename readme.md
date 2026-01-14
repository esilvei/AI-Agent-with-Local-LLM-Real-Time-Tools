# AI Agent with Local LLM & Real-Time Tools

## Objective
This project implements an AI assistant capable of intelligently deciding when to rely on its internal knowledge and when to trigger external tools. It features real-time API integration for weather data and a safe calculator, running entirely locally using **Ollama (Mistral)**.

## Technologies
- **Python 3.12+**
- **LangChain:** For agent orchestration and ReAct logic.
- **Ollama (Mistral):** Local LLM selected for superior logical reasoning without API costs.
- **OpenWeatherMap API:** For real-time weather data fetching.
- **UV:** For extremely fast dependency management.
- **Quality Assurance:** `pytest` for unit testing and `ruff` for linting.

---

## How to Run

### 1. Prerequisites
- **Ollama:** Install [Ollama](https://ollama.com/) and pull the Mistral model:
  ```bash
  ollama run mistral

    API Key: Get a free API Key from OpenWeatherMap.

### 2. Installation

Clone this repository and install the dependencies. Since this project uses uv, you can sync instantly:
Bash

#### Recommended (using uv)
uv sync

#### Standard (using pip)
pip install -r requirements.txt

### 3. Configuration (.env)

Create a .env file in the root directory to store your API key securely:
Snippet de código

OPENWEATHER_API_KEY=your_api_key_here

Note: If no key is provided, the weather tool will handle the error gracefully, but other tools will still work.
###  4. Execution

Run the main script to test Math, General Knowledge, and Real-time Weather:
Bash

#### Using uv
uv run src/main.py

#### Or standard python
python src/main.py

### 5. Running Tests

To verify the integrity of the tools and the agent configuration:
Bash

uv run pytest -v

Implementation Logic (ReAct)

I utilized the ReAct (Reason + Act) architecture:

    Routing: The Agent analyzes the user input.

        Math: Routes to Calculator (inputs sanitized via Python to prevent injection).

        Weather: Routes to WeatherTool (fetches real data via requests).

        General: Answers directly (bypassing tools).

    Prompt Engineering: Implemented a Strict System Prompt to handle Local LLM behavior, enforcing negative constraints (e.g., "Do NOT output Action if you know the answer") to prevent hallucination loops common in smaller models.

    Code Quality: Implemented Git Hooks (pre-commit) to ensure every commit is tested and formatted according to PEP-8 standards.

Lessons Learned & Future Improvements

(Challenge Requirement)

What I Learned:

    How to orchestrate local LLMs effectively using LangChain and custom prompts to avoid loops.

    The importance of mocking external APIs (unittest.mock) to create reliable unit tests.

What I would do differently (with more time):

    Conversation Memory: Implement ChatHistory so the agent remembers previous context.

    Frontend: Build a simple UI using Streamlit or Chainlit.

    Docker: Containerize the application for easier deployment.

Author: Eduardo Fontes Baltazar da Silveira

u `readme.md` com esse conteúdo e fazer o push final. **Desafio c**
