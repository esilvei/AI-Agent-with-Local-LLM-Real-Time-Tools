from agent import initialize_agent


def main():
    agent_executor = initialize_agent()

    print("\n--- 1. Math Test (Mandatory Requirement) ---")
    try:
        # Should trigger the Calculator
        res = agent_executor.invoke({"input": "Calculate 128 * 46"})
        print(f"📍 Final Answer: {res['output']}")
    except Exception as e:
        print(f"Error: {e}")

    print("\n--- 2. General Knowledge Test (Mandatory Requirement) ---")
    try:
        # Should answer directly without tools
        res = agent_executor.invoke(
            {"input": "Who was Albert Einstein? Answer briefly."}
        )
        print(f"📍 Final Answer: {res['output']}")
    except Exception as e:
        print(f"Error: {e}")

    print("\n--- 3. Weather Test (Creative Bonus) ---")
    try:
        # Should trigger the Weather tool
        res = agent_executor.invoke({"input": "What is the weather in London?"})
        print(f"📍 Final Answer: {res['output']}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
