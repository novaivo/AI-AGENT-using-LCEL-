from agent_logic import agent_executor
from dotenv import load_dotenv
import time
from langsmith import traceable


load_dotenv()

@traceable(name="run_agent")
def run_agent():
    """
    Executes the agent with user input and returns the response.
    """
    print("🌟✨ Welcome to Your AI Tool Buddy! ✨🌟")
    print("I'm a smart assistant powered by LLMs and tools 🧠🔧")
    print("Ask me anything about:")
    print("📂 CSV files   📊 SQLite databases   📍 Weather   🔢 Calculator   🌐 Wikipedia\n")
    print("💬 Type your question below — or press Ctrl+C to exit anytime.\n")

    try:
        while True:
            user_input = input("🧠 You: ")
            print("\n🤖 Agent is thinking... please wait ⏳")
            start = time.time()
            result = agent_executor.invoke({"input": user_input})
            end = time.time()
            duration = round(end - start, 2)
            print(f"\n🤖 Agent:\n{result}")
            print(f"\n⏱️ Response time: {duration} seconds.\n")
    except KeyboardInterrupt:
        print("\n👋 Goodbye! Thanks for chatting with me. Stay curious and keep building! 🌈🚀")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    run_agent()
