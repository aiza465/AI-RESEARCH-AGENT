from app.agent import run_agent

if __name__ == "__main__":
    print("\nAI Research Assistant (type 'exit' to stop)\n")

    while True:
        user_input = input("Ask: ")

        if user_input == "exit":
            break

        response = run_agent(user_input)

        print("\nAnswer:\n", response)
        print("\n" + "-"*50 + "\n")
