import os
import time
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder



load_dotenv()
my_apikey = os.getenv("openrouter_API_KEY")


def get_llm():
    try:
           return ChatOpenAI(
           model="meta-llama/llama-3-8b-instruct",
            base_url="https://openrouter.ai/api/v1",
           api_key=my_apikey,
           temperature=0.2
    )
    except Exception as e:
      print(f"Sorry! I'm having trouble thinking right now. Error: {str(e)}")
      return None
llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ("system", 
"""
You are a precise, tool-using AI assistant.

DO NOT guess answers. ALWAYS run the correct tool to get the answer.
If a tool fails, don't keep retrying other tools. Just explain what went wrong.
If a tool returns an error, show that error to the user. Never invent data.

Use the tools below:
- get_calculator → for math
- get_weather → for weather queries
- get_wikipedia → only if no file or database is mentioned
- get_csv_stats → for .csv files
- get_sqlite → for .db or SQL queries
- get_file → for .txt or .md files
- get_whatsapp_message → to send a user-requested message to whatsapp

You can use **get_whatsapp_message** if the user says:
- "Tell me on  whatsapp"
- "Send it to  whatsapp to this person "
- "Notify me there"
- "Push this to whatsapp"
- "Remind me via  whatsapp"
- Anything clearly asking for a get_whatsapp_message

In that case:
1. Run the appropriate tool first (e.g. get_weather, get_calculator)
2. Format the result into a clean message
3. Pass it into `get_whatsapp_message(message=...)`

ALWAYS:
1. Choose the correct tool
2. Run it
3. Wait for the tool output
4. If needed, send the result to Telegram using `telegram_notify`
5. THEN respond to the user clearly
"""
),

    ("human","{input}"),
     MessagesPlaceholder(variable_name="agent_scratchpad")


])
