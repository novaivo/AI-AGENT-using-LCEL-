from agent_logic import agent_executor

def run_agent(input: str):
    """
    excutes the agent with user input and returns the response 
    """
    try:
        result = agent_executor.invoke({"input":input})
        return result 
    except Exception as e:
        return f"❌ Error: {str(e)} "


if __name__ == "__main__":
    print("🌟 Welcome to your AI Tool Buddy! 🤖✨")
    print("I'm ready to answer your questions using my smart toolbox! 🧠🔧")
    print("Type your question below, or press Ctrl+C anytime to exit gracefully 💫\n")
    
    while True:
        try:
            query = input("🧠 You: ")
            response = run_agent(query)
            print(f"🤖 Agent: {response}\n")
        except KeyboardInterrupt:
            print("\n👋 Bye bye! Thanks for chatting with me. Stay curious! 🌈✨")
            break
