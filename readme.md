# AI Agent with Local LLM & Real-Time Tools

## Objective
This project implements an AI assistant capable of intelligently deciding when to rely on its internal knowledge and when to trigger external tools.
It features **real-time API integration** for weather data and a safe calculator, running entirely locally using **Ollama (Mistral)**.

##  Technologies
- **Python 3.12+**
- **LangChain:** For agent orchestration.
- **Ollama (Mistral):** Local LLM selected for superior logical reasoning.
- **OpenWeatherMap API:** For real-time weather data.
- **UV:** For fast dependency management.

## How to Run

### 1. Prerequisites
- Install [Ollama](https://ollama.com/) and pull the Mistral model:
  ```bash
  ollama run mistral

    Get a free API Key from OpenWeatherMap.

2. Installation

Clone this repository and install the dependencies:
Bash

pip install -r requirements.txt

3. Configuration (.env)

Create a .env file in the root directory to store your API key securely. The project uses python-dotenv to load it.
Snippet de código

OPENWEATHER_API_KEY=your_api_key_here

> Note: If no key is provided, the weather tool will return a configuration error safely, but other tools will still work.
4. Execution

Run the main script to test Math, General Knowledge, and Real-time Weather:
Bash

python main.py

# Implementation Logic (ReAct)

I utilized the ReAct (Reason + Act) architecture:

    Routing: The Agent analyzes the user input.

        Math: Routes to Calculator (inputs sanitized via Python).

        Weather: Routes to WeatherTool (fetches real data via requests).

        General: Answers directly (bypassing tools).

    Prompt Engineering: implemented a Strict System Prompt to handle Local LLM behavior, enforcing negative constraints (e.g., "Do NOT output Action if you know the answer") to prevent hallucination loops.

Author: Eduardo Fontes Baltazar da Silveira
